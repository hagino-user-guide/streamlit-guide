
                                    if (px >= canvasWidth / 2) {
                                        ttLeft = clamp(px - pinHalfW - gap - ttWidth, edgePad, canvasWidth - ttWidth - edgePad);
                                    } else {
                                        ttLeft = clamp(px + pinHalfW + gap, edgePad, canvasWidth - ttWidth - edgePad);
                                    }

                                    const stillOverlaps = !(
                                        ttLeft + ttWidth + 8 < pinLeft ||
                                        ttLeft - 8 > pinRight ||
                                        ttTop + ttHeight + 8 < pinTop ||
                                        ttTop - 8 > pinBottom
                                    );

                                    if (stillOverlaps) {
                                        if (py >= canvasHeight / 2) {
                                            ttTop = clamp(py - pinHalfH - gap - ttHeight, edgePad, canvasHeight - ttHeight - edgePad);
                                        } else {
                                            ttTop = clamp(py + pinHalfH + gap, edgePad, canvasHeight - ttHeight - edgePad);
                                        }
                                    }
                                }

                                dynamicTooltip.style.left = ttLeft + 'px';
                                dynamicTooltip.style.top = ttTop + 'px';
                                dynamicTooltip.style.visibility = 'visible';

                                requestAnimationFrame(function() {
                                    const tooltipRect = dynamicTooltip.getBoundingClientRect();
                                    const localLeft = tooltipRect.left - canvasRect.left;
                                    const localTop = tooltipRect.top - canvasRect.top;
                                    const localRight = localLeft + tooltipRect.width;
                                    const localBottom = localTop + tooltipRect.height;

                                    let targetX = clamp(px, localLeft + 16, localRight - 16);
                                    let targetY = clamp(py, localTop + 14, localBottom - 14);

                                    if (px < localLeft) targetX = localLeft;
                                    if (px > localRight) targetX = localRight;
                                    if (py < localTop) targetY = localTop;
                                    if (py > localBottom) targetY = localBottom;

                                    const dx = targetX - px;
                                    const dy = targetY - py;
                                    const length = Math.max(0, Math.sqrt(dx * dx + dy * dy) - 3);
                                    const angle = Math.atan2(dy, dx) * 180 / Math.PI;

                                    dynamicLine.style.left = px + 'px';
                                    dynamicLine.style.top = py + 'px';
                                    dynamicLine.style.width = length + 'px';
                                    dynamicLine.style.transform = 'rotate(' + angle + 'deg)';
                                    dynamicLine.classList.add('show');
                                });
                            });
                        });
                    });

                    if (canvasContainer) {
                        canvasContainer.addEventListener('click', function() {
                            if (dynamicTooltip) dynamicTooltip.classList.remove('show');
                            if (dynamicLine) dynamicLine.classList.remove('show');
                            canvasContainer.classList.remove('has-selection');
                            document.querySelectorAll('.hotspot-btn').forEach(p => p.classList.remove('active'));
                        });
                    }

                    document.querySelectorAll('.page-trigger').forEach(card => {
                        card.addEventListener('click', function() {
                            const targetPageId = this.getAttribute('data-target');
                            const targetPage = document.getElementById(targetPageId);
                            const homePage = document.getElementById('page-home');
                            if (targetPage && homePage) {
                                homePage.className = 'page-view';
                                document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
                                targetPage.classList.add('active');
                                if (kitchenSink) kitchenSink.scrollTop = 0;
                            }
                        });
                    });

                    document.querySelectorAll('.back-to-home-trigger').forEach(btn => {
                        btn.addEventListener('click', function() {
                            const parentPage = this.closest('.page-view');
                            if (parentPage) parentPage.classList.remove('active');
                            const homePage = document.getElementById('page-home');
                            if (homePage) homePage.classList.add('active');
                            if (kitchenSink) kitchenSink.scrollTop = 0;
                        });
                    });

                    /* 🎯 アコーディオン制御JS（車内案内は常に1件のみ、他ページは従来動作） */
                    document.querySelectorAll('.simple-accordion').forEach(acc => {
                        const header = acc.querySelector('.accordion-header');
                        if (!header) return;

                        const toggleAccordion = function() {
                            const willOpen = !acc.classList.contains('open');
                            const singleOpenPage = acc.closest('#page-manner, #page-help');

                            if (singleOpenPage && willOpen) {
                                singleOpenPage.querySelectorAll('.simple-accordion.open').forEach(other => {
                                    if (other !== acc) {
                                        other.classList.remove('open');
                                        const otherHeader = other.querySelector('.accordion-header');
                                        if (otherHeader) otherHeader.setAttribute('aria-expanded', 'false');
                                    }
                                });
                            }

                            acc.classList.toggle('open', willOpen);
                            header.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
                        };

                        header.addEventListener('click', toggleAccordion);
                        header.addEventListener('keydown', function(e) {
                            if (e.key === 'Enter' || e.key === ' ') {
                                e.preventDefault();
                                toggleAccordion();
                            }
                        });
                    });

                    const stationGroups = {
                        kanto: ["バスタ新宿4F", "八王子駅南口バスターミナル", "高尾駅南口", "バスターミナル東京八重洲地下A", "大宮駅西口", "横浜シティ・エア・ターミナル"],
                        kansai: ["ＯＣＡＴ 難波バスターミナル", "プラザモータープール", "天王寺公園東バス駐車場", "京都駅八条口", "奈良駅東口"]
                    };

                    const stationMeta = {
                        "バスタ新宿4F": "新宿高速バスターミナル",
                        "八王子駅南口バスターミナル": "JR八王子駅 南口",
                        "高尾駅南口": "JR高尾駅 南口",
                        "バスターミナル東京八重洲地下A": "東京駅八重洲 地下のりば",
                        "大宮駅西口": "JR大宮駅 西口",
                        "横浜シティ・エア・ターミナル": "YCAT",
                        "ＯＣＡＴ 難波バスターミナル": "JR難波駅直結 OCAT",
                        "プラザモータープール": "大阪・梅田",
                        "天王寺公園東バス駐車場": "天王寺公園東側",
                        "京都駅八条口": "京都駅 八条口",
                        "奈良駅東口": "JR奈良駅 東口"
                    };

                    function stationMenuCard(name) {
                        const subtitle = stationMeta[name] ? `<span class="station-btn-subtitle">${stationMeta[name]}</span>` : '';
                        return `<div class="station-menu-btn station-menu-btn-js" role="button" tabindex="0" data-name="${name}"><div class="station-btn-title-wrap"><span class="station-pin-icon-pink"><i class="ph-bold ph-map-pin"></i></span><span class="station-title-stack"><span class="station-name">${name}</span>${subtitle}</span></div><span class="station-chevron-right"><i class="ph-bold ph-caret-right"></i></span></div>`;
                    }

                    function bindModalEvents() {
                        document.querySelectorAll('.station-menu-btn-js').forEach(btn => {
                            btn.addEventListener('click', function() { showStationDetail(this.getAttribute('data-name')); });
                            btn.addEventListener('keydown', function(e) {
                                if (e.key === 'Enter' || e.key === ' ') {
                                    e.preventDefault();
                                    showStationDetail(this.getAttribute('data-name'));
                                }
                            });
                        });
                        const backBtn = document.getElementById('js-back-to-list');
                        if (backBtn) { backBtn.addEventListener('click', showStationMenuModal); }
                        
                        const toggleTrigger = document.getElementById('js-toggle-script');
                        if (toggleTrigger) {
                            toggleTrigger.addEventListener('click', function(e) {
                                e.stopPropagation();
                                const box = document.getElementById('announcement_script_box');
                                if (box) { box.style.display = (box.style.display === 'block') ? 'none' : 'block'; }
                            });
                        }
                    }

                    function openModal(title, html) {
                        if(mask && modalTitle && modalBody) {
                            mask.classList.add('show');
                            modalTitle.innerText = title;
                            modalBody.innerHTML = html;
                            bindModalEvents();
                        }
                    }
                    
                    const modalCloseBtn = document.getElementById('modal-close-btn');
                    if (modalCloseBtn) {
                        modalCloseBtn.addEventListener('click', function() {
                            if (mask && modalBody) {
                                mask.classList.remove('show');
                                modalBody.innerHTML = '';
                            }
                        });
                    }

                    function showStationMenuModal() {
                        let html = '<div class="station-menu-list"><div class="station-menu-group-title group-kanto"><i class="ph-bold ph-map-trifold"></i>関東エリア</div>';
                        stationGroups.kanto.forEach(name => {
                            html += stationMenuCard(name);
                        });
                        html += '<div class="station-menu-group-title group-kansai"><i class="ph-bold ph-map-trifold"></i>関西エリア</div>';
                        stationGroups.kansai.forEach(name => {
                            html += stationMenuCard(name);
                        });
                        html += '</div>';
                        openModal("乗車・降車場所を選択", html);
                    }
                    
                    function showStationDetail(name) {
                        const html = [
                            '<div class="detail-back-btn" id="js-back-to-list" style="font-size:12.5px; color:#64748B; cursor:pointer; margin-bottom:14px; font-weight:bold; text-align:left;">◀ 乗り場一覧に戻る</div>',
                            '<div style="text-align:left; width:100%; box-sizing:border-box;">',
                            `  <h3 style="font-size:14px; font-weight:800; color:#005bac; margin:0 0 12px 0; padding-bottom:8px; border-bottom:1px solid #E2E8F0;">${name}</h3>`,
                            '  <div class="station-emergency-card">',
                            '      <div class="station-emergency-head"><i class="ph-bold ph-siren"></i>直前連絡先</div>',
                            '      <div class="station-emergency-points"><span><i class="ph-bold ph-clock"></i>出発30分前から利用可能</span><span><i class="ph-bold ph-warning-circle"></i>緊急時のみ利用</span></div>',
                            '      <a class="station-phone-btn" href="tel:05038510388"><i class="ph-bold ph-phone-call"></i><span>050-3851-0388</span></a>',
                            '  </div>',
                            `  <button class="station-map-btn" onclick="alert('${name}の地図アプリを開きます')"><i class="ph-bold ph-map-pin"></i><span>Googleマップで見る</span></button>`,
                            '</div>'
                        ].join('');
                        openModal("乗り場詳細案内", html);
                    }

                    const triggerStations = document.getElementById('trigger-stations');
                    if(triggerStations) { triggerStations.addEventListener('click', showStationMenuModal); }
                    /* ナイトライナー限定サービス：2列グリッド＋一覧下の共通詳細カード */
                    const amenityDetailData = {
                        blanket: {
                            title: 'ブランケット',
                            icon: 'ph-article',
                            photo: '__AMENITY_BLANKET_PHOTO__',
                            html: '大判ブランケットをお一人様1枚、座席にご用意しております。<span class="amenity-detail-highlight">3列独立シートをご利用のお客様は、乗務員へお声がけいただくと、もう1枚追加で貸し出し可能です。</span>'
                        },
                        water: {
                            title: 'ミネラルウォーター',
                            icon: 'ph-drop',
                            photo: '__AMENITY_SET_PHOTO__',
                            html: 'ペットボトルのミネラルウォーターを、お一人様1本ご用意しております。'
                        },
                        cushion: {
                            title: '腰あてクッション',
                            icon: 'ph-sidebar-simple',
                            photo: '__AMENITY_SET_PHOTO__',
                            html: '長時間でも快適にお過ごしいただけるよう、腰あてクッションを全席にご用意しております。'
                        },
                        mask: {
                            title: 'フェイスマスク',
                            icon: 'ph-smiley-blank',
                            photo: '__AMENITY_SET_PHOTO__',
                            html: 'お肌にやさしいフェイスマスクを全席にご用意しております。'
                        }
                    };

                    const amenityDetailShell = document.getElementById('js-amenity-detail-shell');
                    const amenityDetailTitle = document.getElementById('js-amenity-detail-title');
                    const amenityDetailText = document.getElementById('js-amenity-detail-text');
                    const amenityDetailIcon = document.getElementById('js-amenity-detail-icon');
                    let activeAmenityKey = null;

                    document.querySelectorAll('.amenity-select-card').forEach(card => {
                        card.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const key = this.getAttribute('data-amenity');
                            const data = amenityDetailData[key];
                            if (!data || !amenityDetailShell) return;

                            const closeCurrent = activeAmenityKey === key && amenityDetailShell.classList.contains('is-open');
                            document.querySelectorAll('.amenity-select-card').forEach(item => {
                                item.classList.remove('is-active');
                                item.setAttribute('aria-pressed', 'false');
                            });

                            if (closeCurrent) {
                                activeAmenityKey = null;
                                amenityDetailShell.classList.remove('is-open');
                                amenityDetailShell.setAttribute('aria-hidden', 'true');
                                return;
                            }

                            activeAmenityKey = key;
                            this.classList.add('is-active');
                            this.setAttribute('aria-pressed', 'true');
                            if (amenityDetailTitle) amenityDetailTitle.textContent = data.title;
                            if (amenityDetailText) {
                                const photoHtml = data.photo ? '<img class="amenity-detail-photo" src="' + data.photo + '" alt="' + data.title + 'の写真">' : '';
                                amenityDetailText.innerHTML = '<div class="amenity-detail-layout">' + photoHtml + '<div class="amenity-detail-copy">' + data.html + '</div></div>';
                            }
                            if (amenityDetailIcon) amenityDetailIcon.innerHTML = '<i class="ph-bold ' + data.icon + '"></i>';
                            amenityDetailShell.classList.add('is-open');
                            amenityDetailShell.setAttribute('aria-hidden', 'false');
                        });
                    });



                    document.querySelectorAll('.modal-trigger').forEach(trigger => {
                        trigger.addEventListener('click', function() { openModal(this.getAttribute('data-title'), this.getAttribute('data-desc')); });
                    });

                    const schedBtn = document.getElementById('trigger-schedule');
                    if (schedBtn) {
                        schedBtn.addEventListener('click', function() {
                            const selectVal = document.getElementById('bus_select').value;
                            const targetData = schedules[selectVal];
                            if (targetData) { openModal(targetData.title, targetData.html); }
                        });
                    }

                    const btnS3 = document.getElementById('js-btn-seat3');
                    const btnS4 = document.getElementById('js-btn-seat4');
                    if(btnS3 && btnS4) {
                        btnS3.addEventListener('click', function() {
                            btnS4.classList.remove('active'); btnS3.classList.add('active');
                            applySeatLayout('seat3');
                        });
                        btnS4.addEventListener('click', function() {
                            btnS3.classList.remove('active'); btnS4.classList.add('active');
                            applySeatLayout('seat4');
                        });
                    }

                    const floatTopBtn = document.getElementById('js-float-top');
                    if (floatTopBtn) {
                        floatTopBtn.addEventListener('click', function() {
                            window.scrollTo({ top: 0, behavior: 'smooth' });
                            try {
                                window.parent.scrollTo({ top: 0, behavior: 'smooth' });
                            } catch (e) {
                                window.parent.postMessage({ type: 'nightliner:scrollTop' }, '*');
                            }
                        });
                    }



                    // Streamlit iframeをコンテンツの実高に追従させ、内部スクロールを作らない
                    const notifyStreamlitHeight = () => {
                        const height = Math.max(
                            document.documentElement.scrollHeight,
                            document.body.scrollHeight,
                            document.documentElement.offsetHeight,
                            document.body.offsetHeight
                        );
                        window.parent.postMessage({
                            isStreamlitMessage: true,
                            type: 'streamlit:setFrameHeight',
                            height: height
                        }, '*');
                    };

                    let heightRaf = null;
                    const scheduleHeightUpdate = () => {
                        if (heightRaf) cancelAnimationFrame(heightRaf);
                        heightRaf = requestAnimationFrame(() => {
                            notifyStreamlitHeight();
                            heightRaf = null;
                        });
                    };

                    if ('ResizeObserver' in window) {
                        const resizeObserver = new ResizeObserver(scheduleHeightUpdate);
                        resizeObserver.observe(document.documentElement);
                        resizeObserver.observe(document.body);
                        const appWrapper = document.getElementById('js-app-wrapper');
                        if (appWrapper) resizeObserver.observe(appWrapper);
                    }
                    window.addEventListener('load', scheduleHeightUpdate);
                    window.addEventListener('resize', scheduleHeightUpdate);
                    document.addEventListener('click', scheduleHeightUpdate, true);
                    setTimeout(scheduleHeightUpdate, 0);
                    setTimeout(scheduleHeightUpdate, 300);

                    const foodBtn = document.getElementById('js-trigger-manner-food');
                    if (foodBtn) {
                        foodBtn.addEventListener('click', function() {
                            const html = [
                                '<div style="display:flex; flex-direction:column; gap:12px; padding:4px 2px; text-align:left;">',
                                '  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:14px; display:flex; align-items:flex-start; gap:10px;"><span style="font-size:16px;">🍔</span><p style="font-size:12.5px; font-weight:600; color:#334155; margin:0; line-height:1.5;">ファストフードやカップ麺など、<strong>匂いが車内に広がる食べ物の持ち込み・飲食はご遠慮</strong>ください。</p></div>',
                                '  <div style="background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:14px; display:flex; align-items:flex-start; gap:10px;"><span style="font-size:16px;">🍿</span><p style="font-size:12.5px; font-weight:600; color:#334155; margin:0; line-height:1.5;">静かな車内でバリバリと大きな音が鳴るスナック類もお控えください。おにぎりやパンなど匂いがなく音のしないもの、および蓋の完全に閉まるペットボトル飲料等の持ち込みは問題ありません。</p></div>',
                                '</div>'
                            ].join('');
                            openModal("車内での飲食制限について", html);
                        });
                    }

                }

                if (document.readyState !== 'loading') {
                    initApp();
                } else {
                    document.addEventListener('DOMContentLoaded', initApp);
                }
            </script>
        </body>
        </html>
    """
    html = (
        html
        .replace("__SEAT3_PHOTO__", seat3_photo)
        .replace("__SEAT4_PHOTO__", seat4_photo)
        .replace("__OVERHEAD_PHOTO__", overhead_photo)
        .replace("__AMENITY_BLANKET_PHOTO__", amenity_blanket_photo)
        .replace("__AMENITY_SET_PHOTO__", amenity_set_photo)
    )
    st.components.v1.html(html, height=1, scrolling=False)

if __name__ == "__main__":
    main()
