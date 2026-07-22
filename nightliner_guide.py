import base64
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"


def image_data_uri(filename):
    path = ASSET_DIR / filename
    if not path.exists():
        return ""
    mime = {
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".webp": "image/webp",
    }.get(path.suffix.lower(), "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")

def main():
    st.set_page_config(page_title="NIGHTLINER App Guide", layout="wide")
    
    # 🎯 実際にassetsフォルダにあるファイル名に修正しました
    seat3_photo = image_data_uri("seat_3_main.jpg")
    seat4_photo = image_data_uri("seat_4_main.jpg")
    overhead_photo = image_data_uri("seat_overhead_console.jpg")
    amenity_blanket_photo = image_data_uri("amenity_blanket.jpg")
    amenity_set_photo = image_data_uri("amenity_set.jpg")

    # 未用意の画像は空文字に設定
    recline_position_photo = image_data_uri("seat_recline_position_web.jpg")
    recline_operation_photo = image_data_uri("seat_recline_operation_web.jpg")
    seat4_recline_aisle_position_photo = image_data_uri("seat4_recline_aisle_position_web.jpg")
    seat4_recline_aisle_operation_photo = image_data_uri("seat4_recline_aisle_operation_web.jpg")
    seat4_recline_window_position_photo = image_data_uri("seat4_recline_window_position_web.jpg")
    seat4_recline_window_operation_photo = image_data_uri("seat4_recline_window_operation_web.jpg")
    seat4_power_usb_photo = image_data_uri("seat4_power_usb_web.jpg")
    air_vent_open_photo = image_data_uri("seat_air_vent_open_web.jpg")
    air_vent_closed_photo = image_data_uri("seat_air_vent_closed_web.jpg")
    side_table_unlock_photo = image_data_uri("seat_side_table_unlock_web.jpg")
    side_table_deployed_photo = image_data_uri("seat_side_table_deployed_web.jpg")
    legrest_operation_photo = image_data_uri("seat_legrest_operation_web.jpg")
    armrest_lever_position_photo = image_data_uri("seat_armrest_lever_position_web.jpg")
    armrest_lever_operation_photo = image_data_uri("seat_armrest_lever_operation_web.jpg")
    footrest_photo = image_data_uri("seat_footrest_web.jpg")
    
    # 🎯 画面外枠（Streamlit標準のヘッダー・フッター等）を消去するCSS
    st.markdown("""
        <style>
        header, [data-testid="stHeader"], footer, #MainMenu, [data-testid="stSidebar"], [data-testid="stTopBar"], div[data-testid="stTextInput"] { 
            display: none !important; 
        }
        .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 !important; }
        [data-testid="stAppViewContainer"] { background-color: #E2E8F0 !important; }
        div[data-testid="stVerticalBlock"] { gap: 0rem !important; padding: 0 !important; margin: 0 !important; }
        </style>
    """, unsafe_allow_html=True)

    # 🎯 メインのアプリ風UI（HTML / CSS / JavaScript）
    html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scalable=no, user-scalable=no">
            <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/bold/style.css">
            <style>
                /* ── 全体ベーススタイル ── */
                html, body {
                    margin: 0; padding: 0; min-height: 100%; background-color: #E2E8F0;
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                    display: block; width: 100%; overflow-x: hidden; overflow-y: visible;
                    pointer-events: auto !important;
                }
                body, input, select, button, textarea {
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
                }
                .app-wrapper {
                    width: 100%; max-width: 430px; background-color: #FFFFFF; min-height: 0; margin: 0 auto;
                    box-shadow: 0 0 30px rgba(0,0,0,0.1); display: flex; flex-direction: column;
                    box-sizing: border-box; overflow-x: hidden; overflow-y: visible; position: relative; z-index: 10;
                }
                
                /* ── 🚍 LP風リデザインヘッダー（白文字・上質な夜空演出） ── */
                .app-fixed-top { position: sticky; top: 0; left: 0; width: 100%; z-index: 100; flex-shrink: 0; }
                .app-header {
                    background: linear-gradient(135deg, #000c24 0%, #001947 60%, #022763 100%);
                    padding: 22px 24px 18px 24px; color: #FFFFFF; position: relative; overflow: hidden; text-align: left; border-bottom: 2px solid #005bac; isolation: isolate;
                }
                .app-header::before {
                    content: ''; position: absolute; top: 18px; right: 64px; width: 15px; height: 15px;
                    border-radius: 50%; background: transparent;
                    box-shadow: 5px 0 0 0 rgba(255,255,255,0.55), 8px 0 12px rgba(255,255,255,0.08);
                    transform: rotate(-18deg); opacity: 0.8; pointer-events: none; z-index: 1;
                }
                /* 薄い星空の配置 */
                .app-header-stars {
                    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0;
                    background-image: 
                        radial-gradient(1.4px 1.4px at 26px 18px, rgba(255,255,255,0.95), transparent),
                        radial-gradient(1.2px 1.2px at 98px 32px, rgba(255,255,255,0.72), transparent),
                        radial-gradient(1.8px 1.8px at 154px 14px, rgba(255,255,255,0.9), transparent),
                        radial-gradient(1.2px 1.2px at 226px 39px, rgba(255,255,255,0.62), transparent),
                        radial-gradient(1.3px 1.3px at 326px 19px, rgba(255,255,255,0.68), transparent),
                        radial-gradient(1.7px 1.7px at 356px 30px, rgba(255,255,255,0.86), transparent),
                        radial-gradient(1.1px 1.1px at 392px 15px, rgba(255,255,255,0.66), transparent);
                    opacity: 0.72; pointer-events: none;
                }
                /* 高速道路の光跡（薄い白線） */
                .app-header-highway {
                    position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0;
                    background: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="430" height="104" viewBox="0 0 430 104"><path d="M-10,92 Q190,59 440,44 M-10,98 Q190,64 440,49 M-10,84 Q190,73 440,69" stroke="%23ffffff" stroke-width="1.1" fill="none" opacity="0.014"/></svg>') no-repeat;
                    background-size: cover; pointer-events: none;
                }
                .app-header-tagline { position: relative; z-index: 2; display: inline-flex; align-items: center; width: fit-content; padding: 3px 9px 3px 10px; border: 1px solid rgba(255,255,255,0.22); border-radius: 999px; background: rgba(255,255,255,0.08); font-size: 12.5px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.12em; margin-bottom: 6px; opacity: 0.94; line-height: 1; }
                .app-header h1 { position: relative; z-index: 2; font-size: 28px !important; font-weight: 850 !important; margin: 0 0 8px 0 !important; color: #FFFFFF !important; letter-spacing: 0.015em; line-height: 1 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.18); }
                .app-header p { position: relative; z-index: 2; font-size: 12.2px !important; color: #FFFFFF !important; margin: 0 !important; font-weight: 500 !important; opacity: 0.9; line-height: 1.42 !important; max-width: 320px; }
                
                .app-scroll-body { flex: 1; overflow-x: hidden; overflow-y: visible; padding: 8px 16px calc(60px + env(safe-area-inset-bottom, 0px)) 16px; box-sizing: border-box; background-color: #FFFFFF; display: flex; flex-direction: column; width: 100%; position: relative; z-index: 10; }
                .page-view { display: none; width: 100%; box-sizing: border-box; }
                .page-view.active { display: flex !important; flex-direction: column !important; }

                /* パンくずリスト */
                .breadcrumb-bar { display: flex; align-items: center; gap: 6px; margin: 6px 0 14px 2px; padding-bottom: 8px; border-bottom: 1px solid #F1F5F9; }
                .breadcrumb-back { font-size: 12.5px; font-weight: 800; color: #64748B; cursor: pointer; display: flex; align-items: center; gap: 3px; }
                .breadcrumb-current { font-size: 12.5px; font-weight: 800; }

                /* 大見出し */
                .heading { 
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
                    font-size: 14px !important; color: #005bac !important; border-left: 4px solid #005bac !important; padding-left: 10px !important; margin: 22px 0 14px 0 !important; 
                    font-weight: 800 !important; width: 100%; box-sizing: border-box; 
                }
                .heading:first-of-type { margin-top: 4px; }

                /* 当日の流れ・のりばページ */
                #page-today .heading { color: #10B981 !important; border-left-color: #10B981 !important; }
                #page-today .step-badge-node { color: #047857; background: #ECFDF5; }
                #page-today .step-icon-inline { color: #10B981; }
                #page-today .step-premium-card { flex: 0 0 178px; min-height: 164px; padding: 16px 14px; border-color: #D1FAE5; box-shadow: 0 4px 12px rgba(16,185,129,0.04); }
                #page-today .step-scroll-wrapper { gap: 12px; padding: 8px 2px 16px 2px; }
                #page-today .step-outer-container-js { display: block !important; margin-bottom: 4px; }
                #page-today #trigger-schedule { border-color: #A7F3D0 !important; background: #FFFFFF; }
                #page-today #trigger-schedule .item-title { color: #065F46 !important; }
                #page-today .today-scroll-hint { display: none; }
                #page-today #trigger-stations { border-color: #D1FAE5 !important; }
                #page-today #trigger-stations .item-icon-container { background-color: #ECFDF5 !important; color: #10B981 !important; }
                #page-today #trigger-stations .item-title { color: #1E293B !important; }
                #page-today #trigger-schedule .item-arrow, #page-today #trigger-stations .item-arrow { width: 26px; height: 26px; border-radius: 50%; background: #ECFDF5; color: #059669 !important; justify-content: center; font-size: 12px; }
                #page-today .item-trigger-btn { transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease, background-color .18s ease; }
                #page-today .item-trigger-btn:hover { transform: translateY(-2px); border-color: #A7F3D0 !important; box-shadow: 0 8px 18px rgba(16,185,129,0.08); }
                #page-today .item-trigger-btn:active { transform: translateY(-1px) scale(.99); background-color: #F8FFFC; }
                #page-today .today-notice-card { border-color: #D1FAE5; background: linear-gradient(180deg, #F8FFFC 0%, #FFFFFF 100%); }
                #page-today .today-notice-label { color:#047857; font-weight:900; margin-bottom:9px; display:flex; align-items:center; gap:6px; }
                #page-today .today-priority-row { display:grid; grid-template-columns:34px 1fr; gap:10px; align-items:center; padding:11px 12px; margin-bottom:10px; background:#ECFDF5; border:1px solid #A7F3D0; border-radius:12px; }
                #page-today .today-priority-icon { width:34px; height:34px; border-radius:10px; display:flex; align-items:center; justify-content:center; color:#FFFFFF; background:#10B981; font-size:18px; }
                #page-today .today-priority-kicker { display:block; color:#047857; font-size:10.5px; font-weight:900; line-height:1.2; margin-bottom:2px; }
                #page-today .today-priority-main { display:block; color:#00112c; font-size:14.5px; line-height:1.35; font-weight:900; }
                #page-today .today-note-list { padding-left:18px !important; margin:0 !important; }
                #page-today .step-action-list { display:flex; flex-direction:column; gap:5px; margin-top:2px; }
                #page-today .step-action-list span { position:relative; padding-left:13px; color:#475569; font-size:12px; line-height:1.45; font-weight:600; }
                #page-today .step-action-list span::before { content:''; position:absolute; left:0; top:.62em; width:5px; height:5px; border-radius:50%; background:#10B981; }

                /* カテゴリカード */
                .home-section-title { font-size: 14px; font-weight: 800; color: #1E293B; margin: 12px 0 12px 4px; }
                .hero-prep-card {
                    background: linear-gradient(135deg, #FFF5F5 0%, #FFEAEA 100%);
                    border: 2px solid #FEB2B2; border-radius: 18px; padding: 22px 20px;
                    margin-bottom: 24px; cursor: pointer; display: flex; flex-direction: column;
                    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.02); transition: all 0.2s ease; width: 100%; box-sizing: border-box;
                }
                .hero-prep-card:active { transform: scale(0.98); }
                .hero-tag-row { display: flex; align-items: center; justify-content: flex-start; margin-bottom: 14px; }
                .hero-badge { background-color: #E53E3E; color: white; font-size: 10px; font-weight: 900; padding: 4px 12px; border-radius: 8px; letter-spacing: 0.5px; }
                .hero-main-icon { color: #E53E3E; font-size: 24px; display: flex; align-items: center; }
                .hero-catch { font-size: 17px; font-weight: 800; color: #741B1B; line-height: 1.4; margin: 0; }
                .hero-clean-desc { font-size: 12.5px; color: #9B2C2C; font-weight: 600; line-height: 1.5; margin: 10px 0 16px 0; }
                .hero-cta-btn { background: #C53030; color: white; border: none; border-radius: 12px; padding: 9px 12px; font-size: 13.5px; font-weight: bold; text-align: center; width: 100%; box-shadow: 0 4px 10px rgba(197, 48, 48, 0.15); display: flex; align-items: center; justify-content: center; gap: 4px; box-sizing: border-box; }
                
                .category-card { display: flex; align-items: center; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 16px 14px; margin-bottom: 14px; cursor: pointer; box-shadow: 0 4px 12px rgba(0, 17, 44, 0.02); transition: all 0.15s ease; width: 100%; box-sizing: border-box; }
                .category-card:active { transform: scale(0.98); background-color: #F8FAFC; }
                .card-green { border-left: 6px solid #10B981 !important; } .card-purple { border-left: 6px solid #8B5CF6 !important; } .card-orange { border-left: 6px solid #F59E0B !important; } .card-red { border-left: 6px solid #EF4444 !important; }
                
                .card-icon-box { width: 40px; height: 40px; border-radius: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; margin-right: 14px; font-size: 20px; color: white; }
                .bg-green { background-color: #10B981; } .bg-purple { background-color: #8B5CF6; } .bg-orange { background-color: #F59E0B; } .bg-red { background-color: #EF4444; }
                
                .card-main-text { flex: 1; display: flex; flex-direction: column; gap: 7px; text-align: left; }
                .card-title, .manner-pop-title, .rule-display-title { font-size: 14px !important; font-weight: 800 !important; color: #1E293B !important; }
                .card-subtitle, .manner-pop-text, .rule-bullet-list, .accordion-content { font-size: 12.5px !important; color: #475569 !important; font-weight: 500 !important; line-height: 1.6 !important; }
                .card-chevron { color: #94A3B8; font-size: 14px; margin-left: 8px; display: flex; align-items: center; }

                .item-trigger-btn { display: flex !important; align-items: center; background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 14px 12px; margin-bottom: 12px; cursor: pointer; width: 100% !important; box-shadow: 0 4px 12px rgba(0,91,172,0.02); box-sizing: border-box !important; transition: all 0.1s; }
                .item-trigger-btn:active { background-color: #EDF2F7; }
                .item-icon-container { width: 34px; height: 34px; border-radius: 10px; margin-right: 12px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; font-size: 18px; }
                .item-text-node { flex: 1; display: flex; align-items: center; gap: 6px; text-align: left; }
                .item-title { font-size: 13.5px !important; font-weight: 800 !important; color: #1E293B !important; line-height: 1.3; }
                .item-arrow { font-size: 11px; color: #CBD5E1; transition: transform 0.15s; margin-left: auto; display: flex; align-items: center; }

                .simple-accordion { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.01); width: 100%; box-sizing: border-box; overflow: hidden; }
                .simple-accordion .accordion-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 14px; cursor: pointer; user-select: none; }
                .simple-accordion .accordion-header:active { background-color: #F8FAFC; }
                .simple-accordion .accordion-content { display: none; padding: 0 16px 16px 16px; font-size: 12.5px; color: #475569; line-height: 1.6; font-weight: 500; text-align: left; }
                .simple-accordion.open .accordion-content { display: block !important; }
                .simple-accordion .accordion-arrow { font-size: 12px; color: #94A3B8; transition: transform 0.2s; }
                .simple-accordion.open .accordion-arrow { transform: rotate(90deg); }

                /* シートビュー用写真設定 */
                .seat-map-wrapper { position:relative; width:100%; max-width:358px; aspect-ratio:3/4; height:auto; border:1px solid rgba(0,91,172,.24); border-radius:20px; margin:0 auto; overflow:hidden; background:#001F4D; box-shadow:0 14px 30px rgba(0,31,77,.14); isolation:isolate; }
                .seat-photo-main { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center; opacity:0; transition:opacity .25s ease; z-index:1; }
                .view-seat3 .seat-photo-seat3 { opacity:1; }
                .view-seat4 .seat-photo-seat4 { opacity:1; }
                .seat-photo-chip { position:absolute; left:12px; top:12px; z-index:15; display:inline-flex; align-items:center; gap:5px; background:rgba(0,31,77,.82); color:#FFFFFF; border:1px solid rgba(255,255,255,.28); border-radius:999px; padding:7px 11px; font-size:11px; font-weight:900; }
                
                .hotspot-btn { position:absolute; width:36px; height:36px; background:#FFFFFF; border:2px solid #005bac; border-radius:50%; cursor:pointer; z-index:30; display:flex; align-items:center; justify-content:center; font-size:13px; color:#005bac; box-shadow:0 4px 10px rgba(0,91,172,0.4); transform:translate(-50%, -50%); }
                .hotspot-btn.active { background:#005bac !important; color:#FFFFFF !important; }

                .seat-hotspot-info { display:none; width:100%; max-width:358px; margin:10px auto 0; box-sizing:border-box; text-align:left; background:#FFFFFF; border:1px solid #D8E3F0; border-radius:16px; padding:13px 14px; }
                .seat-hotspot-info.show { display:block; }
                .seat-hotspot-info-title { color:#003B72; font-size:14px; font-weight:900; margin-bottom:6px; }
                .seat-hotspot-info-desc { color:#334155; font-size:12.2px; line-height:1.6; margin:0; }

                .seat-toggle-bar { display: flex; background: #F1F5F9; border-radius: 10px; padding: 4px; gap: 4px; margin-bottom: 16px; }
                .seat-toggle-btn { flex: 1; border: none; background: transparent; padding: 10px; font-size: 13px; font-weight: 800; color: #64748B; border-radius: 8px; cursor: pointer; }
                .seat-toggle-btn.active { background: #FFFFFF; color: #005bac; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }

                .floating-top-btn { position: fixed !important; bottom: calc(20px + env(safe-area-inset-bottom, 0px)) !important; right: calc(20px + env(safe-area-inset-right, 0px)) !important; width: 50px !important; height: 50px !important; border-radius: 25px !important; background: #005bac !important; color: white !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important; cursor: pointer !important; z-index: 9999 !important; border: none !important; }
            </style>
        </head>
        <body>
            <div class="app-wrapper" id="js-app-wrapper">
                
                <div class="app-fixed-top">
                    <div class="app-header">
                        <div class="app-header-stars"></div>
                        <div class="app-header-highway"></div>
                        <div class="app-header-tagline">ナイトライナー</div>
                        <h1>ご利用ガイド</h1>
                        <p>快適な夜行バスの旅をサポートする 乗車前のご案内</p>
                    </div>
                </div>
                
                <div class="app-scroll-body" id="js-scroll-body">
                    
                    <!-- ホーム画面 -->
                    <div id="page-home" class="page-view active">
                        <div class="home-section-title">ご乗車前にご確認ください</div>
                        
                        <div class="hero-prep-card page-trigger" data-target="page-prep">
                            <div class="hero-tag-row"><span class="hero-badge">⚠️ 乗車前に必ず確認</span></div>
                            <h2 class="hero-catch">乗車前の準備</h2>
                            <p class="hero-clean-desc">荷物・持ち込みルールや、乗車前にご確認いただきたい内容をご案内します。</p>
                            <button class="hero-cta-btn">ご乗車前のご案内を見る <i class="ph-bold ph-caret-right"></i></button>
                        </div>

                        <div class="home-section-title" style="margin-top: 8px;">目的別ガイド</div>

                        <div class="category-card card-green page-trigger" data-target="page-today">
                            <div class="card-icon-box bg-green"><i class="ph-bold ph-signpost"></i></div>
                            <div class="card-main-text">
                                <span class="card-title">当日の流れ・乗車案内</span>
                                <p class="card-subtitle">乗車までの流れや、のりば・通過スケジュールを確認できます。</p>
                            </div>
                            <div class="card-chevron"><i class="ph-bold ph-caret-right"></i></div>
                        </div>

                        <div class="category-card card-purple page-trigger" data-target="page-recline">
                            <div class="card-icon-box bg-purple"><i class="ph-bold ph-armchair"></i></div>
                            <div class="card-main-text">
                                <span class="card-title">シートの使い方・設備</span>
                                <p class="card-subtitle">リクライニングや各設備の使い方をご案内します。</p>
                            </div>
                            <div class="card-chevron"><i class="ph-bold ph-caret-right"></i></div>
                        </div>

                        <div class="category-card card-orange page-trigger" data-target="page-manner">
                            <div class="card-icon-box bg-orange"><i class="ph-bold ph-bus"></i></div>
                            <div class="card-main-text">
                                <span class="card-title">車内のご利用案内</span>
                                <p class="card-subtitle">車内設備・マナー・アメニティをご案内します。</p>
                            </div>
                            <div class="card-chevron"><i class="ph-bold ph-caret-right"></i></div>
                        </div>
                    </div>

                    <!-- シート使い方ページ -->
                    <div id="page-recline" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ シートの使い方・設備</span>
                        </div>
                        
                        <div class="heading">シートについて</div>
                        <div class="seat-toggle-bar">
                            <button class="seat-toggle-btn active" id="js-btn-seat3">3列独立シート</button>
                            <button class="seat-toggle-btn" id="js-btn-seat4">4列シート</button>
                        </div>
                        
                        <div class="seat-map-wrapper view-seat3" id="seat-canvas-container">
                            <img class="seat-photo-main seat-photo-seat3" src="__SEAT3_PHOTO__" alt="3列独立シート">
                            <img class="seat-photo-main seat-photo-seat4" src="__SEAT4_PHOTO__" alt="4列シート">
                            <div class="seat-photo-chip" id="js-seat-photo-label">3列独立シート 設備ガイド</div>

                            <div class="hotspot-btn" id="pin-overhead" data-key="overhead" style="top: 20%; left: 50%;"><i class="ph-bold ph-lightbulb"></i></div>
                        </div>

                        <div class="seat-hotspot-info" id="js-seat-hotspot-info">
                            <div class="seat-hotspot-info-title" id="js-seat-info-title"></div>
                            <p class="seat-hotspot-info-desc" id="js-seat-info-desc"></p>
                        </div>
                    </div>

                </div>
                
                <button class="floating-top-btn" id="js-float-top">
                    <i class="ph-bold ph-caret-double-up"></i>
                    <span>TOP</span>
                </button>
            </div>

            <script>
                function initApp() {
                    document.querySelectorAll('.page-trigger').forEach(card => {
                        card.addEventListener('click', function() {
                            const targetPageId = this.getAttribute('data-target');
                            document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
                            const targetPage = document.getElementById(targetPageId);
                            if (targetPage) targetPage.classList.add('active');
                            window.scrollTo(0, 0);
                        });
                    });

                    document.querySelectorAll('.back-to-home-trigger').forEach(btn => {
                        btn.addEventListener('click', function() {
                            document.querySelectorAll('.page-view').forEach(p => p.classList.remove('active'));
                            document.getElementById('page-home').classList.add('active');
                            window.scrollTo(0, 0);
                        });
                    });

                    const canvasContainer = document.getElementById('seat-canvas-container');
                    const btnS3 = document.getElementById('js-btn-seat3');
                    const btnS4 = document.getElementById('js-btn-seat4');

                    if(btnS3 && btnS4 && canvasContainer) {
                        btnS3.addEventListener('click', function() {
                            btnS4.classList.remove('active'); btnS3.classList.add('active');
                            canvasContainer.className = "seat-map-wrapper view-seat3";
                        });
                        btnS4.addEventListener('click', function() {
                            btnS3.classList.remove('active'); btnS4.classList.add('active');
                            canvasContainer.className = "seat-map-wrapper view-seat4";
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
    st.components.v1.html(html, height=1400, scrolling=False)

if __name__ == "__main__":
    main()
