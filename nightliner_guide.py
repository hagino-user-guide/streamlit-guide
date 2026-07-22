import base64
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"


def image_data_uri(filename):
    path = ASSET_DIR / filename
    if not path.exists():
        # ファイルが見つからない場合にターミナル（黒い画面）に警告を出す
        print(f"⚠️ 画像ファイルが見つかりません: {path}")
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
    seat3_photo = image_data_uri("seat_3_left_window_original_web.jpg")
    seat4_photo = image_data_uri("seat_4_aisle_guide_web.jpg")
    overhead_photo = image_data_uri("seat_overhead_console_web.jpg")
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
    amenity_blanket_photo = image_data_uri("amenity_blanket_web.jpg")
    amenity_set_photo = image_data_uri("amenity_set_web.jpg")
    
    # 🎯 画面外枠（Streamlit標準のヘッダー・フッター等）を消去するCSS
    st.markdown("""
        <style>
        header, [data-testid="stHeader"], footer, #MainMenu, [data-testid="stSidebar"], [data-testid="stTopBar"], div[data-testid="stTextInput"] { 
            display: none !important; 
        }
        .block-container { padding: 0rem !important; max-width: 100% !important; margin: 0 !important; }
        [data-testid="stAppViewContainer"] { background-color: #E2E8F0 !important; }
        div[data-testid="stVerticalBlock"] { gap: 0rem !important; padding: 0 !important; margin: 0 !important; }
        
                /* ── 🆘 困ったとき：スマートフォン行動ガイド ── */

            
                /* ── 🆘 困ったとき：完成度を高める微調整 ── */
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
                /* バスシルエットは装飾過多に見えるため非表示 */
                .app-header-bus-silhouette {
                    display: none;
                }
                .app-header-tagline { position: relative; z-index: 2; display: inline-flex; align-items: center; width: fit-content; padding: 3px 9px 3px 10px; border: 1px solid rgba(255,255,255,0.22); border-radius: 999px; background: rgba(255,255,255,0.08); font-size: 12.5px; font-weight: 800; color: #FFFFFF; letter-spacing: 0.12em; margin-bottom: 6px; opacity: 0.94; line-height: 1; }
                .app-header h1 { position: relative; z-index: 2; font-size: 28px !important; font-weight: 850 !important; margin: 0 0 8px 0 !important; color: #FFFFFF !important; letter-spacing: 0.015em; line-height: 1 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.18); }
                .app-header p { position: relative; z-index: 2; font-size: 12.2px !important; color: #FFFFFF !important; margin: 0 !important; font-weight: 500 !important; opacity: 0.9; line-height: 1.42 !important; max-width: 320px; }
                
                /* ── 後続パーツのスタイル（変更なし） ── */
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

                /* 当日の流れ・のりばページ：目的別ガイドの緑に合わせて統一 */
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
                
                /* タイポグラフィ */
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

                /* アコーディオン制御 */
                .simple-accordion { background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.01); width: 100%; box-sizing: border-box; overflow: hidden; }
                .simple-accordion .accordion-header { display: flex; align-items: center; justify-content: space-between; padding: 16px 14px; cursor: pointer; user-select: none; }
                .simple-accordion .accordion-header:active { background-color: #F8FAFC; }
                .simple-accordion .accordion-content { display: none; padding: 0 16px 16px 16px; font-size: 12.5px; color: #475569; line-height: 1.6; font-weight: 500; text-align: left; }
                .simple-accordion.open .accordion-content { display: block !important; }
                .simple-accordion .accordion-arrow { font-size: 12px; color: #94A3B8; transition: transform 0.2s; }
                .simple-accordion.open .accordion-arrow { transform: rotate(90deg); }

                /* Help page */
                #page-help {
                    --help-blue: #005BAC;
                    --help-text: #1E293B;
                    --help-muted: #475569;
                    --help-border: #E2E8F0;
                    --help-red: #E53E3E;
                    --help-orange: #F59E0B;
                    --help-coral: #EF4444;
                    --help-green: #10B981;
                    width: 100%;
                    min-width: 0;
                    max-width: 100%;
                    box-sizing: border-box;
                    overflow-x: hidden;
                }
                #page-help *,
                #page-help *::before,
                #page-help *::after {
                    box-sizing: border-box;
                }
                #page-help .breadcrumb-current {
                    color: #C53030;
                }
                #page-help .heading {
                    color: var(--help-blue) !important;
                    border-left-color: var(--help-blue) !important;
                    margin-bottom: 12px !important;
                }
                #page-help .help-page-intro {
                    display: flex;
                    align-items: flex-start;
                    gap: 9px;
                    width: 100%;
                    min-width: 0;
                    margin: 2px 0 14px;
                    padding: 12px 13px;
                    border: 1px solid #D8E7F7;
                    border-left: 4px solid var(--help-blue);
                    border-radius: 14px;
                    background: #F8FBFF;
                    color: var(--help-muted);
                    font-size: 12px;
                    line-height: 1.62;
                    font-weight: 700;
                    box-shadow: 0 3px 10px rgba(0, 91, 172, 0.035);
                }
                #page-help .help-page-intro i {
                    flex: 0 0 auto;
                    margin-top: 1px;
                    color: var(--help-blue);
                    font-size: 18px;
                    line-height: 1;
                }
                #page-help .help-accordion-list {
                    display: flex;
                    flex-direction: column;
                    gap: 12px;
                    width: 100%;
                    min-width: 0;
                }
                #page-help .help-main-accordion {
                    width: 100%;
                    min-width: 0;
                    max-width: 100%;
                    margin: 0;
                    border: 1px solid var(--help-border);
                    border-radius: 16px;
                    background: #FFFFFF;
                    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
                    overflow: hidden;
                }
                #page-help .help-main-accordion.open {
                    border-color: #DDE7F1;
                    box-shadow: 0 6px 16px rgba(15, 23, 42, 0.045);
                }
                #page-help .help-main-accordion .accordion-header {
                    width: 100%;
                    min-width: 0;
                    min-height: 62px;
                    display: flex;
                    align-items: center;
                    justify-content: flex-start;
                    gap: 12px;
                    padding: 12px 13px;
                    background: #FFFFFF;
                    cursor: pointer;
                    user-select: none;
                    -webkit-tap-highlight-color: transparent;
                    transition: background-color .22s ease, box-shadow .22s ease;
                }
                #page-help .help-main-accordion .accordion-header:hover,
                #page-help .help-main-accordion .accordion-header:active {
                    background: #F8FAFC;
                }
                #page-help .help-main-accordion .accordion-header:focus,
                #page-help .help-main-accordion .accordion-header:focus-visible {
                    outline: none;
                    box-shadow: inset 0 0 0 2px rgba(0, 91, 172, .10);
                }
                #page-help .help-main-accordion.open .accordion-header {
                    background: #FFFFFF;
                    box-shadow: inset 0 -1px 0 #F1F5F9;
                }
                #page-help .help-main-icon {
                    width: 38px;
                    height: 38px;
                    flex: 0 0 38px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 12px;
                    border: 1px solid #D9E7F7;
                    background: #EFF6FF;
                    color: var(--help-blue);
                    font-size: 20px;
                    line-height: 1;
                }
                #page-help .help-main-icon i {
                    display: block;
                    line-height: 1;
                }
                #page-help .help-main-title {
                    flex: 1;
                    min-width: 0;
                    color: var(--help-text);
                    font-size: 13.8px;
                    line-height: 1.4;
                    font-weight: 900;
                    text-align: left;
                }
                #page-help .help-main-accordion .accordion-arrow {
                    flex: 0 0 auto;
                    margin-left: auto;
                    color: #CBD5E1;
                    font-size: 12px;
                    transition: transform .22s ease, color .22s ease;
                }
                #page-help .help-main-accordion.open .accordion-arrow {
                    transform: rotate(90deg);
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(1) .help-main-icon {
                    color: var(--help-red);
                    background: #FFF5F5;
                    border-color: #FED7D7;
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(2) .help-main-icon {
                    color: var(--help-orange);
                    background: #FFFBEB;
                    border-color: #FDE68A;
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(3) .help-main-icon {
                    color: var(--help-coral);
                    background: #FFF1F2;
                    border-color: #FECDD3;
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(4) .help-main-icon {
                    color: var(--help-blue);
                    background: #EFF6FF;
                    border-color: #BFDBFE;
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(5) .help-main-icon {
                    color: var(--help-green);
                    background: #ECFDF5;
                    border-color: #A7F3D0;
                }
                #page-help .help-accordion-list .help-main-accordion:nth-child(1).open .accordion-arrow { color: var(--help-red); }
                #page-help .help-accordion-list .help-main-accordion:nth-child(2).open .accordion-arrow { color: var(--help-orange); }
                #page-help .help-accordion-list .help-main-accordion:nth-child(3).open .accordion-arrow { color: var(--help-coral); }
                #page-help .help-accordion-list .help-main-accordion:nth-child(4).open .accordion-arrow { color: var(--help-blue); }
                #page-help .help-accordion-list .help-main-accordion:nth-child(5).open .accordion-arrow { color: var(--help-green); }
                #page-help .help-main-accordion .accordion-content {
                    display: grid;
                    grid-template-rows: 0fr;
                    width: 100%;
                    min-width: 0;
                    max-width: 100%;
                    padding: 0 14px;
                    opacity: 0;
                    overflow: hidden;
                    text-align: left !important;
                    transition: grid-template-rows .24s ease, opacity .2s ease, padding .24s ease;
                }
                #page-help .help-main-accordion.open .accordion-content {
                    display: grid !important;
                    grid-template-rows: 1fr;
                    padding: 13px 14px 15px;
                    opacity: 1;
                }
                #page-help .help-accordion-inner {
                    min-height: 0;
                    width: 100%;
                    min-width: 0;
                    overflow: hidden;
                }
                #page-help .help-copy {
                    margin: 0 0 9px;
                    color: var(--help-muted);
                    font-size: 12px;
                    line-height: 1.72;
                    font-weight: 600;
                    overflow-wrap: anywhere;
                }
                #page-help .help-copy:last-child {
                    margin-bottom: 0;
                }
                #page-help .help-subheading {
                    display: flex;
                    align-items: center;
                    gap: 7px;
                    margin: 0 0 9px;
                    color: var(--help-text);
                    font-size: 13px;
                    line-height: 1.4;
                    font-weight: 900;
                }
                #page-help .help-subheading i {
                    width: 23px;
                    height: 23px;
                    flex: 0 0 23px;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    color: var(--help-blue);
                    font-size: 17px;
                }
                #page-help .help-emergency-contact .help-subheading {
                    color: #991B1B;
                }
                #page-help .help-emergency-contact .help-subheading i {
                    color: #C53030;
                }
                #page-help .help-divider {
                    height: 1px;
                    margin: 14px 0;
                    background: #EEF1F4;
                }
                #page-help .help-emergency-row {
                    display: grid;
                    grid-template-columns: 46px minmax(0, 1fr);
                    gap: 11px;
                    align-items: flex-start;
                }
                #page-help .help-emergency-icon {
                    width: 46px;
                    height: 46px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    color: var(--help-blue);
                    background: #EFF6FF;
                    border: 1px solid #BFDBFE;
                    border-radius: 13px;
                }
                #page-help .help-emergency-icon svg {
                    width: 30px;
                    height: 30px;
                    fill: none;
                    stroke: currentColor;
                    stroke-width: 2;
                    stroke-linecap: round;
                    stroke-linejoin: round;
                }
                #page-help .help-contact-company {
                    margin: 0 0 4px;
                    color: #64748B;
                    font-size: 11.7px;
                    line-height: 1.5;
                    font-weight: 650;
                }
                #page-help .help-phone-number {
                    display: block;
                    margin: 0 0 8px;
                    color: #1E293B;
                    text-decoration: none;
                    font-size: 20px;
                    line-height: 1.25;
                    font-weight: 900;
                    letter-spacing: .025em;
                    pointer-events: none;
                }
                #page-help .help-emergency-number {
                    color: #1E293B;
                }
                #page-help .help-contact-meta {
                    margin: 0 0 8px;
                    color: var(--help-muted);
                    font-size: 11.8px;
                    line-height: 1.6;
                    font-weight: 600;
                }
                #page-help .help-notice-box {
                    width: 100%;
                    margin: 10px 0;
                    padding: 10px 11px;
                    border: 1px solid #F2D38B;
                    border-left: 4px solid #F59E0B;
                    border-radius: 11px;
                    background: #FFF8E8;
                    color: #6B4708;
                    font-size: 11.6px;
                    line-height: 1.65;
                    font-weight: 700;
                    box-shadow: none;
                }
                #page-help .help-contact-notice {
                    margin-top: 8px;
                    margin-bottom: 0;
                }
                #page-help .help-notice-box p {
                    margin: 0 0 4px;
                }
                #page-help .help-notice-box p:last-child {
                    margin-bottom: 0;
                }
                #page-help .help-notice-title {
                    display: flex;
                    align-items: center;
                    gap: 5px;
                    margin: 0 0 6px;
                    color: #92400E;
                    font-size: 11.8px;
                    line-height: 1.45;
                    font-weight: 900;
                }
                #page-help .help-notice-title i {
                    font-size: 14px;
                }
                #page-help .help-note-list {
                    margin: 0;
                    padding-left: 18px;
                    color: #6B4708;
                    font-size: 11.6px;
                    line-height: 1.66;
                    font-weight: 700;
                }
                #page-help .help-note-list li {
                    margin-bottom: 3px;
                }
                #page-help .help-note-list li:last-child {
                    margin-bottom: 0;
                }
                #page-help .help-emergency-contact .help-notice-box {
                    background: #FFF1F2;
                    border-color: #FECDD3;
                    border-left-color: #EF4444;
                    color: #7F1D1D;
                }
                #page-help .help-emergency-contact .help-notice-title {
                    color: #B91C1C;
                }
                #page-help .help-emergency-contact .help-note-list {
                    color: #7F1D1D;
                }
                #page-help .help-action-btn {
                    width: 100%;
                    min-height: 50px;
                    margin-top: 10px;
                    padding: 12px 13px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    gap: 8px;
                    border-radius: 12px;
                    text-decoration: none;
                    font-size: 12.8px;
                    line-height: 1.3;
                    font-weight: 900;
                    letter-spacing: .01em;
                    -webkit-tap-highlight-color: transparent;
                    transition: transform .16s ease, background-color .2s ease, box-shadow .2s ease;
                }
                #page-help .help-action-btn:active {
                    transform: scale(.98);
                }
                #page-help .help-action-btn > i:first-child {
                    flex: 0 0 auto;
                    font-size: 18px;
                }
                #page-help .help-action-btn > span {
                    min-width: 0;
                    overflow-wrap: anywhere;
                }
                #page-help .help-action-btn > i:last-child {
                    margin-left: auto;
                    font-size: 13px;
                    opacity: .78;
                }
                #page-help .help-web-btn,
                #page-help .help-phone-btn {
                    color: var(--help-blue);
                    background: #FFFFFF;
                    border: 1px solid #9ECBF0;
                    box-shadow: 0 3px 8px rgba(0, 91, 172, .055);
                }
                #page-help .help-web-btn:hover,
                #page-help .help-phone-btn:hover {
                    background: #F4F9FF;
                }
                #page-help .help-emergency-btn {
                    color: #FFFFFF;
                    background: #C93D3D;
                    border: 1px solid #B83232;
                    box-shadow: 0 4px 10px rgba(197, 48, 48, .14);
                }
                #page-help .help-emergency-btn:hover {
                    background: #B83232;
                }
                #page-help .help-emergency-row strong {
                    color: #B83232;
                    font-weight: 900;
                }
                @media (max-width: 380px) {
                    #page-help .help-main-accordion .accordion-header {
                        min-height: 58px;
                        padding: 11px;
                        gap: 10px;
                    }
                    #page-help .help-main-icon {
                        width: 34px;
                        height: 34px;
                        flex-basis: 34px;
                        font-size: 18px;
                    }
                    #page-help .help-main-title {
                        font-size: 13px;
                    }
                    #page-help .help-main-accordion.open .accordion-content {
                        padding: 11px 12px 13px;
                    }
                    #page-help .help-subheading {
                        font-size: 12.6px;
                    }
                    #page-help .help-phone-number {
                        font-size: 18.5px;
                    }
                    #page-help .help-action-btn {
                        min-height: 48px;
                        padding: 11px 12px;
                        font-size: 12.4px;
                    }
                }

                /* 横スクロールステップUI */
                .step-outer-container-js { position: relative; width: 100%; display: flex; align-items: center; box-sizing: border-box; }
                .step-scroll-wrapper { display: flex; gap: 16px; overflow-x: auto; padding: 8px 4px 20px 4px; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; position: relative; width: 100%; box-sizing: border-box; }
                .step-scroll-wrapper::-webkit-scrollbar { display: none; }
                .step-premium-card { flex: 0 0 210px; background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 20px 16px; box-sizing: border-box; scroll-snap-align: start; position: relative; z-index: 2; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; gap: 8px; }
                .step-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
                .step-badge-node { font-size: 10px; font-weight: 900; color: #005bac; background: #EFF6FF; padding: 3px 10px; border-radius: 20px; letter-spacing: 0.5px; display: inline-block; }
                .step-icon-inline { font-size: 20px; color: #1E293B; display: flex; align-items: center; margin-top: 2px; }
                .step-premium-card .step-card-title { font-size: 14px !important; font-weight: 800 !important; color: #1E293B !important; line-height: 1.3; text-align: left; margin: 4px 0 2px 0; }
                .step-card-desc { font-size: 12.5px !important; color: #475569 !important; font-weight: 500 !important; line-height: 1.5 !important; margin: 0; }
                .step-info-box-js { margin-top: auto; background-color: #F8FAFC; border-radius: 10px; padding: 10px 12px; border: 1px solid #EFF6FF; text-align: left; }
                .step-info-box-line { font-size: 11px !important; color: #64748B !important; font-weight: 500 !important; line-height: 1.4; margin: 0 0 4px 0; display: flex; align-items: flex-start; gap: 4px; }
                .step-info-box-line:last-child { margin-bottom: 0; }
                .step-info-box-line strong { color: #005bac; white-space: nowrap; font-weight: 800; }

                .step-nav-btn-js { position: absolute; top: calc(50% - 10px); width: 36px; height: 36px; border-radius: 50%; background: #FFFFFF; border: 1px solid #E2E8F0; color: #005bac; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 10px rgba(0,0,0,0.06); cursor: pointer; z-index: 20; transition: all 0.15s; }
                .step-nav-btn-js:active { background-color: #F8FAFC; transform: scale(0.95); }
                .step-nav-prev { left: -8px; } .step-nav-next { right: -8px; }

                /* マナーポップカード */
                .manner-pop-card {
                    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px;
                    padding: 18px; margin-bottom: 14px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.02); text-align: left;
                }
                .manner-pop-title {
                    font-size: 14px !important; font-weight: 800 !important; color: #005bac !important;
                    display: flex; align-items: center; gap: 8px; margin-bottom: 10px;
                }
                .manner-pop-text { font-size: 12.5px !important; color: #475569 !important; line-height: 1.6; margin: 0; font-weight: 500; }

                /* 枠線付き固定カード */
                .rule-display-card {
                    background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px;
                    padding: 18px; margin-bottom: 14px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); text-align: left;
                }
                .rule-display-title { font-size: 14px !important; font-weight: 800 !important; color: #1E293B !important; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; }
                .rule-bullet-list { margin: 0; padding-left: 20px; font-size: 12.5px !important; color: #475569 !important; line-height: 1.7; font-weight: 500; }
                .rule-bullet-list li { margin-bottom: 6px; }
                .rule-bullet-list li:last-child { margin-bottom: 0; }

                /* 荷物制限エリア */
                .ud-status-box { border-radius: 14px; padding: 16px; margin-bottom: 16px; box-sizing: border-box; width: 100%; text-align: left; }
                .ud-box-danger { background: #FFF5F5; border: 2px solid #EF4444; }
                .ud-sign-header { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; font-size: 14px; font-weight: 900; color: #DC2626; }
                .ud-sign-header-icon { font-size: 16px; border-radius: 6px; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; color: white; background-color: #EF4444; }
                .ud-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
                .ud-item { background: #FFFFFF; border-radius: 10px; padding: 12px 2px; text-align: center; border: 1px solid #FCA5A5; display: flex; flex-direction: column; align-items: center; gap: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); }
                .ud-icon-large { font-size: 30px; color: #EF4444; display: flex; align-items: center; justify-content: center; height: 34px; width: 100%; }
                .ud-item-label { display: flex; align-items: center; justify-content: center; width: 100%; }
                .ud-main-lbl { font-size: 10px; font-weight: 900; color: #1E293B; line-height: 1.2; letter-spacing: -0.2px; }

                .prep-subheading { font-size: 12.5px; font-weight: 900; color: #1E293B; margin: 0 0 10px 2px; line-height: 1.4; }
                .luggage-diagram-box { background: #FFFFFF; border: 1px solid #D8E3F0; border-radius: 18px; padding: 14px; margin-bottom: 14px; box-sizing: border-box; box-shadow: 0 6px 18px rgba(0,91,172,0.04); }
                .luggage-size-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 15px; padding: 12px 12px 14px; box-sizing: border-box; }
                .luggage-size-visual { position: relative; height: 220px; background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; overflow: hidden; }
                .luggage-size-svg { width: 100%; height: 100%; display: block; }
                .luggage-main-limit { text-align: center; color: #001F4D; font-size: 12px; font-weight: 900; line-height: 1.45; margin: 10px 0 0; letter-spacing: 0.02em; }
                .luggage-main-limit strong { display: block; color: #005bac; font-size: 17px; margin-top: 2px; letter-spacing: 0; }
                .luggage-limit-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 10px; }
                .luggage-limit-chip { background: #FFFFFF; border: 1px solid #D8E3F0; border-radius: 12px; padding: 8px 4px; text-align: center; box-shadow: 0 3px 8px rgba(0,91,172,0.03); }
                .luggage-limit-chip strong { display: block; color: #005bac; font-size: 14px; font-weight: 900; line-height: 1.1; }
                .luggage-limit-chip span { display: block; color: #64748B; font-size: 10px; font-weight: 800; margin-top: 3px; }
                .luggage-method-box { margin-top: 10px; background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 14px; padding: 10px 12px; text-align: left; }
                .luggage-method-title { font-size: 12.5px; font-weight: 900; color: #005bac; margin: 0 0 6px 0; }
                .luggage-method-text { font-size: 12px; color: #1E293B; font-weight: 700; line-height: 1.48; margin: 0 0 6px 0; }
                .luggage-method-text:last-child { margin-bottom: 0; }

                .prohibit-group-box { border-radius: 14px; padding: 14px; margin-bottom: 14px; box-sizing: border-box; width: 100%; text-align: left; border: 2px solid #E2E8F0; }
                .prohibit-group-title { font-size: 13px; font-weight: 900; margin: 0 0 10px 0; display: flex; align-items: center; gap: 6px; }
                .prohibit-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 7px; }
                .prohibit-card-node { background: #FFFFFF; border-radius: 10px; padding: 8px 4px; min-height: 64px; border: 1px solid #CBD5E1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); box-sizing: border-box; text-align: center; min-width: 0; }
                .prohibit-card-node i { font-size: 20px; flex-shrink: 0; color: #EF4444; }
                .prohibit-card-lbl { font-size: 10.5px; font-weight: 800; color: #1E293B; line-height: 1.25; }
                .prohibit-guidance-box { margin-top: 10px; padding: 9px 10px; border-radius: 10px; border: 1px solid #FECACA; background: #FFFFFF; }
                .prohibit-guidance-title { display: flex; align-items: center; gap: 5px; margin: 0 0 5px 0; color: #9B2C2C; font-size: 11px; font-weight: 900; }
                .prohibit-guidance-title i { font-size: 15px; }
                .prohibit-guidance-list { margin: 0; padding-left: 16px; color: #475569; font-size: 10.5px; font-weight: 500; line-height: 1.55; }
                .prohibit-guidance-list li { margin: 1px 0; }

                .bus-select-box { width: 100%; height: 44px; border: 2px solid #E2E8F0; border-radius: 8px; padding: 0 12px; font-size: 13px; color: #1E293B; outline: none; background-color: #FFFFFF; margin-bottom: 12px; font-weight: 700; width: 100%; box-sizing: border-box; }
                /* アメニティ：スマホ向け2列グリッド＋共通詳細カード */
                .amenity-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; width:100%; box-sizing:border-box; margin-bottom:12px; }
                .amenity-select-card { position:relative; width:100%; min-width:0; min-height:126px; padding:14px 10px 12px; border:1px solid #D8E3F0; border-radius:15px; background:linear-gradient(180deg,#FFFFFF 0%,#F8FBFF 100%); cursor:pointer; box-sizing:border-box; box-shadow:0 5px 14px rgba(0,31,77,.055); text-align:center; -webkit-tap-highlight-color:transparent; touch-action:manipulation; transition:transform .18s ease,border-color .2s ease,box-shadow .2s ease,background .2s ease; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; }
                .amenity-select-card:hover { transform:translateY(-3px); border-color:#B8D8F1; box-shadow:0 10px 22px rgba(0,31,77,.1); }
                .amenity-select-card:active { transform:translateY(-1px) scale(.975); }
                .amenity-select-card:focus-visible { outline:3px solid rgba(93,182,255,.42); outline-offset:2px; }
                .amenity-select-card.is-active { background:linear-gradient(180deg,#F4FAFF 0%,#EAF5FF 100%); border-color:#5DA0D7; box-shadow:0 9px 20px rgba(0,91,172,.12),0 0 0 3px rgba(93,182,255,.09); transform:translateY(-2px); }
                .amenity-line-icon-wrap { width:58px; height:58px; border-radius:17px; display:flex; align-items:center; justify-content:center; background:linear-gradient(145deg,#F4F9FF 0%,#E7F2FC 100%); border:1px solid #CFE3F5; color:#005BAC; box-shadow:inset 0 1px 0 rgba(255,255,255,.9),0 5px 12px rgba(0,91,172,.06); transition:transform .2s ease,background .2s ease,border-color .2s ease; }
                .amenity-select-card:hover .amenity-line-icon-wrap,.amenity-select-card.is-active .amenity-line-icon-wrap { transform:translateY(-1px); background:linear-gradient(145deg,#FFFFFF 0%,#DDEFFF 100%); border-color:#91C4EB; }
                .amenity-line-icon { width:36px; height:36px; display:block; overflow:visible; }
                .amenity-line-icon * { fill:none; stroke:currentColor; stroke-width:2.15; stroke-linecap:round; stroke-linejoin:round; vector-effect:non-scaling-stroke; }
                .amenity-card-name { display:block; color:#17324F; font-size:12px; line-height:1.35; font-weight:900; overflow-wrap:anywhere; }
                .amenity-detail-shell { display:grid; grid-template-rows:0fr; opacity:0; overflow:hidden; margin:0; transition:grid-template-rows .38s cubic-bezier(.2,.72,.2,1),opacity .22s ease,margin .38s ease; }
                .amenity-detail-shell.is-open { grid-template-rows:1fr; opacity:1; margin:2px 0 14px; }
                .amenity-detail-shell-inner { min-height:0; overflow:hidden; }
                .amenity-detail-card { background:linear-gradient(180deg,#FFFFFF 0%,#F7FBFF 100%); border:1px solid #BFDDF4; border-radius:15px; padding:15px; box-shadow:0 5px 14px rgba(0,91,172,.05); text-align:left; }
                .amenity-detail-header { display:flex; align-items:center; gap:9px; margin-bottom:9px; }
                .amenity-detail-icon { width:32px; height:32px; border-radius:10px; display:flex; align-items:center; justify-content:center; background:#EAF4FF; border:1px solid #CFE5F7; color:#005BAC; font-size:17px; flex-shrink:0; }
                .amenity-detail-title { color:#005BAC; font-size:13.5px; line-height:1.35; font-weight:900; }
                .amenity-detail-text { margin:0; color:#334155; font-size:12px; line-height:1.7; font-weight:600; }
                .amenity-detail-highlight { display:block; margin-top:11px; padding:10px 11px; background:#FFF9E8; border:1px solid #F3D98B; border-left:4px solid #E5B93E; border-radius:10px; color:#5A4A1E; font-size:11.5px; line-height:1.6; font-weight:750; }
                @media (max-width:380px) { .amenity-grid{gap:9px}.amenity-select-card{min-height:118px;padding:12px 8px 11px}.amenity-line-icon-wrap{width:54px;height:54px}.amenity-line-icon{width:33px;height:33px}.amenity-card-name{font-size:11.3px}.amenity-detail-card{padding:13px}.amenity-detail-text{font-size:11.5px} }

                /* ── 🚍 高速バスのリアルな車内空間 ── */
                .seat-toggle-bar { display: flex; background: #F1F5F9; border-radius: 10px; padding: 4px; gap: 4px; margin-bottom: 16px; }
                .seat-toggle-btn { flex: 1; border: none; background: transparent; padding: 10px; font-size: 13px; font-weight: 800; color: #64748B; border-radius: 8px; cursor: pointer; }
                .seat-toggle-btn.active { background: #FFFFFF; color: #005bac; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
                
                .seat-map-wrapper { 
                    position: relative; 
                    width: 340px; 
                    height: 320px; 
                    border: 3px solid #001F4D; 
                    border-radius: 20px; 
                    margin: 0 auto; 
                    overflow: hidden; 
                    background: linear-gradient(135deg, #050b14 0%, #0f1c30 100%);
                    box-shadow: 0 12px 28px rgba(0,17,44,0.25);
                    perspective: 800px;
                }
                
                .bus-floor {
                    position: absolute; bottom: 0; left: 0; width: 100%; height: 110px;
                    background: linear-gradient(180deg, #0d1321 0%, #02050b 100%);
                    z-index: 2; transform: rotateX(20deg); transform-origin: bottom;
                }
                .bus-aisle {
                    position: absolute; bottom: 0; left: 0; width: 120px; height: 110px;
                    background: linear-gradient(90deg, #182238 0%, #24324f 100%);
                    border-right: 3px solid #3b82f6; z-index: 3;
                    transform: rotateX(20deg) skewX(-35deg); transform-origin: bottom left;
                    box-shadow: inset -10px 0 20px rgba(0,0,0,0.5);
                }
                .bus-wall-side {
                    position: absolute; top: 0; right: 0; width: 140px; height: 100%;
                    background: linear-gradient(90deg, #090d16 0%, #151f32 100%);
                    z-index: 1; transform: rotateY(-30deg); transform-origin: right;
                    transition: right 0.3s ease;
                }
                .bus-window-real {
                    position: absolute; top: 50px; right: 15px; width: 110px; height: 140px;
                    background: linear-gradient(180deg, #01040a 0%, #0b1120 100%);
                    border: 4px solid #1e293b; border-radius: 16px;
                    transform: rotateY(-10deg);
                }
                .bus-curtain-real {
                    position: absolute; top: 40px; right: 115px; width: 35px; height: 180px;
                    background: linear-gradient(90deg, #1d4ed8 0%, #101f42 50%, #1e40af 100%);
                    border-radius: 4px; z-index: 3; box-shadow: 6px 8px 16px rgba(0,0,0,0.7);
                    transform: rotate(1deg);
                }
                .bus-overhead-console-real {
                    position: absolute; top: 0; left: 0; width: 120%; height: 60px;
                    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
                    border-bottom: 5px solid #005bac; z-index: 5;
                    box-shadow: 0 6px 20px rgba(0,0,0,0.5);
                    transform: rotateX(-15deg) rotateZ(-3deg)  ; transform-origin: top left;
                }
                .console-panel-unit {
                    position: absolute; bottom: 8px; left: 80px; width: 120px; height: 22px;
                    background: #1e293b; border-radius: 6px; border: 1.5px solid #475569;
                }
                .bus-privacy-partition-real {
                    position: absolute; top: 0; left: 0; width: 45px; height: 100%;
                    background: repeating-linear-gradient(90deg, #2d3748, #2d3748 6px, #1a202c 7px, #4a5568 12px);
                    z-index: 6; border-right: 3px solid #005bac; box-shadow: 8px 0 16px rgba(0,0,0,0.7);
                    display: none;
                }

                .real-bus-seat-container {
                    position: absolute; z-index: 4;
                    transform: rotateX(12deg) rotateY(-28deg) rotateZ(3deg);
                    transform-style: preserve-3d;
                    transition: all 0.35s ease-in-out;
                    pointer-events: none;
                }
                .real-seat-head {
                    width: 90px; height: 48px;
                    background: linear-gradient(180deg, #2563eb 0%, #005bac 60%, #1d4ed8 100%);
                    border-radius: 14px 14px 8px 8px; border: 2px solid #ffffff;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.4); margin: 0 auto;
                }
                .real-seat-back {
                    width: 110px; height: 132px;
                    background: linear-gradient(135deg, #334155 0%, #1e293b 60%, #0f172a 100%);
                    border-radius: 18px 18px 4px 4px; margin-top: -2px;
                    border: 1.5px solid #475569; position: relative;
                    box-shadow: inset 0 8px 12px rgba(255,255,255,0.15), 6px 10px 20px rgba(0,0,0,0.5);
                }
                .real-seat-back::before {
                    content: ''; position: absolute; top: 10px; left: 12px; width: 82px; height: 108px;
                    border: 1.5px dashed rgba(255,255,255,0.12); border-radius: 8px;
                }
                .real-seat-arm-l {
                    position: absolute; top: 115px; left: -14px; width: 22px; height: 68px;
                    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
                    border-radius: 6px; border: 1px solid #475569; box-shadow: -4px 4px 8px rgba(0,0,0,0.4);
                }
                .real-seat-arm-r {
                    position: absolute; top: 115px; right: -14px; width: 20px; height: 68px;
                    background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
                    border-radius: 6px; border: 1px solid #475569; box-shadow: 3px 3px 6px rgba(0,0,0,0.4);
                }
                .real-seat-cushion-base {
                    width: 114px; height: 42px;
                    background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
                    border-radius: 4px 4px 14px 14px; margin-top: -2px; margin-left: -2px;
                    border: 1px solid #334155; box-shadow: 0 7px 14px rgba(0,0,0,0.6);
                    position: relative;
                }
                .real-seat-lever-hardware {
                    position: absolute; bottom: 8px; left: -10px; width: 14px; height: 18px;
                    background: linear-gradient(135deg, #64748b 0%, #1e293b 100%);
                    border-radius: 3px; border: 1px solid #475569; box-shadow: -1px 2px 4px rgba(0,0,0,0.5);
                    z-index: 5;
                }
                .real-seat-legrest-panel {
                    width: 86px; height: 46px;
                    background: linear-gradient(180deg, #1e293b 0%, #090d16 100%);
                    border-radius: 4px 4px 10px 10px; margin: 3px auto 0 auto;
                    border: 1.5px solid #2d3748; box-shadow: 0 4px 7px rgba(0,0,0,0.5);
                }
                .real-seat-footrest-pedal {
                    width: 66px; height: 14px;
                    background: linear-gradient(180deg, #475569 0%, #1e293b 100%);
                    border-radius: 2px; margin: 16px auto 0 auto;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.6); border-bottom: 2px solid #000;
                }
                .real-front-pocket-holder {
                    position: absolute; top: 140px; left: 185px; width: 34px; height: 42px;
                    background: rgba(30,41,59,0.8); border: 1.5px solid #005bac; border-radius: 6px;
                    box-shadow: 0 4px 8px rgba(0,0,0,0.4); z-index: 2;
                    transition: all 0.35s ease-in-out;
                }
                .real-front-pocket-holder::after {
                    content: ''; position: absolute; top: 5px; left: 5px; right: 5px; bottom: 5px;
                    border: 1px dashed rgba(255,255,255,0.25); border-radius: 4px;
                }

                .seat-photo-placeholder { position: absolute; bottom: 12px; left: 0; width: 100%; text-align: center; color: rgba(255,255,255,0.35); font-size: 10px; font-weight: bold; pointer-events: none; z-index: 2; text-shadow: 0 1px 2px rgba(0,0,0,0.6); }
                
                .view-seat3 .real-bus-seat-container { top: 65px; left: 80px; transform: rotateX(12deg) rotateY(-28deg) rotateZ(3deg); }
                .view-seat3 .real-front-pocket-holder { top: 145px; left: 175px; }
                .view-seat4 .real-bus-seat-container { top: 75px; left: 45px; transform: rotateX(12deg) rotateY(-20deg) rotateZ(1deg); }
                .view-seat4 .real-front-pocket-holder { top: 155px; left: 145px; }

                /* ── 🎯 ホットスポットピン設定 ── */
                .hotspot-btn { 
                    position: absolute; width: 28px; height: 28px; background: #FFFFFF; 
                    border: 2px solid #005bac; border-radius: 50%; 
                    cursor: pointer; z-index: 10; display: flex; align-items: center; 
                    justify-content: center; font-size: 13px;
                    box-shadow: 0 4px 10px rgba(0,91,172,0.4);
                    transition: top 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), left 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), transform 0.2s, background 0.2s;
                }
                .hotspot-btn::before {
                    content: ''; position: absolute; width: 100%; height: 100%; 
                    border: 2px solid #3B82F6; border-radius: 50%;
                    animation: hotspotPulse 2s infinite; pointer-events: none; opacity: 0;
                }
                .hotspot-btn.active {
                    background: #005bac !important; border-color: #3b82f6 !important;
                    box-shadow: 0 0 16px rgba(59,130,246,0.95) !important; transform: scale(1.15);
                }
                @keyframes hotspotPulse {
                    0% { transform: scale(1); opacity: 0.8; }
                    100% { transform: scale(2.2); opacity: 0; }
                }

                /* ── 🎯 吹き出しUI ── */
                .interactive-tooltip {
                    display: none; position: absolute; width: 210px; height: 76px; box-sizing: border-box; background: #001F4D; color: #FFFFFF; border-radius: 12px; padding: 10px 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.55); z-index: 100; border: 1px solid rgba(255,255,255,0.2); opacity: 0; transform: translateY(4px); transition: opacity 0.2s ease-out, transform 0.2s ease-out; pointer-events: none;
                }
                .interactive-tooltip.show { display: block; opacity: 1; transform: translateY(0); pointer-events: auto; }
                .tooltip-title { font-size: 12px; font-weight: 800; color: #93C5FD; margin-bottom: 3px; display: flex; align-items: center; gap: 4px; }
                .tooltip-desc { font-size: 11px; color: #F8FAFC; line-height: 1.4; margin: 0; font-weight: 500; text-align: left; }
                
                /* ── 🎯 リーダー線 ── */
                .tooltip-leader-line { display: none; position: absolute; width: 0; border-left: 1.5px dashed #93C5FD; z-index: 90; pointer-events: none; }
                .tooltip-leader-line.show { display: block; }

                .info-card { background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 12px; padding: 16px; margin-bottom: 12px; text-align: left; }
                .info-text { font-size: 12px; color: #475569; font-weight: 500; line-height: 1.5; margin: 0; }
                .acc-header-left { display: flex; align-items: center; gap: 8px; font-size: 13.5px; font-weight: 800; color: #1E293B; text-align: left; }

                /* モーダルポップアップ設定 */
                .modal-mask {
                    position: absolute !important; top: 0; left: 0 !important;
                    width: 100% !important; height: 100vh;
                    background: rgba(15,23,42,0.6) !important;
                    display: none; align-items: center; justify-content: center;
                    padding: 16px; box-sizing: border-box; z-index: 999999 !important;
                }
                .modal-mask.show { display: flex !important; }
                .modal-box { width: 100%; max-width: 390px; background: #FFFFFF; border-radius: 20px; padding: 22px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); display: flex; flex-direction: column; max-height: 88vh; box-sizing: border-box; }
                .modal-top { font-size: 15px; font-weight: 800; color: #005bac; margin-bottom: 12px; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
                .modal-close-icon { pointer-events: auto !important; cursor: pointer; color: #64748B; font-size: 20px; }
                .modal-scroll { overflow-y: auto; padding-right: 2px; }

                /* タイムラインCSS */
                .image-timeline-container { position: relative; padding-left: 32px; margin: 16px 0 8px 4px; text-align: left; }
                .image-timeline-container::before { content: ''; position: absolute; left: 7px; top: 8px; bottom: 8px; width: 2px; background-color: #93C5FD; z-index: 1; }
                .image-timeline-node { position: relative; margin-bottom: 24px; }
                .image-timeline-node:last-child { margin-bottom: 0; }
                .image-timeline-node::before { content: ''; position: absolute; border-radius: 50%; box-sizing: border-box; z-index: 2; }
                .node-blue::before { background-color: #FFFFFF; border: 3px solid #005bac; width: 16px; height: 16px; left: -31px; top: 2px; }
                .node-red::before { background-color: #FF4D4D; width: 16px; height: 16px; left: -31px; top: 2px; border: none; }
                .node-header { display: flex; align-items: center; gap: 12px; margin-bottom: 4px; }
                .node-event-icon { width: 28px; height: 28px; border-radius: 9px; border: 1px solid #BFDBFE; background: #EFF6FF; color: #2563EB; display: inline-flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0; }
                .node-red .node-event-icon { border-color: #FECACA; background: #FEF2F2; color: #EF4444; }
                .node-time { font-size: 14px; font-weight: 900; color: #00112c; }
                .node-title { font-size: 14px; font-weight: 900; color: #00112c; }
                .node-desc { font-size: 12.5px; color: #475569; font-weight: 500; line-height: 1.5; margin: 0; }

                .station-menu-list { display: flex; flex-direction: column; gap: 8px; width: 100%; box-sizing: border-box; }
                .station-menu-group-title { width: fit-content; font-size: 12.5px; font-weight: 900; margin: 14px 0 7px 2px; text-align: left; padding: 4px 10px; border-radius: 999px; display: inline-flex; align-items: center; gap: 5px; }
                .station-menu-group-title.group-kanto { color: #047857; background: #ECFDF5; border: 1px solid #A7F3D0; }
                .station-menu-group-title.group-kansai { color: #1D4ED8; background: #EFF6FF; border: 1px solid #BFDBFE; }
                .station-menu-btn { background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 12px 12px; font-size: 13.5px; font-weight: bold; color: #1E293B; text-align: left; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 10px; width: 100%; min-height: 58px; box-sizing: border-box; transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease, background-color .18s ease; -webkit-tap-highlight-color: transparent; }
                .station-menu-btn:hover { transform: translateY(-2px); border-color: #A7F3D0; box-shadow: 0 8px 18px rgba(16,185,129,0.08); }
                .station-menu-btn:active { transform: translateY(-1px) scale(.99); background-color: #F8FFFC; }
                .station-btn-title-wrap { display: flex; align-items: center; gap: 9px; color: #1E293B; min-width: 0; }
                .station-pin-icon-pink { width: 28px; height: 28px; border-radius: 9px; color: #10B981; background: #ECFDF5; font-size: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
                .station-title-stack { display: flex; flex-direction: column; gap: 2px; min-width: 0; }
                .station-name { color:#1E293B; font-size:13px; font-weight:900; line-height:1.25; }
                .station-btn-subtitle { color:#64748B; font-size:11px; line-height:1.25; font-weight:600; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
                .station-chevron-right { width: 26px; height: 26px; border-radius: 50%; background: #ECFDF5; color: #059669; font-size: 13px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }
                .station-emergency-card { background:#FFF7ED; border:1px solid #FED7AA; border-radius:13px; padding:12px; margin:0 0 12px 0; }
                .station-emergency-head { display:flex; align-items:center; gap:6px; color:#C2410C; font-size:12.5px; font-weight:900; margin-bottom:8px; }
                .station-emergency-points { display:grid; grid-template-columns:1fr; gap:5px; margin-bottom:10px; }
                .station-emergency-points span { display:flex; align-items:center; gap:6px; color:#7C2D12; background:#FFFFFF; border:1px solid #FFEDD5; border-radius:9px; padding:7px 9px; font-size:11.5px; font-weight:800; line-height:1.35; }
                .station-phone-btn { width:100%; min-height:42px; border-radius:10px; display:flex; align-items:center; justify-content:center; gap:7px; background:#FFFFFF; border:1px solid #FDBA74; color:#C2410C; text-decoration:none; font-size:13px; font-weight:900; box-sizing:border-box; }
                .station-map-btn { min-height:44px; display:flex; align-items:center; justify-content:center; gap:7px; background:linear-gradient(135deg, #10B981 0%, #059669 100%) !important; border-radius:11px; width:100%; padding:12px; color:white; font-size:13px; font-weight:900; border:none; cursor:pointer; box-sizing:border-box; box-shadow:0 8px 16px rgba(16,185,129,.14); }
                .floating-top-btn { position: fixed !important; bottom: calc(20px + env(safe-area-inset-bottom, 0px)) !important; right: calc(20px + env(safe-area-inset-right, 0px)) !important; width: 50px !important; height: 50px !important; border-radius: 25px !important; background: #005bac !important; color: white !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important; cursor: pointer !important; z-index: 9999 !important; border: none !important; }
                .floating-top-btn i { font-size: 16px; margin-bottom: 2px; }
                .floating-top-btn span { font-size: 8.5px; font-weight: 900; }


                /* ── 💺 シートの使い方・設備：プレミアムUI ── */
                .recline-guide-card { background:linear-gradient(135deg,#F4F8FF 0%,#EEF5FF 100%); border:1px solid #CFE1F5; border-left:5px solid #005BAC; border-radius:16px; padding:12px 14px; margin-bottom:10px; box-shadow:0 5px 14px rgba(0,91,172,.06); text-align:left; }
                .recline-guide-title { display:flex; align-items:center; gap:8px; color:#004B91; font-size:13.5px; font-weight:900; margin:0 0 5px 0; }
                .recline-guide-text { color:#475569; font-size:12px; line-height:1.5; font-weight:600; margin:0; }
                .recline-flow-card { background:#FFFFFF; border:1px solid #E2E8F0; border-radius:16px; padding:4px 12px; margin-bottom:12px; box-shadow:0 4px 12px rgba(15,23,42,.025); text-align:left; }
                .recline-flow-row { display:grid; grid-template-columns:32px 1fr; gap:9px; align-items:flex-start; padding:10px 0; border-bottom:1px solid #F1F5F9; }
                .recline-flow-row:last-child { border-bottom:none; }
                .recline-flow-icon { width:30px; height:30px; border-radius:10px; display:flex; align-items:center; justify-content:center; background:#EAF4FF; color:#005BAC; font-size:16px; flex-shrink:0; }
                .recline-flow-label { color:#1E293B; font-size:12.5px; font-weight:900; line-height:1.35; margin:0 0 2px 0; }
                .recline-flow-text { color:#475569; font-size:11.5px; line-height:1.45; font-weight:600; margin:0; }
                .seat-toggle-btn { display:flex; flex-direction:column; align-items:center; justify-content:center; gap:2px; min-height:48px; padding:8px 6px; line-height:1.2; }
                .seat-toggle-main { display:block; font-size:12.5px; font-weight:900; }
                .seat-toggle-sub { display:block; font-size:10px; font-weight:800; opacity:.78; }
                .seat-guide-intro { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:14px; padding:10px 12px; margin:0 0 8px; color:#475569; font-size:11.5px; line-height:1.5; font-weight:650; text-align:left; }
                .seat-type-note { display:none; }
                .seat-map-wrapper { position:relative; width:100%; max-width:358px; aspect-ratio:4/3; height:auto; border:1px solid rgba(0,91,172,.24); border-radius:20px; margin:0 auto; overflow:hidden; background:#001F4D; box-shadow:0 14px 30px rgba(0,31,77,.14),inset 0 1px 0 rgba(255,255,255,.4); isolation:isolate; }
                .seat-map-wrapper.view-seat3 { aspect-ratio:3/4; max-width:390px; }
                .seat-map-wrapper.view-seat4 { aspect-ratio:3/4; max-width:390px; }
                .seat-map-wrapper::before { content:''; position:absolute; inset:0; z-index:4; background:linear-gradient(180deg,rgba(0,12,36,.04) 0%,rgba(0,12,36,.02) 48%,rgba(0,21,55,.20) 100%); pointer-events:none; }
                .seat-photo-main { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:center; opacity:0; transform:scale(1.01); filter:saturate(1) contrast(1.02) brightness(1); transition:opacity .25s ease,transform .35s ease; z-index:1; }
                .view-seat3 .seat-photo-seat3 { object-fit:contain; object-position:center center; }
                .view-seat3 .seat-photo-seat3 { opacity:1; transform:scale(1); }
                .view-seat4 .seat-photo-seat4 { object-fit:contain; object-position:center center; opacity:1; transform:scale(1); }
                .seat-photo-chip { position:absolute; left:12px; top:12px; z-index:15; display:inline-flex; align-items:center; gap:5px; max-width:calc(100% - 24px); background:rgba(0,31,77,.82); color:#FFFFFF; border:1px solid rgba(255,255,255,.28); border-radius:999px; padding:7px 11px; font-size:11px; font-weight:900; letter-spacing:.02em; box-shadow:0 8px 18px rgba(0,16,40,.24); backdrop-filter:blur(8px); }
                .seat-map-wrapper.view-seat4 .seat-photo-chip { top:auto; bottom:12px; }
                .seat-photo-helper { position:absolute; left:12px; right:12px; bottom:12px; z-index:15; display:flex; align-items:center; gap:8px; background:rgba(255,255,255,.94); color:#17324F; border:1px solid rgba(0,91,172,.18); border-radius:14px; padding:9px 11px; font-size:11.5px; line-height:1.45; font-weight:850; box-shadow:0 10px 24px rgba(0,24,62,.2); backdrop-filter:blur(8px); }
                .seat-photo-helper i { color:#005BAC; font-size:16px; flex-shrink:0; }
                .seat-map-wrapper.has-selection .seat-photo-helper { opacity:0; transform:translateY(6px); pointer-events:none; transition:opacity .18s ease,transform .18s ease; }
                .hotspot-btn { position:absolute; width:44px; min-width:44px; height:44px; box-sizing:border-box; border:none; background:transparent; color:#FFFFFF; border-radius:50%; cursor:pointer; z-index:30; display:flex; align-items:center; justify-content:center; padding:0; font-size:13px; font-weight:900; line-height:1; transition:top .32s cubic-bezier(.25,.8,.25,1),left .32s cubic-bezier(.25,.8,.25,1),transform .18s ease; -webkit-tap-highlight-color:transparent; touch-action:manipulation; }
                .hotspot-btn::before { content:''; position:absolute; left:50%; top:50%; width:25px; height:25px; border:1.3px solid rgba(93,182,255,.32); background:rgba(93,182,255,.04); border-radius:50%; transform:translate(-50%,-50%) scale(.82); animation:seatPinPulse 2.4s infinite; pointer-events:none; z-index:0; }
                .hotspot-btn::after { content:''; position:absolute; left:50%; top:50%; width:20px; height:20px; border-radius:50%; border:1.3px solid rgba(255,255,255,.96); background:radial-gradient(circle at 32% 24%,#6ED0FF 0%,#1681D8 46%,#004A86 100%); box-shadow:0 5px 10px rgba(0,48,106,.25),0 0 0 2px rgba(93,182,255,.09),inset 0 1px 0 rgba(255,255,255,.56); transform:translate(-50%,-50%); pointer-events:none; z-index:1; }
                .hotspot-btn:hover { transform:translateY(-1px) scale(1.03); }
                .hotspot-btn:active { transform:scale(.94); }
                .hotspot-btn i { position:relative; z-index:2; font-size:10.5px; color:#FFFFFF; filter:drop-shadow(0 1px 2px rgba(0,22,49,.42)); pointer-events:none; }
                .hotspot-btn.active { background:transparent !important; border-color:transparent !important; box-shadow:none !important; transform:translateY(-1px) scale(1.08); }
                .hotspot-btn.active::before { width:32px; height:32px; border:2px solid rgba(184,148,70,.72); background:rgba(184,148,70,.1); animation:none; transform:translate(-50%,-50%) scale(1); box-shadow:0 0 0 3px rgba(184,148,70,.12); }
                .hotspot-btn.active::after { width:25px; height:25px; background:radial-gradient(circle at 32% 24%,#1A88D8 0%,#005BAC 52%,#003B72 100%); border:2px solid #F2C95B; box-shadow:0 9px 18px rgba(0,49,109,.34),0 0 0 4px rgba(184,148,70,.16),0 0 20px rgba(184,148,70,.34),inset 0 1px 0 rgba(255,255,255,.55); }
                .hotspot-btn.active i { color:#FFFFFF; filter:drop-shadow(0 1px 2px rgba(0,22,49,.38)); }
                @keyframes seatPinPulse { 0%,58%{transform:translate(-50%,-50%) scale(.82);opacity:.58} 100%{transform:translate(-50%,-50%) scale(1.45);opacity:0} }
                .seat-map-wrapper:not(.has-selection) .hotspot-btn { animation:seatPinGlow 2.8s ease-in-out infinite; }
                @keyframes seatPinGlow { 0%,100%{filter:brightness(1)} 50%{filter:brightness(1.16)} }
                .seat-map-wrapper.view-seat3 .hotspot-btn { margin-left:-22px; margin-top:-22px; }
                .seat-map-wrapper.view-seat4 .hotspot-btn { margin-left:-22px; margin-top:-22px; }
                .interactive-tooltip { display:none; position:absolute; width:218px; max-width:calc(100% - 20px); min-height:70px; box-sizing:border-box; background:linear-gradient(180deg,#FFFFFF 0%,#F7FBFF 100%); color:#1E293B; border-radius:16px; padding:12px 13px 11px; box-shadow:0 16px 34px rgba(0,25,64,.22),0 0 0 1px rgba(255,255,255,.78); z-index:45; border:1px solid rgba(0,91,172,.22); opacity:0; transform:translateY(6px); transition:opacity .18s ease,transform .18s ease; pointer-events:auto; }
                .interactive-tooltip::before { content:''; position:absolute; top:0; left:14px; right:14px; height:3px; border-radius:0 0 999px 999px; background:linear-gradient(90deg,#005BAC,#5DB6FF,#B89446); }
                .interactive-tooltip.show { display:block; opacity:1; transform:translateY(0); }
                .tooltip-title { font-size:12.8px; font-weight:900; color:#003B72; margin-bottom:6px; display:flex; align-items:center; gap:4px; line-height:1.35; padding-bottom:6px; border-bottom:1px solid #E4EEF8; }
                .tooltip-desc { font-size:11.4px; color:#334155; line-height:1.58; margin:0; font-weight:650; text-align:left; }
                .tooltip-detail-btn { display:none; align-items:center; justify-content:center; gap:4px; min-height:32px; margin-top:9px; padding:7px 10px; border:none; border-radius:999px; background:#005BAC; color:#FFFFFF; font-size:11.5px; font-weight:900; cursor:pointer; width:100%; box-shadow:0 6px 12px rgba(0,91,172,.16); }
                .tooltip-leader-line { display:none; position:absolute; height:2px; width:0; background:repeating-linear-gradient(90deg,#005BAC 0 5px,transparent 5px 9px); transform-origin:0 50%; z-index:40; pointer-events:none; filter:drop-shadow(0 0 3px rgba(0,91,172,.44)); }
                .tooltip-leader-line.show { display:block; }
                .seat-hotspot-info { display:none; width:100%; max-width:358px; margin:10px auto 0; box-sizing:border-box; text-align:left; background:linear-gradient(180deg,#FFFFFF 0%,#FBFDFF 100%); border:1px solid #D8E3F0; border-radius:16px; padding:13px 14px 14px; box-shadow:0 6px 16px rgba(0,91,172,.055); }
                .seat-hotspot-info.show { display:block; }
                .seat-hotspot-info.ready { border-color:#C5DAF0; box-shadow:0 8px 18px rgba(0,91,172,.07); }
                .seat-hotspot-info-kicker { display:flex; align-items:center; gap:6px; margin:0 0 7px; color:#64748B; font-size:10.8px; line-height:1.35; font-weight:850; }
                .seat-hotspot-info-kicker i { color:#005BAC; font-size:15px; }
                .seat-hotspot-info-title { margin:0 0 6px; color:#003B72; font-size:14px; line-height:1.42; font-weight:900; overflow-wrap:anywhere; }
                .seat-hotspot-info-desc { margin:0; color:#334155; font-size:12.2px; line-height:1.62; font-weight:650; overflow-wrap:anywhere; }
                .seat-hotspot-info-extra { display:none; margin-top:10px; padding-top:10px; border-top:1px solid #E4EEF8; color:#475569; font-size:11.8px; line-height:1.55; font-weight:650; }
                .seat-feature-detail { display:none; margin:12px auto 0; max-width:340px; background:linear-gradient(180deg,#FFFFFF,#FBFDFF); border:1px solid #D8E3F0; border-radius:16px; padding:14px 15px; box-sizing:border-box; text-align:left; box-shadow:0 5px 15px rgba(0,91,172,.045); }
                .seat-feature-detail.show { display:block; }
                .seat-feature-detail-title { display:flex; align-items:center; gap:8px; font-size:14px; font-weight:900; color:#005BAC; margin-bottom:8px; }
                .seat-feature-detail-body { font-size:12.5px; line-height:1.65; color:#475569; font-weight:600; }
                .seat-feature-detail-body strong { color:#1E293B; font-weight:900; }
                .seat-feature-detail-body .detail-mini-title { display:block; color:#1E293B; font-weight:900; margin:8px 0 2px; }
                .seat-detail-photo { display:block; width:100%; height:176px; object-fit:contain; background:#F8FAFC; border-radius:12px; margin:0 0 10px; border:1px solid #D8E3F0; }
                .seat-detail-photo-cover { height:210px; object-fit:cover; object-position:center 72%; }
                .seat-detail-photo-tall { height:220px; }
                .seat-detail-list { display:flex; flex-direction:column; gap:7px; }
                .seat-detail-row { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:10px; padding:8px 10px; }
                .seat-detail-row strong { display:block; color:#1E293B; font-size:12px; line-height:1.35; margin-bottom:2px; font-weight:900; }
                .seat-detail-row span { display:block; color:#475569; font-size:11.5px; line-height:1.45; font-weight:600; }
                .seat-detail-guide { display:flex; flex-direction:column; gap:8px; }
                .seat-detail-guide-head { display:flex; align-items:center; gap:7px; color:#003B72; font-size:12px; font-weight:900; margin:1px 0 2px; }
                .seat-detail-guide-head i { width:24px; height:24px; border-radius:9px; display:inline-flex; align-items:center; justify-content:center; color:#005BAC; background:#EAF4FF; font-size:14px; flex-shrink:0; }
                .seat-detail-guide-text { margin:0; color:#334155; background:linear-gradient(180deg,#FFFFFF 0%,#F8FBFF 100%); border:1px solid #E1ECF8; border-radius:12px; padding:10px 11px; font-size:12.2px; line-height:1.58; font-weight:650; }
                .seat-equipment-block { background:#FFFFFF; border:1px solid #E1ECF8; border-radius:12px; padding:10px; box-shadow:0 3px 10px rgba(0,91,172,.035); }
                .seat-equipment-title { display:flex; align-items:center; gap:7px; color:#003B72; font-size:12.4px; line-height:1.35; font-weight:900; margin:0 0 7px; }
                .seat-equipment-title i { width:24px; height:24px; border-radius:9px; display:inline-flex; align-items:center; justify-content:center; color:#005BAC; background:#EAF4FF; font-size:14px; flex-shrink:0; }
                .seat-equipment-text { margin:0; color:#475569; font-size:11.8px; line-height:1.55; font-weight:650; }
                .seat-equipment-photo-card { display:flex; flex-direction:column; gap:7px; }
                .seat-equipment-photo { width:100%; height:144px; object-fit:cover; object-position:center; border-radius:10px; border:1px solid #D8E3F0; background:#F8FAFC; }
                .seat-equipment-photo-card span { color:#475569; font-size:11.6px; line-height:1.5; font-weight:650; }
                .seat-equipment-stack { display:flex; flex-direction:column; gap:9px; }
                .seat-equipment-step-card { display:flex; flex-direction:column; gap:7px; background:#F8FBFF; border:1px solid #E1ECF8; border-radius:12px; padding:8px; box-shadow:0 3px 10px rgba(0,91,172,.035); }
                .seat-equipment-step-card strong { display:block; color:#0F2942; font-size:12.3px; line-height:1.35; font-weight:900; }
                .seat-equipment-step-card span { display:block; color:#475569; font-size:11.6px; line-height:1.5; font-weight:650; }
                .seat-equipment-step-photo { width:100%; height:156px; object-fit:cover; object-position:center; border-radius:10px; border:1px solid #D8E3F0; background:#F8FAFC; }
                .seat-equipment-photo-seat { object-position:center 72%; }
                .seat-equipment-photo-contain { height:220px; object-fit:contain; background:#F8FAFC; }
                .seat-equipment-link { width:100%; min-height:42px; border:1px solid #BFD4EA; border-radius:12px; background:#FFFFFF; color:#005BAC; font-size:12.4px; line-height:1.35; font-weight:900; display:flex; align-items:center; justify-content:center; gap:6px; padding:10px 12px; margin-top:9px; cursor:pointer; box-shadow:0 4px 10px rgba(0,91,172,.055); }
                .seat-equipment-link:active { transform:scale(.98); }
                .seat-equipment-accordion { background:#FFFFFF; border:1px solid #E1ECF8; border-radius:12px; overflow:hidden; box-shadow:0 3px 10px rgba(0,91,172,.035); }
                .seat-equipment-accordion + .seat-equipment-accordion { margin-top:8px; }
                .seat-equipment-accordion summary { list-style:none; display:flex; align-items:center; justify-content:space-between; gap:8px; padding:10px 11px; color:#003B72; font-size:12.4px; line-height:1.35; font-weight:900; cursor:pointer; }
                .seat-equipment-accordion summary::-webkit-details-marker { display:none; }
                .seat-equipment-accordion summary span { display:flex; align-items:center; gap:7px; }
                .seat-equipment-accordion summary span i { width:24px; height:24px; border-radius:9px; display:inline-flex; align-items:center; justify-content:center; color:#005BAC; background:#EAF4FF; font-size:14px; flex-shrink:0; }
                .seat-equipment-accordion summary > i { color:#94A3B8; font-size:14px; transition:transform .18s ease; }
                .seat-equipment-accordion[open] summary > i { transform:rotate(180deg); }
                .seat-equipment-accordion-body { display:flex; flex-direction:column; gap:8px; padding:0 10px 10px; }
                .seat-detail-caution strong, .seat-equipment-tip strong { display:block; margin:0 0 5px; font-size:11.8px; line-height:1.35; font-weight:900; }
                .seat-detail-caution ul, .seat-equipment-tip ul { margin:0; padding-left:1.15em; }
                .seat-detail-caution li, .seat-equipment-tip li { margin:3px 0; }
                .seat-equipment-tip { margin-top:8px; padding:8px 10px; border-radius:10px; background:#F8FBFF; border:1px solid #D8E3F0; color:#334155; font-size:11.5px; line-height:1.48; font-weight:700; }
                .seat-detail-step { display:grid; grid-template-columns:28px 1fr; gap:9px; align-items:flex-start; background:linear-gradient(180deg,#FFFFFF 0%,#F8FBFF 100%); border:1px solid #E1ECF8; border-radius:12px; padding:9px 10px; box-shadow:0 3px 10px rgba(0,91,172,.035); }
                .seat-detail-step-no { width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:#005BAC; color:#FFFFFF; font-size:12px; font-weight:900; box-shadow:0 4px 10px rgba(0,91,172,.15); }
                .seat-detail-step strong { display:block; color:#0F2942; font-size:12.4px; line-height:1.35; margin:0 0 2px; font-weight:900; }
                .seat-detail-step span { display:block; color:#475569; font-size:11.7px; line-height:1.48; font-weight:650; }
                .seat-air-card-list { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:8px; }
                .seat-air-card { display:flex; flex-direction:column; gap:7px; background:#FFFFFF; border:1px solid #E1ECF8; border-radius:12px; padding:8px; box-shadow:0 3px 10px rgba(0,91,172,.035); }
                .seat-air-photo { width:100%; height:104px; object-fit:cover; object-position:center; border-radius:10px; border:1px solid #D8E3F0; background:#F8FAFC; }
                .seat-air-card strong { display:block; color:#0F2942; font-size:12.3px; line-height:1.35; margin:0 0 3px; font-weight:900; }
                .seat-air-card span { display:block; color:#475569; font-size:11.6px; line-height:1.48; font-weight:650; }
                .seat-detail-caution { margin-top:8px; padding:8px 10px; border-radius:10px; background:#FFF7ED; border:1px solid #FED7AA; color:#9A3412; font-size:11.5px; line-height:1.45; font-weight:700; }
                .seat-photo-placeholder-card { display:flex; align-items:center; gap:9px; min-height:58px; background:#F8FAFC; border:1px dashed #BFD4EA; border-radius:12px; padding:10px 12px; margin:10px 0 2px; color:#64748B; font-size:11.5px; line-height:1.45; font-weight:800; }
                .seat-photo-placeholder-card i { color:#005BAC; font-size:17px; flex-shrink:0; }
                @media (max-width:380px){ .hotspot-btn::before{width:24px;height:24px}.hotspot-btn::after{width:19px;height:19px}.hotspot-btn.active::before{width:31px;height:31px}.hotspot-btn.active::after{width:24px;height:24px}.hotspot-btn i{font-size:10px}.interactive-tooltip{width:210px}.seat-hotspot-info{padding:12px 13px 13px}.seat-air-photo{height:96px} }
                @media (max-width:355px){ .hotspot-btn::before{width:23px;height:23px}.hotspot-btn::after{width:18px;height:18px}.hotspot-btn.active::before{width:30px;height:30px}.hotspot-btn.active::after{width:23px;height:23px}.hotspot-btn i{display:block;font-size:9.5px}.interactive-tooltip{width:202px;padding:12px 12px 11px}.seat-hotspot-info-title{font-size:13.5px}.seat-hotspot-info-desc{font-size:11.8px}.seat-air-card{padding:7px}.seat-air-photo{height:88px}.seat-air-card strong{font-size:11.8px}.seat-air-card span{font-size:11.1px}.seat-equipment-photo{height:128px}.seat-equipment-step-photo{height:132px}.seat-equipment-photo-contain{height:190px} }


                /* ── 🟠 車内のご利用案内：整理済みアコーディオンUI ── */
                #page-manner {
                    --manner-accent:#F59E0B;
                    --manner-accent-dark:#B85E06;
                    --manner-accent-soft:#FFF7E8;
                    --manner-line:#F6D59A;
                    --manner-border:#E2E8F0;
                    --manner-text:#1E293B;
                    --manner-subtext:#475569;
                    width:100%; min-width:0; max-width:100%; box-sizing:border-box; overflow-x:hidden;
                }
                #page-manner *, #page-manner *::before, #page-manner *::after { box-sizing:border-box; }
                #page-manner .breadcrumb-bar { width:100%; min-width:0; border-bottom-color:#FDE8C4; }
                #page-manner .breadcrumb-current { color:var(--manner-accent-dark); }
                #page-manner .manner-page-intro {
                    width:100%; margin:2px 0 14px; padding:12px 14px; border:1px solid #F2DFC1;
                    border-left:4px solid var(--manner-accent); border-radius:14px; background:#FFFCF7;
                    color:var(--manner-subtext); font-size:12px; line-height:1.62; font-weight:600;
                }
                #page-manner .manner-accordion-list { width:100%; min-width:0; display:flex; flex-direction:column; gap:12px; }
                #page-manner .manner-main-accordion {
                    width:100%; min-width:0; max-width:100%; margin:0; border:1px solid var(--manner-border);
                    border-left:4px solid var(--manner-accent); border-radius:16px; background:#FFFFFF;
                    box-shadow:0 5px 14px rgba(91,55,13,.045); overflow:hidden;
                }
                #page-manner .manner-main-accordion .accordion-header {
                    width:100%; min-width:0; min-height:62px; display:flex; align-items:center; gap:11px;
                    padding:12px 13px; background:#FFFFFF; cursor:pointer; user-select:none;
                    transition:background-color .27s ease, box-shadow .27s ease;
                }
                #page-manner .manner-main-accordion.open .accordion-header { background:#FFFCF7; box-shadow:inset 0 -1px 0 #FDE8C4; }
                #page-manner .manner-main-icon {
                    width:37px; height:37px; flex:0 0 37px; border-radius:11px; display:flex; align-items:center;
                    justify-content:center; color:var(--manner-accent-dark); background:var(--manner-accent-soft);
                    border:1px solid #F5D393; font-size:18px;
                }
                #page-manner .manner-main-svg { width:21px; height:21px; fill:none; stroke:currentColor; stroke-width:2; stroke-linecap:round; stroke-linejoin:round; }
                #page-manner .manner-main-title { min-width:0; flex:1; color:var(--manner-text); font-size:13.5px; line-height:1.4; font-weight:900; }
                #page-manner .manner-main-accordion .accordion-arrow {
                    flex:0 0 auto; color:var(--manner-accent); font-size:12px; transition:transform .27s ease;
                }
                #page-manner .manner-main-accordion.open .accordion-arrow { transform:rotate(90deg); }
                #page-manner .manner-main-accordion .accordion-content {
                    display:grid; grid-template-rows:0fr; width:100%; min-width:0; max-width:100%;
                    padding:0 14px; opacity:0; overflow:hidden;
                    transition:grid-template-rows .27s ease, opacity .22s ease, padding .27s ease;
                }
                #page-manner .manner-main-accordion.open .accordion-content {
                    display:grid !important; grid-template-rows:1fr; padding:14px 14px 16px; opacity:1;
                }
                #page-manner .manner-accordion-inner { min-height:0; overflow:hidden; width:100%; min-width:0; }
                #page-manner .manner-copy { margin:0 0 10px; color:var(--manner-subtext); font-size:12px; line-height:1.72; font-weight:600; }
                #page-manner .manner-copy:last-child { margin-bottom:0; }
                #page-manner .manner-subitem-list { display:flex; flex-direction:column; gap:9px; width:100%; }
                #page-manner .manner-subitem {
                    width:100%; min-width:0; display:grid; grid-template-columns:31px minmax(0,1fr); gap:10px;
                    align-items:flex-start; padding:11px; border:1px solid #F1E2CB; border-radius:12px; background:#FFFCF8;
                }
                #page-manner .manner-subitem-icon {
                    width:31px; height:31px; border-radius:9px; display:flex; align-items:center; justify-content:center;
                    color:var(--manner-accent-dark); background:var(--manner-accent-soft); font-size:16px;
                }
                #page-manner .manner-subitem-title { margin:0 0 4px; color:var(--manner-text); font-size:12.5px; line-height:1.4; font-weight:900; }
                #page-manner .manner-subitem-text { margin:0; color:var(--manner-subtext); font-size:11.8px; line-height:1.68; font-weight:600; overflow-wrap:anywhere; }
                #page-manner .manner-subitem-text + .manner-subitem-text { margin-top:7px; }
                #page-manner .manner-notice {
                    margin-top:10px; padding:11px 12px; border:1px solid #F1CE73; border-left:4px solid #E7A91F;
                    border-radius:11px; background:#FFF8DE; color:#6B4708; font-size:11.7px; line-height:1.65; font-weight:750;
                }
                #page-manner .amenity-section-description { margin:0 0 11px; color:var(--manner-subtext); font-size:12px; line-height:1.6; font-weight:600; }
                #page-manner .amenity-section-shell, #page-manner .amenity-grid,
                #page-manner .amenity-detail-shell, #page-manner .amenity-detail-shell-inner,
                #page-manner .amenity-detail-card { width:100%; min-width:0; max-width:100%; box-sizing:border-box; }
                #page-manner .amenity-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:9px; margin:0; }
                #page-manner .amenity-select-card {
                    width:100%; min-width:0; min-height:112px; padding:12px 8px 11px; border:1px solid #E5E7EB;
                    border-radius:14px; background:linear-gradient(180deg,#FFFFFF,#FBFCFE); cursor:pointer;
                    display:flex; flex-direction:column; align-items:center; justify-content:center; gap:9px;
                    box-shadow:0 4px 12px rgba(15,23,42,.04); transition:transform .18s ease,border-color .22s ease,box-shadow .22s ease,background .22s ease;
                    -webkit-tap-highlight-color:transparent; touch-action:manipulation;
                }
                #page-manner .amenity-select-card:hover { transform:translateY(-2px); border-color:#F3C973; box-shadow:0 8px 18px rgba(175,103,13,.09); }
                #page-manner .amenity-select-card:active { transform:scale(.975); }
                #page-manner .amenity-select-card.is-active { border-color:var(--manner-accent); background:linear-gradient(180deg,#FFFFFF,var(--manner-accent-soft)); box-shadow:0 7px 18px rgba(175,103,13,.11),0 0 0 3px rgba(245,158,11,.07); }
                #page-manner .amenity-line-icon-wrap {
                    width:52px; height:52px; border-radius:15px; display:flex; align-items:center; justify-content:center;
                    color:var(--manner-accent-dark); background:#FFF9EF; border:1px solid #F6D99E;
                }
                #page-manner .amenity-line-icon { width:32px; height:32px; display:block; color:var(--manner-accent-dark); }
                #page-manner .amenity-line-icon * { fill:none; stroke:currentColor; stroke-width:2.45; stroke-linecap:round; stroke-linejoin:round; vector-effect:non-scaling-stroke; }
                #page-manner .amenity-card-name { color:#27364A; font-size:11.5px; line-height:1.35; font-weight:900; text-align:center; overflow-wrap:anywhere; }
                #page-manner .amenity-detail-shell { display:grid; grid-template-rows:0fr; opacity:0; overflow:hidden; margin:0; transition:grid-template-rows .27s ease,opacity .22s ease,margin .27s ease; }
                #page-manner .amenity-detail-shell.is-open { grid-template-rows:1fr; opacity:1; margin:10px 0 0; }
                #page-manner .amenity-detail-shell-inner { min-height:0; overflow:hidden; }
                #page-manner .amenity-detail-card { padding:14px; border:1px solid #F0D19A; border-radius:14px; background:linear-gradient(180deg,#FFFFFF,#FFFCF7); box-shadow:0 4px 12px rgba(100,67,18,.045); }
                #page-manner .amenity-detail-header { display:flex; align-items:center; gap:9px; margin-bottom:8px; }
                #page-manner .amenity-detail-icon { width:31px; height:31px; flex:0 0 31px; border-radius:9px; display:flex; align-items:center; justify-content:center; color:var(--manner-accent-dark); background:var(--manner-accent-soft); border:1px solid #F4D28E; font-size:16px; }
                #page-manner .amenity-detail-title { color:var(--manner-accent-dark); font-size:13.5px; line-height:1.35; font-weight:900; }
                #page-manner .amenity-detail-text { color:#334155; font-size:11.8px; line-height:1.7; font-weight:600; }
                #page-manner .amenity-detail-highlight { display:block; margin-top:10px; padding:10px 11px; background:#FFF8DF; border:1px solid #F4D37D; border-left:4px solid #E5B93E; border-radius:10px; color:#6B4708; font-size:11.5px; line-height:1.62; font-weight:750; }
                @media (max-width:380px) {
                    #page-manner .manner-main-accordion .accordion-header { min-height:58px; padding:11px; }
                    #page-manner .manner-main-icon { width:34px; height:34px; flex-basis:34px; }
                    #page-manner .manner-main-title { font-size:13px; }
                    #page-manner .manner-main-accordion.open .accordion-content { padding:12px 12px 14px; }
                    #page-manner .amenity-select-card { min-height:106px; }
                }



                /* ── 🟠 車内のご利用案内：内側装飾を減らした読みやすい構成 ── */
                #page-manner .manner-main-accordion {
                    box-shadow: 0 3px 10px rgba(91,55,13,.035);
                }
                #page-manner .manner-main-accordion:focus,
                #page-manner .manner-main-accordion:focus-within,
                #page-manner .manner-main-accordion .accordion-header:focus,
                #page-manner .manner-main-accordion .accordion-header:focus-visible {
                    outline: none;
                    box-shadow: none;
                }
                #page-manner .manner-main-accordion.open {
                    border-color: #E7D3B4;
                }
                #page-manner .manner-main-accordion.open .accordion-header {
                    background: #FFFCF8;
                    box-shadow: inset 0 -1px 0 #F3E6D1;
                }
                #page-manner .manner-main-accordion.open .accordion-content {
                    padding: 8px 15px 15px;
                }
                #page-manner .manner-copy {
                    margin: 0;
                    padding: 10px 0;
                    color: var(--manner-subtext);
                    font-size: 12px;
                    line-height: 1.72;
                    font-weight: 600;
                }
                #page-manner .manner-copy + .manner-copy {
                    padding-top: 0;
                }
                #page-manner .manner-subitem-list {
                    display: flex;
                    flex-direction: column;
                    gap: 8px;
                    width: 100%;
                }
                #page-manner .manner-subitem {
                    width: 100%;
                    min-width: 0;
                    display: grid;
                    grid-template-columns: 30px minmax(0, 1fr);
                    gap: 10px;
                    align-items: flex-start;
                    padding: 10px 11px;
                    border: 1px solid #E6EAF0;
                    border-radius: 12px;
                    background: #FFFFFF;
                    box-shadow: 0 2px 8px rgba(15, 23, 42, .024);
                }
                #page-manner .manner-subitem:first-child {
                    margin-top: 0;
                }
                #page-manner .manner-subitem:last-child {
                    margin-bottom: 0;
                }
                #page-manner .manner-subitem.is-key {
                    border-color: #E6EAF0;
                    background: #FFFFFF;
                    box-shadow: none;
                }
                #page-manner .manner-subitem-icon {
                    width: 32px;
                    height: 32px;
                    border: 1px solid var(--card-icon-border);
                    border-radius: 11px;
                    background: var(--card-icon-bg);
                    color: var(--card-accent);
                    font-size: 20px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .72);
                }
                #page-manner .manner-main-icon i,
                #page-manner .manner-subitem-icon i,
                #page-manner .amenity-detail-icon i {
                    line-height: 1;
                }
                #page-manner .manner-subitem.is-key .manner-subitem-icon {
                    background: var(--card-icon-bg);
                    border-color: var(--card-icon-border);
                }
                #page-manner .manner-subitem-svg {
                    width: 19px;
                    height: 19px;
                    fill: none;
                    stroke: currentColor;
                    stroke-width: 2.65;
                    stroke-linecap: round;
                    stroke-linejoin: round;
                }
                #page-manner .manner-subitem-title {
                    margin: 0 0 4px;
                    color: var(--card-dark);
                    font-size: 12.5px;
                    line-height: 1.4;
                    font-weight: 900;
                }
                #page-manner .manner-subitem-text {
                    margin: 0;
                    color: var(--manner-subtext);
                    font-size: 11.8px;
                    line-height: 1.62;
                    font-weight: 600;
                }
                #page-manner .manner-subitem-text + .manner-subitem-text {
                    margin-top: 5px;
                }
                #page-manner .manner-mini-list {
                    margin: 6px 0 0;
                    padding: 0;
                    list-style: none;
                    display: flex;
                    flex-direction: column;
                    gap: 4px;
                    color: var(--manner-subtext);
                    font-size: 11.7px;
                    line-height: 1.55;
                    font-weight: 650;
                }
                #page-manner .manner-mini-list li {
                    position: relative;
                    padding-left: 13px;
                }
                #page-manner .manner-mini-list li::before {
                    content: '';
                    position: absolute;
                    left: 1px;
                    top: .68em;
                    width: 5px;
                    height: 5px;
                    border-radius: 999px;
                    background: #CBD5E1;
                }
                #page-manner .manner-flow-list {
                    gap: 11px;
                }
                #page-manner .manner-flow-list .manner-subitem {
                    position: relative;
                }
                #page-manner .manner-flow-list .manner-subitem:not(:last-child)::after {
                    content: '↓';
                    position: absolute;
                    left: 22px;
                    bottom: -13px;
                    color: #94A3B8;
                    font-size: 11px;
                    line-height: 1;
                    opacity: .55;
                    font-weight: 900;
                }
                #page-manner .manner-rest .manner-subitem-list {
                    gap: 8px;
                }
                #page-manner .manner-rest .manner-subitem {
                    grid-template-columns: 34px minmax(0, 1fr);
                    gap: 10px;
                    padding: 11px 12px;
                    border-radius: 11px;
                }
                #page-manner .manner-rest .manner-subitem-icon {
                    color: var(--card-accent);
                }
                #page-manner .manner-rest .manner-subitem-title {
                    color: var(--card-dark);
                    margin-bottom: 8px;
                }
                #page-manner .rest-toilet-compare {
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 14px;
                    margin-top: 7px;
                    position: relative;
                }
                #page-manner .rest-toilet-compare::before {
                    content: '';
                    position: absolute;
                    top: 8px;
                    bottom: 8px;
                    left: 50%;
                    border-left: 1px dashed #D8DEE8;
                    transform: translateX(-.5px);
                }
                #page-manner .rest-seat-status {
                    min-width: 0;
                    padding: 9px 9px;
                    border: 1px solid #E6EAF0;
                    border-radius: 10px;
                    background: #FFFFFF;
                    display: grid;
                    grid-template-columns: 28px minmax(0, 1fr);
                    gap: 7px;
                    align-items: center;
                    position: relative;
                    z-index: 1;
                }
                #page-manner .rest-seat-status.status-yes {
                    background: #F1FFFB;
                    border-color: #BFEAE1;
                }
                #page-manner .rest-seat-status.status-no {
                    background: #F8FAFC;
                    border-color: #E3E8EF;
                }
                #page-manner .rest-seat-icon {
                    width: 28px;
                    height: 28px;
                    border-radius: 8px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 18px;
                }
                #page-manner .rest-seat-svg {
                    width: 19px;
                    height: 19px;
                    fill: none;
                    stroke: currentColor;
                    stroke-width: 2.25;
                    stroke-linecap: round;
                    stroke-linejoin: round;
                }
                #page-manner .rest-seat-status.status-yes .rest-seat-icon {
                    color: #0A9B83;
                    background: #DDF8F1;
                }
                #page-manner .rest-seat-status.status-no .rest-seat-icon {
                    color: #64748B;
                    background: #EEF2F7;
                }
                #page-manner .rest-seat-name,
                #page-manner .rest-seat-badge {
                    display: block;
                    line-height: 1.35;
                    overflow-wrap: anywhere;
                }
                #page-manner .rest-seat-name {
                    color: #334155;
                    font-size: 10.7px;
                    font-weight: 800;
                    margin-bottom: 3px;
                }
                #page-manner .rest-seat-badge {
                    font-size: 11.2px;
                    font-weight: 900;
                }
                #page-manner .rest-seat-status.status-yes .rest-seat-badge {
                    color: #008B78;
                }
                #page-manner .rest-seat-status.status-no .rest-seat-badge {
                    color: #64748B;
                }
                #page-manner .rest-info-points {
                    display: grid;
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                    gap: 6px;
                    margin-top: 7px;
                }
                #page-manner .rest-info-points span {
                    min-width: 0;
                    padding: 7px 8px;
                    border: 1px solid #E6EAF0;
                    border-radius: 9px;
                    background: #FFFFFF;
                    color: #334155;
                    font-size: 11.3px;
                    line-height: 1.35;
                    font-weight: 800;
                }
                #page-manner .manner-rest .rest-break-card .manner-subitem-icon {
                    color: #E45D7A;
                    background: #FFF1F4;
                    border-color: #F5D2DB;
                }
                #page-manner .manner-rest .rest-break-card .manner-subitem-title {
                    color: #E45D7A;
                }
                #page-manner .rest-info-list {
                    margin: 4px 0 0;
                    padding: 0;
                    list-style: none;
                    display: flex;
                    flex-direction: column;
                    gap: 7px;
                    color: #334155;
                    font-size: 11.6px;
                    line-height: 1.45;
                    font-weight: 650;
                }
                #page-manner .rest-info-list li {
                    display: grid;
                    grid-template-columns: 18px minmax(0, 1fr);
                    gap: 7px;
                    align-items: start;
                }
                #page-manner .rest-info-list i {
                    color: #E87993;
                    font-size: 15px;
                    line-height: 1.35;
                }
                #page-manner .manner-rest .rest-caution-card {
                    border-color: #F2D99B;
                    background: linear-gradient(180deg, #FFFDF8 0%, #FFF9EA 100%);
                }
                #page-manner .manner-rest .rest-caution-card .manner-subitem-icon {
                    background: #FFFFFF;
                    border-color: #F1D99F;
                }
                #page-manner .manner-rest .rest-caution-card .manner-subitem-icon,
                #page-manner .manner-rest .rest-caution-card .manner-subitem-title {
                    color: #C97912;
                }
                #page-manner .manner-rest .rest-caution-card .manner-mini-list li::before {
                    background: #E2A12B;
                }
                #page-manner .manner-notice {
                    margin: 10px 0 0;
                    padding: 10px 11px;
                    border: 1px solid #F1D58B;
                    border-radius: 8px;
                    background: #FFF9E8;
                    box-shadow: none;
                    color: #6B4708;
                    font-size: 11.6px;
                    line-height: 1.65;
                    font-weight: 700;
                }
                #page-manner .amenity-section-description {
                    margin: 2px 0 9px;
                }
                #page-manner .amenity-grid {
                    gap: 8px;
                }
                #page-manner .amenity-select-card {
                    min-height: 98px;
                    padding: 10px 7px 9px;
                    gap: 7px;
                    border-color: #E6E9ED;
                    border-radius: 12px;
                    box-shadow: 0 2px 7px rgba(15,23,42,.025);
                }
                #page-manner .amenity-select-card:hover {
                    transform: translateY(-1px);
                    box-shadow: 0 4px 10px rgba(175,103,13,.055);
                }
                #page-manner .amenity-select-card.is-active {
                    border-color: #DDE5EE;
                    background: #FFFFFF;
                    box-shadow: 0 0 0 2px rgba(217, 139, 36, .08);
                }
                #page-manner .amenity-line-icon-wrap {
                    width: 45px;
                    height: 45px;
                    border-radius: 13px;
                    border-color: var(--card-icon-border);
                    background: var(--card-icon-bg);
                    color: var(--card-accent);
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .75);
                }
                #page-manner .amenity-select-card:hover .amenity-line-icon-wrap,
                #page-manner .amenity-select-card.is-active .amenity-line-icon-wrap {
                    background: var(--card-icon-bg);
                    border-color: var(--card-icon-border);
                }
                #page-manner .amenity-line-icon {
                    width: 28px;
                    height: 28px;
                }
                #page-manner .amenity-detail-shell.is-open {
                    margin-top: 8px;
                }
                #page-manner .amenity-detail-card {
                    padding: 11px 12px;
                    border: 1px solid #E6EAF0;
                    border-radius: 10px;
                    background: #FFFFFF;
                    box-shadow: none;
                }
                #page-manner .amenity-detail-header {
                    margin-bottom: 6px;
                }
                #page-manner .amenity-detail-icon {
                    width: 27px;
                    height: 27px;
                    flex-basis: 27px;
                    border: 1px solid var(--card-icon-border);
                    background: var(--card-icon-bg);
                    color: var(--card-accent);
                    font-size: 17px;
                }
                #page-manner .amenity-detail-title {
                    color: var(--card-dark);
                    font-size: 13px;
                }
                #page-manner .amenity-detail-text {
                    font-size: 11.7px;
                    line-height: 1.68;
                }
                #page-manner .amenity-detail-layout {
                    display: grid;
                    grid-template-columns: 82px minmax(0, 1fr);
                    gap: 10px;
                    align-items: start;
                }
                #page-manner .amenity-detail-photo {
                    width: 82px;
                    height: 64px;
                    border-radius: 10px;
                    object-fit: cover;
                    border: 1px solid #E6EAF0;
                    background: #FFFFFF;
                }
                #page-manner .amenity-detail-copy {
                    min-width: 0;
                }
                #page-manner .amenity-detail-highlight {
                    margin-top: 8px;
                    padding: 8px 9px;
                    border: 1px solid #E8DDD0;
                    border-left: 1px solid #E8DDD0;
                    border-radius: 8px;
                    background: #FFFFFF;
                    box-shadow: none;
                    font-size: 11.3px;
                }
                #page-manner .manner-page-intro {
                    border: 1px solid #E6EAF0;
                    border-left: 1px solid #E6EAF0;
                    background: #FFFFFF;
                }
                #page-manner .manner-main-accordion {
                    --card-accent: var(--manner-accent);
                    --card-dark: var(--manner-accent-dark);
                    --card-soft: var(--manner-accent-soft);
                    --card-tint: #FBFCFE;
                    --card-line: #F6D59A;
                    --card-icon-bg: #FFF7EE;
                    --card-icon-border: #F4D9BD;
                    border: 1px solid #E5EAF0;
                    border-left: 1px solid #E5EAF0;
                    background: #FFFFFF;
                    box-shadow: 0 3px 10px rgba(15, 23, 42, .035);
                }
                #page-manner .manner-accordion-list {
                    margin-top: 12px;
                    gap: 8px;
                }
                #page-manner .manner-seatbelt { --card-accent:#D86A52; --card-dark:#B95744; --card-soft:#FFFFFF; --card-tint:#FFFFFF; --card-line:#E6EAF0; --card-icon-bg:#FFF1EC; --card-icon-border:#F3D7D0; }
                #page-manner .manner-night { --card-accent:#7367C8; --card-dark:#5D52AE; --card-soft:#FFFFFF; --card-tint:#FFFFFF; --card-line:#E6EAF0; --card-icon-bg:#F2EFFF; --card-icon-border:#DDD7F5; }
                #page-manner .manner-device { --card-accent:#3E82D8; --card-dark:#2F6CB8; --card-soft:#FFFFFF; --card-tint:#FFFFFF; --card-line:#E6EAF0; --card-icon-bg:#EFF6FF; --card-icon-border:#D7E7FA; }
                #page-manner .manner-amenity { --card-accent:#D98B24; --card-dark:#B97118; --card-soft:#FFFFFF; --card-tint:#FFFFFF; --card-line:#E6EAF0; --card-icon-bg:#FFF4E2; --card-icon-border:#F0DEC2; }
                #page-manner .manner-rest { --card-accent:#18A889; --card-dark:#0A846F; --card-soft:#FFFFFF; --card-tint:#FFFFFF; --card-line:#E6EAF0; --card-icon-bg:#EAFBF6; --card-icon-border:#CDEDE5; }
                #page-manner .manner-main-accordion .accordion-header {
                    min-height: 50px;
                    padding: 8px 12px;
                    gap: 10px;
                }
                #page-manner .manner-main-icon {
                    color: var(--card-accent);
                    background: var(--card-icon-bg);
                    border-color: var(--card-icon-border);
                    width: 38px;
                    height: 38px;
                    flex-basis: 38px;
                    font-size: 22px;
                    border-radius: 13px;
                    box-shadow: inset 0 1px 0 rgba(255, 255, 255, .72);
                }
                #page-manner .manner-main-svg {
                    width: 24px;
                    height: 24px;
                    stroke-width: 2.75;
                }
                #page-manner .manner-title-stack {
                    flex: 1;
                    min-width: 0;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    gap: 0;
                }
                #page-manner .manner-title-stack .manner-main-title {
                    flex: 0 1 auto;
                    line-height: 1.3;
                    font-size: 13.5px;
                    color: #10233C;
                }
                #page-manner .manner-main-subtitle {
                    display: none;
                }
                #page-manner .manner-main-accordion .accordion-arrow {
                    color: #9AA8B8;
                    width: 24px;
                    height: 24px;
                    flex: 0 0 24px;
                    border-radius: 999px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-left: 4px;
                    background: transparent;
                    font-size: 13px;
                    opacity: 1;
                }
                #page-manner .manner-main-accordion.open {
                    border-color: #E5EAF0;
                    border-left: 1px solid #E5EAF0;
                    background: #FFFFFF;
                }
                #page-manner .manner-main-accordion.open .accordion-header {
                    background: #FFFFFF;
                    box-shadow: inset 0 -1px 0 #E6EAF0;
                }
                #page-manner .manner-main-accordion.open .manner-main-icon {
                    color: var(--card-accent);
                    background: var(--card-icon-bg);
                    border-color: var(--card-icon-border);
                    box-shadow: inset 0 0 0 1px rgba(255, 255, 255, .65);
                }
                #page-manner .manner-main-accordion.open .accordion-arrow {
                    color: var(--card-accent);
                    background: transparent;
                    box-shadow: none;
                    opacity: 1;
                }
                @media (max-width: 380px) {
                    #page-manner .manner-main-accordion .accordion-header {
                        min-height: 48px;
                        padding: 8px 11px;
                        gap: 9px;
                    }
                    #page-manner .manner-main-icon {
                        width: 36px;
                        height: 36px;
                        flex-basis: 36px;
                        font-size: 20px;
                    }
                    #page-manner .manner-main-svg {
                        width: 23px;
                        height: 23px;
                    }
                    #page-manner .manner-main-subtitle {
                        font-size: 10.5px;
                    }
                    #page-manner .manner-main-accordion .accordion-arrow {
                        width: 24px;
                        height: 24px;
                        flex-basis: 24px;
                        margin-left: 2px;
                    }
                    #page-manner .manner-main-accordion.open .accordion-content {
                        padding: 7px 13px 13px;
                    }
                    #page-manner .manner-subitem {
                        grid-template-columns: 30px minmax(0, 1fr);
                        gap: 8px;
                        padding: 9px 10px;
                    }
                    #page-manner .manner-subitem-icon {
                        width: 30px;
                        height: 30px;
                        font-size: 18px;
                    }
                    #page-manner .rest-toilet-compare,
                    #page-manner .rest-info-points {
                        grid-template-columns: 1fr;
                    }
                    #page-manner .rest-toilet-compare::before {
                        display: none;
                    }
                    #page-manner .amenity-detail-layout {
                        grid-template-columns: 74px minmax(0, 1fr);
                        gap: 9px;
                    }
                    #page-manner .amenity-detail-photo {
                        width: 74px;
                        height: 58px;
                    }
                    #page-manner .amenity-select-card {
                        min-height: 92px;
                        padding: 9px 6px 8px;
                    }
                    #page-manner .amenity-line-icon-wrap {
                        width: 42px;
                        height: 42px;
                    }
                    #page-manner .amenity-line-icon {
                        width: 26px;
                        height: 26px;
                    }
                }

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
                    
                    <div id="page-home" class="page-view active">
                        <div class="home-section-title">ご乗車前にご確認ください</div>
                        
                        <div class="hero-prep-card page-trigger" data-target="page-prep">
                            <div class="hero-tag-row">
                                <span class="hero-badge">⚠️ 乗車前に必ず確認</span>
                            </div>
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

                        <div class="category-card card-red page-trigger" data-target="page-help">
                            <div class="card-icon-box bg-red"><i class="ph-bold ph-question"></i></div>
                            <div class="card-main-text">
                                <span class="card-title">困ったときは（FAQ）</span>
                                <p class="card-subtitle">緊急時の対応やお問い合わせ先をご確認いただけます。</p>
                            </div>
                            <div class="card-chevron"><i class="ph-bold ph-caret-right"></i></div>
                        </div>
                    </div>

                    <div id="page-prep" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current c-prep-text">/ 乗車前の準備</span>
                        </div>
                        
                        <div class="heading">最重要｜モバイルバッテリー・リチウムイオン電池製品について</div>
                        <div class="ud-status-box ud-box-danger" style="background:#FFFFFF;">
                            <div class="ud-sign-header">
                                <span class="ud-sign-header-icon"><i class="ph-bold ph-warning"></i></span>
                                <span>必ず車内へお持ち込みください</span>
                            </div>
                            <p style="font-size:11.5px; color:#475569; font-weight:600; margin:0 0 14px 0; line-height:1.6;">
                                モバイルバッテリーなどのリチウムイオン電池製品は、必ず車内へお持ち込みください。発火防止のため、トランクへのお預けは禁止しています。
                            </p>
                            <div class="ud-grid">
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-battery-charging"></i></div><div class="ud-item-label"><span class="ud-main-lbl">モバイルバッテリー</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-device-mobile"></i></div><div class="ud-item-label"><span class="ud-main-lbl">スマートフォン</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-laptop"></i></div><div class="ud-item-label"><span class="ud-main-lbl">ノートPC</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-fan"></i></div><div class="ud-item-label"><span class="ud-main-lbl">携帯扇風機</span></div></div>
                            </div>
                            <p style="font-size:10.5px; color:#94A3B8; font-weight:600; margin:12px 0 0 0; line-height:1.5; border-top:1px dashed #F1F5F9; padding-top:10px;">
                                ※タブレット・電子タバコなど、リチウムイオン電池を使用する製品も対象です。
                            </p>
                        </div>

                        <div class="heading">お荷物について</div>
                        <div class="prep-subheading">トランクへ預けられる荷物（目安）</div>
                        <div class="luggage-diagram-box">
                            <div class="luggage-size-card">
                                <div class="luggage-size-visual">
                                    <!-- ── 🛠️ viewBoxを調整して、イラストにジャストフィット（ズームイン）させて余白をゼロ化 ── -->
                                    <svg class="luggage-size-svg" viewBox="35 15 245 205" xmlns="http://www.w3.org/2000/svg" aria-label="トランク預け荷物のサイズ目安">
                                        <defs>
                                            <linearGradient id="nlSuitcaseFront" x1="0" y1="0" x2="1" y2="1">
                                                <stop offset="0" stop-color="#1E8BF0"/>
                                                <stop offset="1" stop-color="#005BAC"/>
                                            </linearGradient>
                                            <linearGradient id="nlSuitcaseSide" x1="0" y1="0" x2="1" y2="1">
                                                <stop offset="0" stop-color="#0A6FCA"/>
                                                <stop offset="1" stop-color="#003F86"/>
                                            </linearGradient>
                                            <filter id="nlShadow" x="-20%" y="-20%" width="140%" height="150%">
                                                <feDropShadow dx="0" dy="6" stdDeviation="5" flood-color="#005BAC" flood-opacity="0.15"/>
                                            </filter>
                                        </defs>

                                        <!-- 地面の影 -->
                                        <ellipse cx="125" cy="165" rx="55" ry="15" fill="#003F86" opacity="0.12" transform="rotate(-5, 125, 165)"/>

                                        <!-- スーツケース本体 -->
                                        <g filter="url(#nlShadow)">
                                            <!-- キャスター（車輪） -->
                                            <circle cx="78" cy="140" r="5" fill="#1E293B"/>
                                            <circle cx="130" cy="170" r="5" fill="#1E293B"/>
                                            <circle cx="165" cy="150" r="5" fill="#1E293B"/>

                                            <!-- 左正面（幅面） -->
                                            <path d="M130 165 L78 135 V45 L130 75 Z" fill="url(#nlSuitcaseFront)"/>
                                            
                                            <!-- 右側面（奥行面） -->
                                            <path d="M130 165 L165 145 V55 L130 75 Z" fill="url(#nlSuitcaseSide)"/>
                                            
                                            <!-- 上面 -->
                                            <path d="M130 75 L78 45 L113 25 L165 55 Z" fill="#5DB6FF"/>

                                            <!-- 正面の立体リブ加工（白い縞模様） -->
                                            <line x1="117" y1="157.5" x2="117" y2="67.5" stroke="#ffffff" stroke-width="2" opacity="0.3" stroke-linecap="round"/>
                                            <line x1="104" y1="150" x2="104" y2="60" stroke="#ffffff" stroke-width="2" opacity="0.3" stroke-linecap="round"/>
                                            <line x1="91" y1="142.5" x2="91" y2="52.5" stroke="#ffffff" stroke-width="2" opacity="0.3" stroke-linecap="round"/>

                                            <!-- 側面のサイドハンドル -->
                                            <path d="M142 107 Q147.5 112 153 111" fill="none" stroke="#003F86" stroke-width="4" stroke-linecap="round" opacity="0.7"/>

                                            <!-- 上部伸縮ハンドル -->
                                            <path d="M108.5 42.5 V22.5 L134.5 37.5 V57.5" fill="none" stroke="#003F86" stroke-width="4" stroke-linecap="round"/>
                                        </g>

                                        <!-- 寸法線（ガイド点線） -->
                                        <g stroke="#94A3B8" stroke-width="1" stroke-dasharray="2,2">
                                            <!-- 幅の引き出し線 -->
                                            <line x1="78" y1="135" x2="58" y2="147"/>
                                            <line x1="130" y1="165" x2="110" y2="177"/>
                                            <!-- 奥行の引き出し線 -->
                                            <line x1="130" y1="165" x2="147" y2="175"/>
                                            <line x1="165" y1="145" x2="182" y2="155"/>
                                            <!-- 高さの引き出し線 -->
                                            <line x1="165" y1="145" x2="190" y2="145"/>
                                            <line x1="165" y1="55" x2="190" y2="55"/>
                                        </g>

                                        <!-- 寸法線本体（矢印・スラッシュ線） -->
                                        <g stroke="#005BAC" stroke-width="1.5" stroke-linecap="round">
                                            <!-- 幅寸法線 -->
                                            <line x1="58" y1="147" x2="110" y2="177"/>
                                            <line x1="55" y1="151" x2="61" y2="143"/>
                                            <line x1="107" y1="181" x2="113" y2="173"/>
                                            
                                            <!-- 奥行寸法線 -->
                                            <line x1="147" y1="175" x2="182" y2="155"/>
                                            <line x1="144" y1="171" x2="150" y2="179"/>
                                            <line x1="179" y1="151" x2="185" y2="159"/>

                                            <!-- 高さ寸法線 -->
                                            <line x1="190" y1="145" x2="190" y2="55"/>
                                            <line x1="185" y1="145" x2="195" y2="145"/>
                                            <line x1="185" y1="55" x2="195" y2="55"/>
                                        </g>

                                        <!-- 寸法ラベルバッジと数値テキスト -->
                                        <!-- 幅 -->
                                        <rect x="45" y="163" width="68" height="18" rx="9" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
                                        <text x="79" y="175" text-anchor="middle" font-size="9" font-weight="900" fill="#005BAC">幅 約60cm</text>

                                        <!-- 奥行 -->
                                        <rect x="148" y="163" width="68" height="18" rx="9" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
                                        <text x="182" y="175" text-anchor="middle" font-size="9" font-weight="900" fill="#005BAC">奥行 約50cm</text>

                                        <!-- 高さ -->
                                        <rect x="198" y="91" width="74" height="20" rx="10" fill="#EFF6FF" stroke="#BFDBFE" stroke-width="1"/>
                                        <text x="235" y="104" text-anchor="middle" font-size="9" font-weight="900" fill="#005BAC">高さ 約90cm</text>
                                    </svg>
                                </div>
                                <p class="luggage-main-limit">トランク預けの目安<strong>3辺合計200cm以内</strong></p>
                                <div class="luggage-limit-row">
                                    <div class="luggage-limit-chip"><strong>200cm以内</strong><span>3辺合計</span></div>
                                    <div class="luggage-limit-chip"><strong>30kg以内</strong><span>重量</span></div>
                                    <div class="luggage-limit-chip"><strong>1個まで</strong><span>お一人様</span></div>
                                </div>
                            </div>

                            <div class="luggage-method-box">
                                <div class="luggage-method-title">お預けについて</div>
                                <p class="luggage-method-text">スーツケースなどの大きなお荷物は、<br>ご乗車前に乗務員へお預けください。</p>
                                <p class="luggage-method-text">お渡しした手荷物タグは、<br>降車まで大切に保管してください。</p>
                            </div>
                        </div>

                        <div class="prep-subheading" style="margin-top:18px;">お持ち込み・お預かりできないもの</div>
                        <p style="font-size:11px; color:#475569; font-weight:600; margin:-2px 2px 10px 2px; line-height:1.55;">
                            以下のお荷物・危険物は、お持ち込み・お預かりいただけません。
                        </p>
                        <div class="prohibit-group-box" style="border-color: #EF4444; background: #FEF2F2; padding: 12px; margin-bottom: 10px;">
                            <div class="prohibit-grid">
                                <div class="prohibit-card-node"><i class="ph-bold ph-bicycle"></i><span class="prohibit-card-lbl">自転車</span></div>
                                <div class="prohibit-card-node"><i class="ph-bold ph-waves"></i><span class="prohibit-card-lbl">サーフボード</span></div>
                                <div class="prohibit-card-node"><i class="ph-bold ph-guitar"></i><span class="prohibit-card-lbl">大型楽器</span></div>
                                <div class="prohibit-card-node"><i class="ph-bold ph-paw-print"></i><span class="prohibit-card-lbl">ペット</span></div>
                                <div class="prohibit-card-node"><i class="ph-bold ph-warning-diamond"></i><span class="prohibit-card-lbl">危険物</span></div>
                                <div class="prohibit-card-node"><i class="ph-bold ph-balloon"></i><span class="prohibit-card-lbl">ヘリウム入り<br>風船</span></div>
                            </div>
                            <div class="prohibit-guidance-box">
                                <div class="prohibit-guidance-title"><i class="ph-bold ph-info"></i>ご案内</div>
                                <ul class="prohibit-guidance-list">
                                    <li>トランクスペースには限りがあります。</li>
                                    <li>収納できない場合は、お預かりできません。</li>
                                    <li>当日収納できなかった場合は、当社では責任を負いかねますのでご了承ください。</li>
                                </ul>
                            </div>
                        </div>

                        <div class="heading" style="margin-top:18px !important;">ご利用ルール</div>
                        <div class="simple-accordion">
                            <div class="accordion-header">
                                <div class="acc-header-left"><i class="ph-bold ph-fork-knife" style="color:#F59E0B;"></i>飲食について</div>
                                <span class="accordion-arrow">▶</span>
                            </div>
                            <div class="accordion-content">
                                <ul class="rule-bullet-list" style="margin:0; padding-left:18px;">
                                    <li>においの強い飲食物や、カップ麺・汁物などのお持ち込みはご遠慮ください。</li>
                                    <li>消灯後のお食事はご遠慮ください。</li>
                                    <li>パン・おにぎり・お菓子など、においや音が気になりにくいものや、完全に閉まる飲み物は問題ありません。</li>
                                    <li>ゴミは座席ポケットに残さず、サービスエリア等で処分するか、お持ち帰りにご協力ください。</li>
                                </ul>
                            </div>
                        </div>

                        <div class="simple-accordion">
                            <div class="accordion-header">
                                <div class="acc-header-left"><i class="ph-bold ph-x-circle" style="color:#EF4444;"></i>禁酒・禁煙について</div>
                                <span class="accordion-arrow">▶</span>
                            </div>
                            <div class="accordion-content">
                                <ul class="rule-bullet-list" style="margin:0; padding-left:18px;">
                                    <li>車内は全席禁酒・禁煙です。</li>
                                    <li>電子タバコも車内ではご使用いただけません。</li>
                                    <li>喫煙はサービスエリア等の指定場所をご利用ください。</li>
                                    <li>飲酒による酩酊状態や、他のお客様にご迷惑をおかけすると乗務員が判断した場合は、ご乗車をお断りする場合があります。その場合、返金はいたしかねます。</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div id="page-today" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current c-today-text">/ 当日の流れ・のりば</span>
                        </div>
                        
                        <div class="heading">乗車場所・降車場所のご案内</div>
                        <div class="info-card today-notice-card">
                            <p class="info-text today-notice-label"><i class="ph-bold ph-warning-circle"></i>ご乗車前にご確認ください</p>
                            <div class="today-priority-row">
                                <span class="today-priority-icon"><i class="ph-bold ph-clock-countdown"></i></span>
                                <span>
                                    <span class="today-priority-kicker">集合時間</span>
                                    <strong class="today-priority-main">出発10分前です</strong>
                                </span>
                            </div>
                            <ul class="rule-bullet-list today-note-list">
                                <li>指定された乗車場所以外からはご乗車いただけません</li>
                                <li>出発当日の乗車場所・降車場所は変更できません</li>
                                <li>バスは定刻どおり出発します</li>
                            </ul>
                        </div>
                        
                        <div class="item-trigger-btn" id="trigger-stations">
                            <div class="item-icon-container bg-green" style="background-color: #EFF6FF; color: #3B82F6;"><i class="ph-bold ph-map-pin"></i></div>
                            <div class="item-text-node"><div class="item-title">乗車・降車場所を選択</div></div>
                            <div class="item-arrow">▶</div>
                        </div>

                        <div class="heading">乗車当日の流れ</div>
                        <div class="step-outer-container-js">
                            <div class="step-scroll-wrapper" id="js-step-scroller">
                                <div class="step-premium-card">
                                    <div class="step-card-header"><span class="step-badge-node">STEP 1</span></div>
                                    <div class="step-icon-inline"><i class="ph-bold ph-clock"></i></div>
                                    <div class="step-card-title">出発10分前までに集合</div>
                                    <div class="step-action-list"><span>乗車場所を確認</span><span>時間に余裕をもって集合</span></div>
                                </div>
                                <div class="step-premium-card">
                                    <div class="step-card-header"><span class="step-badge-node">STEP 2</span></div>
                                    <div class="step-icon-inline"><i class="ph-bold ph-user-check"></i></div>
                                    <div class="step-card-title">受付・予約確認</div>
                                    <div class="step-action-list"><span>お名前を伝える</span><span>予約内容を確認</span></div>
                                </div>
                                <div class="step-premium-card">
                                    <div class="step-card-header"><span class="step-badge-node">STEP 3</span></div>
                                    <div class="step-icon-inline"><i class="ph-bold ph-suitcase-simple"></i></div>
                                    <div class="step-card-title">荷物のお預け</div>
                                    <div class="step-action-list"><span>トランク荷物を渡す</span><span>手荷物タグを保管</span></div>
                                </div>
                                <div class="step-premium-card">
                                    <div class="step-card-header"><span class="step-badge-node">STEP 4</span></div>
                                    <div class="step-icon-inline"><i class="ph-bold ph-armchair"></i></div>
                                    <div class="step-card-title">ご乗車・着席</div>
                                    <div class="step-action-list"><span>乗務員の案内で乗車</span><span>指定または案内席へ着席</span></div>
                                </div>
                                <div class="step-premium-card">
                                    <div class="step-card-header"><span class="step-badge-node">STEP 5</span></div>
                                    <div class="step-icon-inline"><i class="ph-bold ph-bus"></i></div>
                                    <div class="step-card-title">出発</div>
                                    <div class="step-action-list"><span>シートベルトを着用</span><span>車内案内を確認</span></div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="heading">運行スケジュール</div>
                        <p style="font-size:12px; color:#64748B; margin-bottom:10px;">ご利用便を選択すると、運行スケジュールをご確認いただけます。</p>
                        <select class="bus-select-box" id="bus_select">
                            <option value="bus_201">ナイトライナー 201便（東京行）スケジュール</option>
                            <option value="bus_202">ナイトライナー 202便（大阪行）スケジュール</option>
                        </select>
                        
                        <div class="item-trigger-btn" id="trigger-schedule" style="border: 1px solid #CBD5E1;">
                            <div style="background-color: #10B981; color: white; border-radius: 50%; width: 26px; height: 26px; display: flex; align-items: center; justify-content: center; margin-right: 12px; flex-shrink: 0; font-size: 14px;"><i class="ph-bold ph-arrow-right"></i></div>
                            <div class="item-text-node"><div class="item-title">選択した便のスケジュールを見る</div></div>
                            <div class="item-arrow">▶</div>
                        </div>
                    </div>

                    <div id="page-recline" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current c-recline-text">/ シートの使い方・設備</span>
                        </div>
                        
                        <div class="heading">リクライニングについて</div>
                        <div class="recline-guide-card">
                            <div class="recline-guide-title"><i class="ph-bold ph-armchair"></i> ご乗車時から少し倒れた状態です</div>
                            <p class="recline-guide-text">シートはあらかじめ少し倒した角度で準備しています。必要な場合だけ、ゆっくり調整してください。</p>
                        </div>
                        <div class="recline-flow-card">
                            <div class="recline-flow-row">
                                <div class="recline-flow-icon"><i class="ph-bold ph-user-sound"></i></div>
                                <div>
                                    <p class="recline-flow-label">さらに倒すとき</p>
                                    <p class="recline-flow-text">後方のお客様に一声かけてから操作してください。</p>
                                </div>
                            </div>
                            <div class="recline-flow-row">
                                <div class="recline-flow-icon"><i class="ph-bold ph-hand-palm"></i></div>
                                <div>
                                    <p class="recline-flow-label">ゆっくり操作してください</p>
                                    <p class="recline-flow-text">レバーを持ち、少しずつ倒してください。</p>
                                </div>
                            </div>
                            <div class="recline-flow-row">
                                <div class="recline-flow-icon"><i class="ph-bold ph-arrow-counter-clockwise"></i></div>
                                <div>
                                    <p class="recline-flow-label">シートを戻すとき</p>
                                    <p class="recline-flow-text">降車前は元の位置へゆっくり戻してください。</p>
                                </div>
                            </div>
                        </div>

                        <div class="heading" style="margin-top: 28px !important;">シートについて</div>
                        <div class="seat-toggle-bar">
                            <button class="seat-toggle-btn active" id="js-btn-seat3"><span class="seat-toggle-main">3列独立シート</span><span class="seat-toggle-sub">トイレ付</span></button>
                            <button class="seat-toggle-btn" id="js-btn-seat4"><span class="seat-toggle-main">4列シート</span><span class="seat-toggle-sub">スタンダード</span></button>
                        </div>
                        <p class="seat-guide-intro">シートタイプを選択し、写真上の設備アイコンをタップすると、設備の位置や使い方をご確認いただけます。</p>
                        <p class="seat-type-note" id="js-seat-type-note"></p>
                        
                        <div class="seat-map-wrapper view-seat3" id="seat-canvas-container">
                            <img class="seat-photo-main seat-photo-seat3" src="__SEAT3_PHOTO__" alt="3列独立シート全景">
                            <img class="seat-photo-main seat-photo-seat4" src="__SEAT4_PHOTO__" alt="4列シート全景">
                            <div class="seat-photo-chip" id="js-seat-photo-label">3列独立シート 設備ガイド</div>

                            <div class="hotspot-btn" id="pin-luggage" data-key="luggage" aria-label="荷物棚"><i class="ph-bold ph-bag"></i></div>
                            <div class="hotspot-btn" id="pin-overhead" data-key="overhead" aria-label="読書灯・空調吹出口"><i class="ph-bold ph-lightbulb"></i></div>
                            <div class="hotspot-btn" id="pin-table-legrest" data-key="tableLegrest" aria-label="サイドテーブル・レッグレスト操作部"><i class="ph-bold ph-sliders-horizontal"></i></div>
                            <div class="hotspot-btn" id="pin-legrest" data-key="legrest" aria-label="レッグレスト"><i class="ph-bold ph-armchair"></i></div>
                            <div class="hotspot-btn" id="pin-armrest" data-key="armrest" aria-label="アームレストレバー"><i class="ph-bold ph-hand"></i></div>
                            <div class="hotspot-btn" id="pin-usb" data-key="usb" aria-label="USBポート"><i class="ph-bold ph-usb"></i></div>
                            <div class="hotspot-btn" id="pin-privacy" data-key="privacy" aria-label="プライバシー設備"><i class="ph-bold ph-columns"></i></div>
                            <div class="hotspot-btn" id="pin-recline" data-key="recline" aria-label="リクライニング"><i class="ph-bold ph-arrow-counter-clockwise"></i></div>
                            <div class="hotspot-btn" id="pin-power" data-key="power" aria-label="充電設備"><i class="ph-bold ph-plug-charging"></i></div>
                            <div class="hotspot-btn" id="pin-footcomfort" data-key="footcomfort" aria-label="足元設備"><i class="ph-bold ph-footprints"></i></div>

                            <div class="tooltip-leader-line" id="js-dynamic-line"></div>
                            <div class="interactive-tooltip" id="js-dynamic-tooltip">
                                <div class="tooltip-title" id="js-tt-title">設備名</div>
                                <p class="tooltip-desc" id="js-tt-desc">説明文</p>
                                <button type="button" class="tooltip-detail-btn" id="js-seat-detail-more">詳しく見る</button>
                            </div>
                        </div>
                        <div class="seat-hotspot-info" id="js-seat-hotspot-info" aria-live="polite">
                            <div class="seat-hotspot-info-title" id="js-seat-info-title"></div>
                            <p class="seat-hotspot-info-desc" id="js-seat-info-desc"></p>
                            <div class="seat-hotspot-info-extra" id="js-seat-info-extra"></div>
                        </div>
                        <div class="seat-feature-detail" id="js-seat-feature-detail" aria-hidden="true">
                            <div class="seat-feature-detail-title" id="js-feature-detail-title">天井設備ユニット</div>
                            <div class="seat-feature-detail-body" id="js-feature-detail-body"></div>
                        </div>

                    </div>

                    
<div id="page-manner" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current c-manner-text">/ 車内のご利用案内</span>
                        </div>

                        <div class="manner-accordion-list">
                            <div class="simple-accordion manner-main-accordion manner-seatbelt">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="manner-main-icon" aria-hidden="true">
                                        <svg class="manner-main-svg" viewBox="0 0 24 24"><circle cx="8" cy="5.5" r="1.8"/><path d="M6.8 9.2h3.8l2.4 4.2h4.3"/><path d="M5.4 11.2l3 7.1h9.8"/><path d="M15.3 8.8l3.5 9.5"/><path d="M4.7 18.4h15.2"/></svg>
                                    </span>
                                    <span class="manner-title-stack"><span class="manner-main-title">シートベルトについて</span></span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="manner-accordion-inner">
                                    <div class="manner-subitem-list">
                                        <div class="manner-subitem is-key"><span class="manner-subitem-icon"><svg class="manner-subitem-svg" viewBox="0 0 24 24" aria-hidden="true"><circle cx="8" cy="5.5" r="1.8"/><path d="M6.8 9.2h3.8l2.4 4.2h4.3"/><path d="M5.4 11.2l3 7.1h9.8"/><path d="M15.3 8.8l3.5 9.5"/><path d="M4.7 18.4h15.2"/></svg></span><div><p class="manner-subitem-title">乗車中は必ずシートベルトをご着用ください</p><ul class="manner-mini-list"><li>法律により、全席で着用が義務付けられています。</li><li>急ブレーキや事故の際、お客様の安全を守るため必ずご着用ください。</li></ul></div></div>
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><i class="ph-bold ph-warning-circle"></i></span><div><p class="manner-subitem-title">急停車への備え</p><p class="manner-subitem-text">安全運転に努めていますが、事故防止のため急停車や急ハンドルとなる場合があります。</p></div></div>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion manner-main-accordion manner-night">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="manner-main-icon"><i class="ph-bold ph-moon-stars"></i></span>
                                    <span class="manner-title-stack"><span class="manner-main-title">夜間のルール</span></span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="manner-accordion-inner">
                                    <div class="manner-subitem-list">
                                        <div class="manner-subitem is-key"><span class="manner-subitem-icon"><svg class="manner-subitem-svg" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M12 4v16"/><path d="M7.5 8c1.2 1.4 1.2 6.6 0 8"/><path d="M16.5 8c-1.2 1.4-1.2 6.6 0 8"/></svg></span><div><p class="manner-subitem-title">窓カーテンについて</p><p class="manner-subitem-text">夜間走行中は開け閉めをご遠慮ください。外の光は、他のお客様の安眠を妨げる原因となります。</p></div></div>
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><i class="ph-bold ph-clock"></i></span><div><p class="manner-subitem-title">消灯時間</p><p class="manner-subitem-text">最終経由地を出発してから約5分後に消灯します。消灯前にアナウンスを行います。</p></div></div>
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><i class="ph-bold ph-chat-circle-slash"></i></span><div><p class="manner-subitem-title">消灯後のお願い</p><p class="manner-subitem-text">消灯後の私語は、他のお客様のご迷惑となるためお控えください。</p><p class="manner-subitem-text">休憩時も安眠を妨げないよう、ノーアナウンス・最小限の照明でご案内します。</p></div></div>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion manner-main-accordion manner-device">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="manner-main-icon"><i class="ph-bold ph-device-mobile"></i></span>
                                    <span class="manner-title-stack"><span class="manner-main-title">スマホ・電子機器のマナー</span></span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="manner-accordion-inner">
                                    <div class="manner-subitem-list">
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><svg class="manner-subitem-svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 10v4h3l5 4V6l-5 4H4Z"/><path d="m17 9 4 6"/><path d="m21 9-4 6"/></svg></span><div><p class="manner-subitem-title">音について</p><p class="manner-subitem-text">車内での通話はご遠慮ください。通知音・アラーム・操作音も、乗車前に消音設定をお願いします。</p></div></div>
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><svg class="manner-subitem-svg" viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="3.5" width="12" height="17" rx="3"/><circle cx="12" cy="10.5" r="2.1"/><path d="M12 6.8V5.7"/><path d="M12 15.3v-1.1"/><path d="M8.8 7.3l.8.8"/><path d="M15.2 7.3l-.8.8"/><path d="M8.8 13.7l.8-.8"/><path d="M15.2 13.7l-.8-.8"/></svg></span><div><p class="manner-subitem-title">画面の明るさ</p><p class="manner-subitem-text">消灯後は画面の光が目立ちます。必要な場合は明るさを下げ、周囲に漏れないようご配慮ください。</p></div></div>
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><i class="ph-bold ph-headphones"></i></span><div><p class="manner-subitem-title">イヤホン・音漏れ</p><p class="manner-subitem-text">深夜の車内は非常に静かです。音量は普段より小さめに設定し、音漏れにご注意ください。</p></div></div>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion manner-main-accordion manner-amenity">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="manner-main-icon"><i class="ph-bold ph-gift"></i></span>
                                    <span class="manner-title-stack"><span class="manner-main-title">ナイトライナー限定アメニティ</span></span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="manner-accordion-inner">
                                    <div class="amenity-section-shell">
                                        <div class="amenity-grid" id="js-amenity-grid">
                                            <button type="button" class="amenity-select-card" data-amenity="blanket" aria-pressed="false" aria-label="ブランケットの詳細を表示"><span class="amenity-line-icon-wrap"><svg class="amenity-line-icon" viewBox="0 0 48 48"><path d="M10 14.5h24a5 5 0 0 1 5 5v13.5H15a5 5 0 0 1-5-5V14.5Z"/><path d="M15 33v-9.5a4 4 0 0 1 4-4h20"/><path d="M20 14.5v5M26 14.5v5M32 14.5v5"/><path d="M10 28h5"/></svg></span><span class="amenity-card-name">ブランケット</span></button>
                                            <button type="button" class="amenity-select-card" data-amenity="water" aria-pressed="false" aria-label="ミネラルウォーターの詳細を表示"><span class="amenity-line-icon-wrap"><svg class="amenity-line-icon" viewBox="0 0 48 48"><path d="M20 8h8M21 8v6l-3 4v19a3 3 0 0 0 3 3h6a3 3 0 0 0 3-3V18l-3-4V8"/><path d="M18 22h12M18 33h12"/><path d="M36 18c0 3.2-2.3 5.5-5 5.5"/></svg></span><span class="amenity-card-name">ミネラルウォーター</span></button>
                                            <button type="button" class="amenity-select-card" data-amenity="cushion" aria-pressed="false" aria-label="腰あてクッションの詳細を表示"><span class="amenity-line-icon-wrap"><svg class="amenity-line-icon" viewBox="0 0 48 48"><path d="M13 13c5-2.5 17-2.5 22 0 2 5 2 17 0 22-5 2.5-17 2.5-22 0-2-5-2-17 0-22Z"/><path d="M17 17c3.5 2.5 10.5 2.5 14 0M17 31c3.5-2.5 10.5-2.5 14 0"/><path d="M13 24h22"/></svg></span><span class="amenity-card-name">腰あてクッション</span></button>
                                            <button type="button" class="amenity-select-card" data-amenity="mask" aria-pressed="false" aria-label="フェイスマスクの詳細を表示"><span class="amenity-line-icon-wrap"><svg class="amenity-line-icon" viewBox="0 0 48 48"><path d="M14 11c6-3 14-3 20 0l2 15c1 8-5 13-12 13S11 34 12 26l2-15Z"/><path d="M18.5 21h3M26.5 21h3"/><path d="M20 30c2.5 1.8 5.5 1.8 8 0"/><path d="M14 16 9 20M34 16l5 4"/></svg></span><span class="amenity-card-name">フェイスマスク</span></button>
                                        </div>
                                        <div class="amenity-detail-shell" id="js-amenity-detail-shell" aria-hidden="true"><div class="amenity-detail-shell-inner"><div class="amenity-detail-card"><div class="amenity-detail-header"><span class="amenity-detail-icon" id="js-amenity-detail-icon"><i class="ph-bold ph-sparkle"></i></span><span class="amenity-detail-title" id="js-amenity-detail-title"></span></div><div class="amenity-detail-text" id="js-amenity-detail-text"></div></div></div></div>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion manner-main-accordion manner-rest">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="manner-main-icon"><i class="ph-bold ph-toilet"></i></span>
                                    <span class="manner-title-stack"><span class="manner-main-title">車内トイレ・サービスエリアのご案内</span></span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="manner-accordion-inner">
                                    <div class="manner-subitem-list">
                                        <div class="manner-subitem"><span class="manner-subitem-icon"><i class="ph-bold ph-toilet"></i></span><div><p class="manner-subitem-title">車内トイレ</p><div class="rest-toilet-compare"><div class="rest-seat-status status-yes"><span class="rest-seat-icon"><svg class="rest-seat-svg" viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="4" width="10" height="11" rx="2"/><path d="M6 15h12v3H6z"/><path d="M8 21v-3M16 21v-3"/><path d="M5 8v6M19 8v6"/></svg></span><span><span class="rest-seat-name">3列独立シート</span><span class="rest-seat-badge">✓ 車内トイレあり</span></span></div><div class="rest-seat-status status-no"><span class="rest-seat-icon"><svg class="rest-seat-svg" viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="4" width="10" height="11" rx="2"/><path d="M6 15h12v3H6z"/><path d="M8 21v-3M16 21v-3"/><path d="M5 8v6M19 8v6"/></svg></span><span><span class="rest-seat-name">4列シート（スタンダード）</span><span class="rest-seat-badge">× 車内トイレなし</span></span></div></div></div></div>
                                        <div class="manner-subitem rest-break-card"><span class="manner-subitem-icon"><i class="ph-bold ph-coffee"></i></span><div><p class="manner-subitem-title">サービスエリア休憩</p><ul class="rest-info-list"><li><i class="ph-bold ph-clock"></i><span>約2〜3時間ごとに休憩します（通常2回）</span></li><li><i class="ph-bold ph-megaphone"></i><span>休憩時には乗務員が発車時刻をご案内します</span></li><li><i class="ph-bold ph-moon-stars"></i><span>休憩中は最小限の照明・ノーアナウンスでご案内します</span></li></ul></div></div>
                                        <div class="manner-subitem is-key rest-caution-card"><span class="manner-subitem-icon"><i class="ph-bold ph-warning-circle"></i></span><div><p class="manner-subitem-title">サービスエリアご利用時のお願い</p><ul class="manner-mini-list"><li>発車時刻までに必ずバスへお戻りください。</li><li>定刻運行のため、お戻りが確認できない場合は、お待ちせず出発する場合があります。</li><li>人数確認のため、出発前にカーテンを開けさせていただく場合があります。</li></ul></div></div>
                                    </div>
                                </div></div>
                            </div>
                        </div>
                    </div>

                    <div id="page-help" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current c-help-text">/ 困ったときは</span>
                        </div>

                        <div class="help-page-intro">
                            <i class="ph-bold ph-lifebuoy"></i>
                            <span>お困りの内容を選ぶと、必要な対応や連絡先をすぐに確認できます。</span>
                        </div>

                        <div class="help-accordion-list">
                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="help-main-icon"><i class="ph-bold ph-heartbeat"></i></span>
                                    <span class="help-main-title">体調が優れない場合</span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="help-accordion-inner">
                                    <p class="help-copy">乗車中に気分が悪くなられた場合は、ご遠慮なくお早めに乗務員へお知らせください。</p>
                                </div></div>
                            </div>

                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="help-main-icon"><i class="ph-bold ph-bus"></i></span>
                                    <span class="help-main-title">運行状況・運休情報</span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="help-accordion-inner">
                                    <p class="help-copy">台風・大雪・地震などの天災、高速道路通行止め、交通渋滞、工事、車両故障などにより、運休または大幅な遅延が発生する場合があります。</p>
                                    <p class="help-copy">最新の運行状況は、ナイトライナー公式ホームページのお知らせをご確認ください。</p>
                                    <div class="help-notice-box">
                                        <p>・遅延による返金はありません</p>
                                        <p>・宿泊費・タクシー代等の補償はありません</p>
                                    </div>
                                    <a class="help-action-btn help-web-btn" href="https://www.nightliner.jp/" target="_blank" rel="noopener noreferrer">
                                        <i class="ph-bold ph-globe-hemisphere-west"></i>
                                        <span>最新の運行情報を見る</span>
                                        <i class="ph-bold ph-arrow-square-out"></i>
                                    </a>
                                </div></div>
                            </div>

                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="help-main-icon"><i class="ph-bold ph-alarm"></i></span>
                                    <span class="help-main-title">出発時間に遅れそうな場合</span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="help-accordion-inner">
                                    <div class="help-subsection">
                                        <div class="help-subheading"><i class="ph-bold ph-bus"></i><span>定刻発車について</span></div>
                                        <p class="help-copy">当バスは路線バスとして運行しております。</p>
                                        <p class="help-copy">電車や新幹線と同様に定刻で出発します。</p>
                                        <p class="help-copy">出発10分前までに集合してください。</p>
                                        <p class="help-copy">出発時間までにお越しいただけない場合はキャンセル扱いとなり、返金はございません。</p>
                                        <p class="help-copy">電車遅延の場合も同様です。</p>
                                        <p class="help-copy">また、お客様へのお電話は行っておりません。</p>
                                    </div>
                                    <div class="help-divider"></div>
                                    <div class="help-subsection">
                                        <div class="help-subheading"><i class="ph-bold ph-coffee"></i><span>サービスエリアで乗り遅れた場合</span></div>
                                        <div class="help-notice-box">
                                            <p>・お荷物は東京富士交通車庫でのお引き取りとなります。</p>
                                            <p>・返金・代替交通機関の費用負担はありません。</p>
                                        </div>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="help-main-icon"><i class="ph-bold ph-door-open"></i></span>
                                    <span class="help-main-title">非常口・緊急時の対応</span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="help-accordion-inner">
                                    <div class="help-emergency-row">
                                        <span class="help-emergency-icon" aria-hidden="true">
                                            <svg viewBox="0 0 48 48"><rect x="9" y="6" width="28" height="36" rx="2"></rect><path d="M17 14h12v20H17z"></path><path d="M29 24h8"></path><path d="M33 20l4 4-4 4"></path><circle cx="26" cy="24" r="1.5"></circle></svg>
                                        </span>
                                        <p class="help-copy">バス後方右側に非常口があります。<br><br>赤い枠を外し、ハンドルを矢印方向へ回すと扉が開きます。<br><br><strong>非常時以外は絶対に操作しないでください。</strong></p>
                                    </div>
                                </div></div>
                            </div>

                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header" role="button" tabindex="0" aria-expanded="false">
                                    <span class="help-main-icon"><i class="ph-bold ph-phone-call"></i></span>
                                    <span class="help-main-title">お問い合わせ・忘れ物・緊急連絡先</span>
                                    <span class="accordion-arrow">▶</span>
                                </div>
                                <div class="accordion-content"><div class="help-accordion-inner">
                                    <div class="help-contact-section">
                                        <div class="help-subheading"><i class="ph-bold ph-buildings"></i><span>一般お問い合わせ</span></div>
                                        <p class="help-contact-company">東京富士交通株式会社</p>
                                        <div class="help-phone-number">049-225-1323</div>
                                        <p class="help-contact-meta"><strong>受付時間</strong><br>9:30〜17:30</p>
                                        <div class="help-notice-box help-contact-notice">
                                            <p class="help-notice-title"><i class="ph-bold ph-warning-circle"></i><span>一般お問い合わせの注意事項</span></p>
                                            <ul class="help-note-list">
                                                <li>電話予約は受付していません</li>
                                                <li>当日キャンセルは受付時間内にご連絡ください</li>
                                                <li>17時以降はキャンセル料100％です</li>
                                                <li>忘れ物のお問い合わせもこちらです</li>
                                            </ul>
                                        </div>
                                        <a class="help-action-btn help-phone-btn" href="tel:0492251323"><i class="ph-bold ph-phone-call"></i><span>一般窓口へ電話する</span><i class="ph-bold ph-caret-right"></i></a>
                                    </div>

                                    <div class="help-divider"></div>

                                    <div class="help-contact-section help-emergency-contact">
                                        <div class="help-subheading"><i class="ph-bold ph-siren"></i><span>発車当日の緊急連絡先</span></div>
                                        <div class="help-phone-number help-emergency-number">050-3851-0388</div>
                                        <p class="help-contact-meta"><strong>利用可能時間</strong><br>出発30分前〜出発時間まで</p>
                                        <div class="help-notice-box">
                                            <p class="help-notice-title"><i class="ph-bold ph-warning-octagon"></i><span>緊急連絡先の注意事項</span></p>
                                            <ul class="help-note-list">
                                                <li>この番号ではキャンセル受付はできません</li>
                                                <li>利用可能時間は出発30分前から出発時間までです</li>
                                                <li>出発時間経過後のキャンセルは返金できません</li>
                                            </ul>
                                        </div>
                                        <a class="help-action-btn help-emergency-btn" href="tel:05038510388"><i class="ph-bold ph-siren"></i><span>緊急連絡先へ電話する</span><i class="ph-bold ph-caret-right"></i></a>
                                    </div>
                                </div></div>
                            </div>
                        </div>
                    </div>

                </div>
                
                <button class="floating-top-btn" id="js-float-top">
                    <i class="ph-bold ph-caret-double-up"></i>
                    <span>TOP</span>
                </button>
            </div>

            <div id="app_modal" class="modal-mask">
                <div class="modal-box">
                    <div class="modal-top"><span id="modal_title" style="font-size:15px; font-weight:900; color:#005bac;">詳細案内</span><span class="modal-close-icon" id="modal-close-btn">✕</span></div>
                    <div id="app_modal_scroll_body" class="modal-scroll"></div>
                </div>
            </div>

            <script>
                function initApp() {
                    const kitchenSink = document.getElementById('js-scroll-body');

                    function syncStreamlitFrameHeight() {
                        const appWrapper = document.getElementById('js-app-wrapper');
                        const scrollBody = document.getElementById('js-scroll-body');
                        const activePage = document.querySelector('.page-view.active');

                        const contentHeight = Math.max(
                            appWrapper ? Math.ceil(appWrapper.scrollHeight) : 0,
                            scrollBody ? Math.ceil(scrollBody.scrollHeight) : 0,
                            activePage ? Math.ceil(activePage.scrollHeight + activePage.getBoundingClientRect().top) : 0,
                            Math.ceil(document.body.scrollHeight),
                            Math.ceil(document.body.offsetHeight),
                            Math.ceil(document.documentElement.scrollHeight),
                            Math.ceil(document.documentElement.offsetHeight)
                        );
                        const height = Math.max(1200, contentHeight + 24);

                        try {
                            if (window.frameElement) {
                                window.frameElement.style.height = height + 'px';
                                window.frameElement.setAttribute('height', String(height));
                            }
                        } catch (error) {
                            // iframeの直接更新が許可されない環境ではpostMessageのみ使用。
                        }

                        window.parent.postMessage({
                            isStreamlitMessage: true,
                            type: 'streamlit:setFrameHeight',
                            height: height
                        }, '*');
                    }

                    let frameHeightTimer = null;
                    function scheduleFrameHeightSync() {
                        window.clearTimeout(frameHeightTimer);
                        frameHeightTimer = window.setTimeout(syncStreamlitFrameHeight, 40);

                        // CSSトランジションや画像描画後の高さも拾う。
                        window.setTimeout(syncStreamlitFrameHeight, 160);
                        window.setTimeout(syncStreamlitFrameHeight, 420);
                    }

                    function scrollBrowserToTop() {
                        // ページ切替時は、以前のブラウザスクロール位置を引き継がない。
                        // smooth指定は高さ再計算と競合するため、即時で先頭へ戻す。
                        window.scrollTo(0, 0);

                        try {
                            if (window.frameElement) {
                                window.frameElement.scrollIntoView({ block: 'start', inline: 'nearest', behavior: 'auto' });
                            }
                        } catch (error) {
                            // サンドボックス環境では親画面側の直接操作が制限される場合がある。
                        }

                        try {
                            window.parent.scrollTo(0, 0);
                        } catch (error) {
                            // frameElement.scrollIntoView側で先頭位置を合わせる。
                        }

                        // ページ表示・iframe高さ更新後にも、念のため先頭位置を確定する。
                        window.requestAnimationFrame(function() {
                            window.scrollTo(0, 0);
                            try {
                                if (window.frameElement) {
                                    window.frameElement.scrollIntoView({ block: 'start', inline: 'nearest', behavior: 'auto' });
                                }
                            } catch (error) {}
                        });
                    }

                    if (window.ResizeObserver) {
                        const frameResizeObserver = new ResizeObserver(scheduleFrameHeightSync);
                        [
                            document.getElementById('js-app-wrapper'),
                            document.getElementById('js-scroll-body'),
                            document.body,
                            document.documentElement
                        ].forEach(function(target) {
                            if (target) frameResizeObserver.observe(target);
                        });
                    }

                    if (window.MutationObserver) {
                        const frameMutationObserver = new MutationObserver(scheduleFrameHeightSync);
                        const mutationTarget = document.getElementById('js-app-wrapper') || document.body;
                        frameMutationObserver.observe(mutationTarget, {
                            subtree: true,
                            childList: true,
                            attributes: true,
                            attributeFilter: ['class', 'style', 'src', 'aria-hidden', 'aria-expanded']
                        });
                    }

                    document.querySelectorAll('img').forEach(function(image) {
                        if (!image.complete) {
                            image.addEventListener('load', scheduleFrameHeightSync, { once: true });
                            image.addEventListener('error', scheduleFrameHeightSync, { once: true });
                        }
                    });

                    window.addEventListener('load', scheduleFrameHeightSync);
                    window.addEventListener('resize', scheduleFrameHeightSync);
                    scheduleFrameHeightSync();

                    const mask = document.getElementById('app_modal');
                    const modalBody = document.getElementById('app_modal_scroll_body');
                    const modalTitle = document.getElementById('modal_title');
                    
                    const stepScroller = document.getElementById('js-step-scroller');
                    const stepPrevBtn = document.getElementById('js-step-prev');
                    const stepNextBtn = document.getElementById('js-step-next');

                    const canvasContainer = document.getElementById('seat-canvas-container');
                    const photoLabel = document.getElementById('js-seat-photo-label');

                    const dynamicTooltip = document.getElementById('js-dynamic-tooltip');
                    const dynamicLine = document.getElementById('js-dynamic-line');
                    const ttTitle = document.getElementById('js-tt-title');
                    const ttDesc = document.getElementById('js-tt-desc');
                    const detailMoreBtn = document.getElementById('js-seat-detail-more');
                    const featureDetailCard = document.getElementById('js-seat-feature-detail');
                    const featureDetailTitle = document.getElementById('js-feature-detail-title');
                    const featureDetailBody = document.getElementById('js-feature-detail-body');
                    const seatTypeNote = document.getElementById('js-seat-type-note');
                    const seatInfoPanel = document.getElementById('js-seat-hotspot-info');
                    const seatInfoTitle = document.getElementById('js-seat-info-title');
                    const seatInfoDesc = document.getElementById('js-seat-info-desc');
                    const seatInfoExtra = document.getElementById('js-seat-info-extra');
                    const seat4AirPin = document.getElementById('pin-privacy');
                    if (seat4AirPin) {
                        seat4AirPin.dataset.key = 'seat4Air';
                        seat4AirPin.setAttribute('aria-label', '個別空調');
                        seat4AirPin.innerHTML = '<i class="ph-bold ph-wind"></i>';
                    }
                    let currentSeatType = 'seat3';
                    let currentSeatFeatureKey = null;

                    const pinConfig = {
                        seat3: {
                            "pin-luggage":       { top: "12.2%", left: "30.5%", display: "flex" },
                            "pin-overhead":      { top: "12.7%", left: "59.0%", display: "flex" },
                            "pin-table-legrest": { top: "57.9%", left: "71.8%", display: "flex" },
                            "pin-power":         { top: "67.4%", left: "72.6%", display: "flex" },
                            "pin-legrest":       { top: "90.3%", left: "78.2%", display: "flex" },
                            "pin-armrest":       { top: "71.4%", left: "46.7%", display: "flex" },
                            "pin-recline":       { top: "79.3%", left: "37.6%", display: "flex" },
                            "pin-usb":           { top: "85.7%", left: "48.3%", display: "flex" },
                            "pin-footcomfort":   { top: "92.4%", left: "92.1%", display: "flex" },
                            "pin-privacy":       { top: "0%", left: "0%", display: "none" }
                        },
                        seat4: {
                            "pin-luggage":       { top: "5.8%", left: "34.0%", display: "flex" },
                            "pin-overhead":      { top: "3.6%", left: "16.4%", display: "flex" },
                            "pin-armrest":       { top: "41.5%", left: "13.4%", display: "flex" },
                            "pin-recline":       { top: "80.4%", left: "38.2%", display: "flex" },
                            "pin-power":         { top: "87.6%", left: "82.0%", display: "flex" },
                            "pin-privacy":       { top: "2.6%", left: "4.8%", display: "flex" },
                            "pin-table-legrest": { top: "0%", left: "0%", display: "none" },
                            "pin-legrest":       { top: "0%", left: "0%", display: "none" },
                            "pin-usb":           { top: "0%", left: "0%", display: "none" },
                            "pin-footcomfort":   { top: "0%", left: "0%", display: "none" }
                        }
                    };

                    const schedules = {
                        bus_201: {
                            title: "201便（東京行）スケジュール",
                            html: [
                                '<div class="image-timeline-container">',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-clipboard-text"></i></span><span class="node-time">20:45</span><span class="node-title">受付</span></div>',
                                '    <div class="node-desc">手荷物お預け・乗車受付開始</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-red">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-bus"></i></span><span class="node-time">21:15</span><span class="node-title">出発</span></div>',
                                '    <div class="node-desc">のりばを定刻に出発</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-megaphone"></i></span><span class="node-time">22:30</span><span class="node-title">案内アナウンス</span></div>',
                                '    <div class="node-desc">車内案内放送（シート・アメニティ案内）<br><span id="js-toggle-script" style="font-size:11.5px; color:#3B82F6; font-weight:bold; cursor:pointer; text-decoration:underline; display:inline-block; margin-top:4px;">[ 📄 車内放送原稿 ]</span><div id="announcement_script_box" style="display:none; background-color:#F8FAFC; border:1px dashed #CBD5E1; border-radius:6px; padding:10px; margin-top:6px; font-size:11px; color:#334155; line-height:1.4; max-height:150px; overflow-y:auto;"><span style="background-color:#EFF6FF; color:#2563EB; font-size:9px; padding:1px 4px; border-radius:3px; font-weight:bold;">日本語</span><br>皆様、夜遅くからのご乗車お疲れ様です。当便は定刻通り出発いたしました。これより最初の休憩地まで約2時間走行いたします。<br><br><span style="background-color:#F0FDF4; color:#16A34A; font-size:9px; padding:1px 4px; border-radius:3px; font-weight:bold;">English</span><br>Thank you for choosing NIGHTLINER. This bus has departed on schedule.</div></div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-red">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-moon-stars"></i></span><span class="node-time">23:00</span><span class="node-title">消灯</span></div>',
                                '    <div class="node-desc">車内完全消灯（スマホ利用禁止）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-coffee"></i></span><span class="node-time">23:30</span><span class="node-title">休憩</span></div>',
                                '    <div class="node-desc">第1サービスエリア休憩（20分間）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-coffee"></i></span><span class="node-time">03:15</span><span class="node-title">休憩</span></div>',
                                '    <div class="node-desc">第2サービスエリア休憩（20分間）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-map-pin"></i></span><span class="node-time">05:30</span><span class="node-title">到着</span></div>',
                                '    <div class="node-desc">東京方面降車停留所 到着</div>',
                                '  </div>',
                                '</div>'
                            ].join('')
                        },
                        bus_202: {
                            title: "202便（大阪行）スケジュール",
                            html: [
                                '<div class="image-timeline-container">',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-clipboard-text"></i></span><span class="node-time">22:10</span><span class="node-title">受付</span></div>',
                                '    <div class="node-desc">手荷物お預け・乗車受付開始</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-red">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-bus"></i></span><span class="node-time">22:40</span><span class="node-title">出発</span></div>',
                                '    <div class="node-desc">のりばを定刻に出発</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-megaphone"></i></span><span class="node-time">23:45</span><span class="node-title">案内アナウンス</span></div>',
                                '    <div class="node-desc">車内案内放送</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-red">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-moon-stars"></i></span><span class="node-time">00:15</span><span class="node-title">消灯</span></div>',
                                '    <div class="node-desc">車内完全消灯（スマホ利用禁止）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-coffee"></i></span><span class="node-time">00:45</span><span class="node-title">休憩</span></div>',
                                '    <div class="node-desc">第1サービスエリア休憩（20分間）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-coffee"></i></span><span class="node-time">04:30</span><span class="node-title">休憩</span></div>',
                                '    <div class="node-desc">第2サービスエリア休憩（20分間）</div>',
                                '  </div>',
                                '  <div class="image-timeline-node node-blue">',
                                '    <div class="node-header"><span class="node-event-icon"><i class="ph-bold ph-map-pin"></i></span><span class="node-time">06:50</span><span class="node-title">到着</span></div>',
                                '    <div class="node-desc">関西方面降車停留所 到着</div>',
                                '  </div>',
                                '</div>'
                            ].join('')
                        }
                    };

                    const seatFeatureData = {
                        luggage: {
                            title: "荷物棚",
                            desc: "小さな手荷物を収納できます。重い荷物や貴重品は置かず、落下しないようご注意ください。"
                        },
                        overhead: {
                            title: "読書灯・個別空調",
                            desc: "読書灯と個別空調の位置です。",
                            detail: '<img class="seat-detail-photo" src="__OVERHEAD_PHOTO__" alt="読書灯・個別空調の全体写真"><div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-lightbulb"></i><span>読書灯</span></div><p class="seat-equipment-text">オレンジ色のボタンを押すと点灯します。消灯後は、周囲のお客様へのご配慮をお願いいたします。</p></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-wind"></i><span>個別空調</span></div><div class="seat-air-card-list"><div class="seat-air-card"><img class="seat-air-photo" src="__AIR_VENT_OPEN_PHOTO__" alt="個別空調の吹出口が開いている写真"><div><strong>吹出口を開いた状態</strong><span>吹出口の向きを動かすことで、風向きを調整できます。</span></div></div><div class="seat-air-card"><img class="seat-air-photo" src="__AIR_VENT_CLOSED_PHOTO__" alt="個別空調の吹出口を閉じている写真"><div><strong>吹出口を閉じた状態</strong><span>風を止めたい場合は、吹出口を閉じる位置まで回してください。</span></div></div></div></div></div>'
                        },
                        tableLegrest: {
                            title: "サイドテーブル・レッグレスト操作部",
                            desc: "サイドテーブルとレッグレスト操作部の位置です。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-tray"></i><span>サイドテーブル</span></div><div class="seat-equipment-stack"><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SIDE_TABLE_DEPLOYED_PHOTO__" alt="サイドテーブルがアームレスト内に収納されている状態の写真"><strong>収納状態</strong><span>サイドテーブルはアームレスト内に収納されています。</span></div><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SIDE_TABLE_UNLOCK_PHOTO__" alt="アームレスト上部を開けてサイドテーブルを取り出す写真"><strong>取り出し方</strong><span>アームレスト上部を開け、中からサイドテーブルを手動で引き出してください。</span></div></div></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-armchair"></i><span>レッグレスト操作部</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo seat-equipment-photo-contain" src="__LEGREST_OPERATION_PHOTO__" alt="アームレスト先端のボタンとレッグレストが分かる写真"><span>アームレスト先端のボタンを押すと、レッグレストが動きます。</span></div></div></div>'
                        },
                        privacy: {
                            title: "カーテン・仕切り",
                            desc: "外光や隣席からの視線をやわらげます。乗降時は開けてください。"
                        },
                        recline: {
                            title: "リクライニングレバー",
                            desc: "レバーを引いたまま、背もたれへゆっくり体重をかけて倒します。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-map-pin"></i><span>レバーの位置</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo" src="__RECLINE_POSITION_PHOTO__" alt="リクライニングレバーの位置が分かる写真"><span>白い矢印が付いたレバーが、リクライニング操作部です。</span></div></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-hand-tap"></i><span>操作方法</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo" src="__RECLINE_OPERATION_PHOTO__" alt="リクライニングレバーを引いている写真"><span>レバーを矢印の方向へ引いたまま、背もたれにゆっくり体重をかけます。お好みの位置でレバーを離すと、その位置で固定されます。</span></div></div></div>'
                        },
                        power: {
                            title: "コンセント",
                            desc: "携帯電話などの充電に限りご利用いただけます。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-plug-charging"></i><span>コンセント</span></div><p class="seat-equipment-text">携帯電話などの充電に限りご利用いただけます。</p><div class="seat-detail-caution"><strong>ご利用時のお願い</strong><ul><li>パソコン・DVD機器・ゲーム機器などにはご使用いただけません。</li><li>瞬間的な停電や電圧低下が発生する場合がありますので、あらかじめご了承ください。</li></ul></div></div></div>'
                        },
                        legrest: {
                            title: "レッグレスト",
                            desc: "ふくらはぎを支え、長時間の移動をより快適にします。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-armchair"></i><span>レッグレスト</span></div><p class="seat-equipment-text">ふくらはぎを支えることで、足への負担やむくみを軽減し、長時間の移動をより快適にします。</p><button type="button" class="seat-equipment-link" data-seat-target="tableLegrest"><i class="ph-bold ph-caret-right"></i><span>レッグレストの操作方法</span></button></div></div>'
                        },
                        armrest: {
                            title: "アームレストレバー",
                            desc: "アームレスト先端のレバーを押しながら、アームレストを動かしてください。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-map-pin"></i><span>レバーの位置</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo seat-equipment-photo-contain" src="__ARMREST_LEVER_POSITION_PHOTO__" alt="アームレスト先端とレバーの位置が分かる写真"><span>アームレスト先端にあるレバーです。リクライニングレバーとは別の操作部です。</span></div></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-hand-tap"></i><span>操作している様子</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo seat-equipment-photo-contain" src="__ARMREST_LEVER_OPERATION_PHOTO__" alt="アームレスト先端のレバーを押している写真"><span>アームレスト先端のレバーを押しながら、アームレストを動かしてください。</span></div></div></div>'
                        },
                        usb: {
                            title: "USBポート",
                            desc: "USB対応機器の充電にご利用いただけます。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-usb"></i><span>USBポート</span></div><p class="seat-equipment-text">USB対応機器の充電にご利用いただけます。充電ケーブルはお客様ご自身でご用意ください。</p></div></div>'
                        },
                        footcomfort: {
                            title: "フットレスト",
                            desc: "手動で倒して、足元を楽にできます。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-footprints"></i><span>フットレスト</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo seat-equipment-photo-contain" src="__FOOTREST_PHOTO__" alt="フットレストを手動で倒している写真"><span>フットレストは手動で倒してご利用ください。</span></div><div class="seat-equipment-tip"><strong>快適ポイント</strong><ul><li>靴を脱いだ状態、または靴下でご利用いただくと、より快適にお休みいただけます。</li><li>足を乗せることで、長時間の移動も快適にお過ごしいただけます。</li></ul></div></div></div>'
                        }
                    };

                    const seat4FeatureData = {
                        luggage: seatFeatureData.luggage,
                        overhead: seatFeatureData.overhead,
                        armrest: {
                            title: "アームレスト",
                            desc: "通路側席・窓側席とも共通のひじ掛けです。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-armchair"></i><span>アームレスト</span></div><div class="seat-equipment-photo-card"><img class="seat-equipment-photo seat-equipment-photo-contain" src="__SEAT4_PHOTO__" alt="4列シートのアームレスト位置が分かる写真"><span>座席横のアームレストです。通路側席・窓側席ともに、ひじ掛けとしてご利用いただけます。</span></div></div></div>'
                        },
                        recline: {
                            title: "リクライニングレバー",
                            desc: "通路側席と窓側席でレバー位置が異なります。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-armchair"></i><span>通路側席</span></div><p class="seat-equipment-text">アームレスト下部のレバーを引くことでリクライニングできます。</p><div class="seat-equipment-stack"><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_AISLE_POSITION_PHOTO__" alt="4列シート通路側席のリクライニングレバー位置"><strong>レバーの位置</strong><span>通路側のアームレスト下部にあります。</span></div><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_AISLE_OPERATION_PHOTO__" alt="4列シート通路側席のリクライニング操作写真"><strong>操作方法</strong><span>レバーを引いたまま、背もたれへゆっくり体重をかけてください。</span></div></div></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-sidebar"></i><span>窓側席</span></div><p class="seat-equipment-text">座席の窓側にある短い縦型レバーを引くことでリクライニングできます。</p><div class="seat-equipment-stack"><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_WINDOW_POSITION_PHOTO__" alt="4列シート窓側席のリクライニングレバー位置"><strong>レバーの位置</strong><span>窓側の壁寄りにある、短い縦型のレバーです。</span></div><div class="seat-equipment-step-card"><img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_WINDOW_OPERATION_PHOTO__" alt="4列シート窓側席のリクライニング操作写真"><strong>操作方法</strong><span>レバーを引いたまま、背もたれへゆっくり体重をかけてください。</span></div></div></div></div>'
                        },
                        power: {
                            title: "コンセント・USBポート",
                            desc: "座席前方に設置されています。",
                            detail: '<div class="seat-detail-guide"><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-plug-charging"></i><span>コンセント</span></div><p class="seat-equipment-text">携帯電話などの充電に限りご利用いただけます。</p><div class="seat-detail-caution"><strong>ご利用時のお願い</strong><ul><li>パソコン・DVD機器・ゲーム機器などにはご使用いただけません。</li><li>瞬間的な停電や電圧低下が発生する場合がありますので、あらかじめご了承ください。</li></ul></div></div><div class="seat-equipment-block"><div class="seat-equipment-title"><i class="ph-bold ph-usb"></i><span>USBポート</span></div><p class="seat-equipment-text">USB対応機器の充電にご利用いただけます。充電ケーブルはお客様ご自身でご用意ください。</p></div></div>'
                        }
                    };

                    seat4FeatureData.overhead = {
                        title: "読書灯",
                        desc: "読書灯の位置と使い方をご案内します。",
                        detail: `<div class="seat-detail-guide">
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-lightbulb"></i><span>読書灯</span></div>
                                <p class="seat-equipment-text">オレンジ色のボタンを押すと点灯します。消灯後は、周囲のお客様へのご配慮をお願いいたします。</p>
                            </div>
                        </div>`
                    };

                    seat4FeatureData.seat4Air = {
                        title: "個別空調",
                        desc: "吹出口の向きや開閉で風量を調整できます。",
                        detail: `<div class="seat-detail-guide">
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-wind"></i><span>個別空調</span></div>
                                <div class="seat-air-card-list">
                                    <div class="seat-air-card">
                                        <img class="seat-air-photo" src="__AIR_VENT_OPEN_PHOTO__" alt="個別空調の吹出口が開いている写真">
                                        <div><strong>吹出口を開いた状態</strong><span>吹出口の向きを動かすことで、風向きを調整できます。</span></div>
                                    </div>
                                    <div class="seat-air-card">
                                        <img class="seat-air-photo" src="__AIR_VENT_CLOSED_PHOTO__" alt="個別空調の吹出口を閉じている写真">
                                        <div><strong>吹出口を閉じた状態</strong><span>風を止めたい場合は、吹出口を閉じる位置まで回してください。</span></div>
                                    </div>
                                </div>
                            </div>
                        </div>`
                    };

                    seat4FeatureData.armrest = {
                        title: "アームレスト",
                        desc: "通路側席・窓側席とも共通のひじ掛けです。",
                        detail: `<div class="seat-detail-guide">
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-armchair"></i><span>アームレスト</span></div>
                                <p class="seat-equipment-text">座席横のひじ掛けです。通路側席・窓側席ともに、腕を休めるためにご利用いただけます。</p>
                            </div>
                        </div>`
                    };

                    seat4FeatureData.recline = {
                        title: "リクライニングレバー",
                        desc: "座席によってレバーの位置が異なります。",
                        detail: `<div class="seat-detail-guide">
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-info"></i><span>座席に合わせて確認</span></div>
                                <p class="seat-equipment-text">座席によってリクライニングレバーの位置が異なります。ご利用の座席に合わせてご確認ください。</p>
                            </div>
                            <details class="seat-equipment-accordion">
                                <summary><span><i class="ph-bold ph-armchair"></i>通路側席</span><i class="ph-bold ph-caret-down"></i></summary>
                                <div class="seat-equipment-accordion-body">
                                    <p class="seat-equipment-text">通路側席は、アームレスト下部のレバーを引くことでリクライニングできます。</p>
                                    <div class="seat-equipment-stack">
                                        <div class="seat-equipment-step-card">
                                            <img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_AISLE_POSITION_PHOTO__" alt="4列シート通路側席のリクライニングレバー位置">
                                            <strong>レバーの位置</strong><span>通路側のアームレスト下部にあります。</span>
                                        </div>
                                        <div class="seat-equipment-step-card">
                                            <img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_AISLE_OPERATION_PHOTO__" alt="4列シート通路側席のリクライニング操作写真">
                                            <strong>操作方法</strong><span>レバーを引いたまま、背もたれへゆっくり体重をかけてください。</span>
                                        </div>
                                    </div>
                                </div>
                            </details>
                            <details class="seat-equipment-accordion">
                                <summary><span><i class="ph-bold ph-sidebar"></i>窓側席</span><i class="ph-bold ph-caret-down"></i></summary>
                                <div class="seat-equipment-accordion-body">
                                    <p class="seat-equipment-text">窓側席は、座席窓側にある短い縦型のレバーを引くことでリクライニングできます。</p>
                                    <div class="seat-equipment-stack">
                                        <div class="seat-equipment-step-card">
                                            <img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_WINDOW_POSITION_PHOTO__" alt="4列シート窓側席のリクライニングレバー位置">
                                            <strong>レバーの位置</strong><span>窓側の壁寄りにある、短い縦型のレバーです。</span>
                                        </div>
                                        <div class="seat-equipment-step-card">
                                            <img class="seat-equipment-step-photo" src="__SEAT4_RECLINE_WINDOW_OPERATION_PHOTO__" alt="4列シート窓側席のリクライニング操作写真">
                                            <strong>操作方法</strong><span>レバーを引いたまま、背もたれへゆっくり体重をかけてください。</span>
                                        </div>
                                    </div>
                                </div>
                            </details>
                        </div>`
                    };

                    seat4FeatureData.power = {
                        title: "コンセント・USBポート",
                        desc: "座席前方に設置されています。",
                        detail: `<div class="seat-detail-guide">
                            <img class="seat-detail-photo seat-detail-photo-tall" src="__SEAT4_POWER_USB_PHOTO__" alt="4列シートのコンセント・USBポート位置">
                            <p class="seat-detail-guide-text">コンセント・USBポートは座席前方に設置されています。</p>
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-plug-charging"></i><span>コンセント</span></div>
                                <p class="seat-equipment-text">携帯電話などの充電に限りご利用いただけます。</p>
                                <div class="seat-detail-caution"><strong>ご利用時のお願い</strong><ul><li>パソコン・DVD機器・ゲーム機器などにはご使用いただけません。</li><li>瞬間的な停電や電圧低下が発生する場合がありますので、あらかじめご了承ください。</li></ul></div>
                            </div>
                            <div class="seat-equipment-block">
                                <div class="seat-equipment-title"><i class="ph-bold ph-usb"></i><span>USBポート</span></div>
                                <p class="seat-equipment-text">USB対応機器の充電にご利用いただけます。充電ケーブルはお客様ご自身でご用意ください。</p>
                            </div>
                        </div>`
                    };

                    function getSeatFeatureData(key) {
                        if (currentSeatType === 'seat4' && seat4FeatureData[key]) {
                            return seat4FeatureData[key];
                        }
                        return seatFeatureData[key];
                    }

                    const illustSeat3 = document.getElementById('illustSeat3');
                    const illustSeat4 = document.getElementById('illustSeat4');

                    function applySeatLayout(type) {
                        if (!canvasContainer) return;
                        currentSeatType = type;
                        const partition = document.getElementById('js-bus-privacy-partition');
                        const wallSide = document.getElementById('js-bus-wall-side');
                        
                        if (type === 'seat3') {
                            canvasContainer.className = "seat-map-wrapper view-seat3";
                            if (partition) partition.style.display = "block";
                            if (wallSide) wallSide.style.right = "-45px"; 
                            if (photoLabel) photoLabel.innerText = "3列独立シート 設備ガイド";
                            if (seatTypeNote) seatTypeNote.innerText = "";
                            if (illustSeat3) illustSeat3.style.display = "block";
                            if (illustSeat4) illustSeat4.style.display = "none";
                        } else {
                            canvasContainer.className = "seat-map-wrapper view-seat4";
                            if (partition) partition.style.display = "none";
                            if (wallSide) wallSide.style.right = "0px";    
                            if (photoLabel) photoLabel.innerText = "4列シート 設備ガイド";
                            if (seatTypeNote) seatTypeNote.innerText = "";
                            if (illustSeat3) illustSeat3.style.display = "none";
                            if (illustSeat4) illustSeat4.style.display = "block";
                        }
                        
                        const configs = pinConfig[type];
                        for (const id in configs) {
                            const pinEl = document.getElementById(id);
                            if (pinEl) {
                                pinEl.style.top = configs[id].top;
                                pinEl.style.left = configs[id].left;
                                pinEl.style.display = configs[id].display;
                            }
                        }
                        if (dynamicTooltip) dynamicTooltip.classList.remove('show');
                        if (dynamicLine) dynamicLine.classList.remove('show');
                        document.querySelectorAll('.hotspot-btn').forEach(p => p.classList.remove('active'));
                        currentSeatFeatureKey = null;
                        if (detailMoreBtn) detailMoreBtn.style.display = 'none';
                        resetSeatInfoPanel(type);
                        if (featureDetailCard) {
                            featureDetailCard.classList.remove('show');
                            featureDetailCard.setAttribute('aria-hidden', 'true');
                        }
                        if (featureDetailBody) featureDetailBody.innerHTML = '';
                    }

                    function resetSeatInfoPanel(type) {
                        if (!seatInfoPanel) return;
                        if (type === 'seat3') {
                            seatInfoPanel.classList.remove('show');
                            seatInfoPanel.classList.remove('ready');
                            if (seatInfoTitle) seatInfoTitle.innerText = "";
                            if (seatInfoDesc) seatInfoDesc.innerText = "";
                            if (seatInfoExtra) {
                                seatInfoExtra.innerHTML = "";
                                seatInfoExtra.style.display = "none";
                            }
                        } else {
                            seatInfoPanel.classList.remove('show', 'ready');
                        }
                    }

                    function updateSeatInfoPanel(data) {
                        if (!seatInfoPanel || !data) return;
                        seatInfoPanel.classList.add('show', 'ready');
                        if (seatInfoTitle) seatInfoTitle.innerText = data.title;
                        if (seatInfoDesc) seatInfoDesc.innerText = data.desc;
                        if (seatInfoExtra) {
                            const extraHtml = data.detail || data.extra || "";
                            seatInfoExtra.innerHTML = extraHtml;
                            seatInfoExtra.style.display = extraHtml ? "block" : "none";
                        }
                    }

                    if (seatInfoPanel) {
                        seatInfoPanel.addEventListener('click', function(e) {
                            const targetButton = e.target.closest('[data-seat-target]');
                            if (!targetButton) return;
                            e.preventDefault();
                            e.stopPropagation();
                            const targetKey = targetButton.getAttribute('data-seat-target');
                            const targetPin = document.querySelector('.hotspot-btn[data-key="' + targetKey + '"]');
                            if (targetPin) {
                                targetPin.click();
                                seatInfoPanel.scrollIntoView({ block: 'nearest', inline: 'nearest', behavior: 'smooth' });
                            }
                        });
                    }

                    applySeatLayout('seat3');

                    if (stepScroller) {
                        stepScroller.addEventListener('wheel', function(e) {
                            if (e.deltaY !== 0) {
                                e.preventDefault();
                                stepScroller.scrollLeft += e.deltaY;
                            }
                        }, { passive: false });
                    }
                    if (stepNextBtn && stepScroller) { stepNextBtn.addEventListener('click', function() { stepScroller.scrollBy({ left: 240, behavior: 'smooth' }); }); }
                    if (stepPrevBtn && stepScroller) { stepPrevBtn.addEventListener('click', function() { stepScroller.scrollBy({ left: -240, behavior: 'smooth' }); }); }

                    if (detailMoreBtn) {
                        detailMoreBtn.addEventListener('click', function(e) {
                            e.stopPropagation();
                            const data = getSeatFeatureData(currentSeatFeatureKey);
                            if (!data || !data.detail || !featureDetailCard) return;
                            if (featureDetailTitle) featureDetailTitle.innerText = data.title;
                            if (featureDetailBody) featureDetailBody.innerHTML = data.detail;
                            featureDetailCard.classList.add('show');
                            featureDetailCard.setAttribute('aria-hidden', 'false');
                        });
                    }
                    document.querySelectorAll('.hotspot-btn').forEach(pin => {
                        pin.addEventListener('click', function(e) {
                            e.stopPropagation();
                            document.querySelectorAll('.hotspot-btn').forEach(p => p.classList.remove('active'));
                            this.classList.add('active');
                            if (canvasContainer) canvasContainer.classList.add('has-selection');

                            const key = this.getAttribute('data-key');
                            const data = getSeatFeatureData(key);

                            if (!data || !dynamicTooltip || !dynamicLine || !canvasContainer) return;

                            currentSeatFeatureKey = key;
                            ttTitle.innerText = data.title;
                            ttDesc.innerText = data.desc;
                            if (detailMoreBtn) detailMoreBtn.style.display = data.detail ? 'inline-flex' : 'none';
                            if (featureDetailCard) {
                                featureDetailCard.classList.remove('show');
                                featureDetailCard.setAttribute('aria-hidden', 'true');
                            }
                            if (featureDetailBody) featureDetailBody.innerHTML = '';

                            if (currentSeatType === 'seat3' || currentSeatType === 'seat4') {
                                if (dynamicTooltip) dynamicTooltip.classList.remove('show');
                                if (dynamicLine) dynamicLine.classList.remove('show');
                                updateSeatInfoPanel(data);
                                return;
                            }

                            /* 実寸を取得するため、見えない状態で一度描画する */
                            dynamicTooltip.classList.remove('show');
                            dynamicLine.classList.remove('show');
                            dynamicTooltip.style.visibility = 'hidden';
                            dynamicTooltip.style.left = '0px';
                            dynamicTooltip.style.top = '0px';
                            dynamicTooltip.classList.add('show');

                            requestAnimationFrame(function() {
                                const canvasRect = canvasContainer.getBoundingClientRect();
                                const pinRect = pin.getBoundingClientRect();
                                const canvasWidth = canvasContainer.clientWidth;
                                const canvasHeight = canvasContainer.clientHeight;
                                const px = pinRect.left - canvasRect.left + pinRect.width / 2;
                                const py = pinRect.top - canvasRect.top + pinRect.height / 2;
                                const ttWidth = Math.min(dynamicTooltip.offsetWidth || 228, canvasWidth - 20);
                                const ttHeight = dynamicTooltip.offsetHeight || 84;
                                const edgePad = 10;
                                const gap = 22;
                                const pinHalfW = pinRect.width / 2;
                                const pinHalfH = pinRect.height / 2;

                                const clamp = function(value, min, max) {
                                    return Math.max(min, Math.min(value, max));
                                };

                                const candidates = [
                                    {
                                        side: 'left',
                                        left: px - pinHalfW - gap - ttWidth,
                                        top: py - ttHeight / 2
                                    },
                                    {
                                        side: 'right',
                                        left: px + pinHalfW + gap,
                                        top: py - ttHeight / 2
                                    },
                                    {
                                        side: 'above',
                                        left: px - ttWidth / 2,
                                        top: py - pinHalfH - gap - ttHeight
                                    },
                                    {
                                        side: 'below',
                                        left: px - ttWidth / 2,
                                        top: py + pinHalfH + gap
                                    }
                                ];

                                /* 右側のピンは左表示を、左側のピンは右表示を優先 */
                                if (px < canvasWidth / 2) {
                                    candidates.splice(0, 2, candidates[1], candidates[0]);
                                }

                                let selected = null;
                                for (const candidate of candidates) {
                                    const fitsHorizontally = candidate.left >= edgePad && candidate.left + ttWidth <= canvasWidth - edgePad;
                                    const fitsVertically = candidate.top >= edgePad && candidate.top + ttHeight <= canvasHeight - edgePad;
                                    if (fitsHorizontally && fitsVertically) {
                                        selected = candidate;
                                        break;
                                    }
                                }

                                /* どの方向にも完全には収まらない場合は、はみ出し量が最小の候補を選ぶ */
                                if (!selected) {
                                    let bestScore = Infinity;
                                    candidates.forEach(function(candidate) {
                                        const overflowLeft = Math.max(0, edgePad - candidate.left);
                                        const overflowRight = Math.max(0, candidate.left + ttWidth - (canvasWidth - edgePad));
                                        const overflowTop = Math.max(0, edgePad - candidate.top);
                                        const overflowBottom = Math.max(0, candidate.top + ttHeight - (canvasHeight - edgePad));
                                        const score = overflowLeft + overflowRight + overflowTop + overflowBottom;
                                        if (score < bestScore) {
                                            bestScore = score;
                                            selected = candidate;
                                        }
                                    });
                                }

                                let ttLeft = clamp(selected.left, edgePad, canvasWidth - ttWidth - edgePad);
                                let ttTop = clamp(selected.top, edgePad, canvasHeight - ttHeight - edgePad);

                                /* クランプ後にピンと重なった場合は、反対側へ逃がす */
                                const pinLeft = px - pinHalfW;
                                const pinRight = px + pinHalfW;
                                const pinTop = py - pinHalfH;
                                const pinBottom = py + pinHalfH;
                                const overlapsPin = !(
                                    ttLeft + ttWidth + 8 < pinLeft ||
                                    ttLeft - 8 > pinRight ||
                                    ttTop + ttHeight + 8 < pinTop ||
                                    ttTop - 8 > pinBottom
                                );

                                if (overlapsPin) {
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
                            currentSeatFeatureKey = null;
                            resetSeatInfoPanel(currentSeatType);
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
                                scrollBrowserToTop();
                            }
                        });
                    });

                    document.querySelectorAll('.back-to-home-trigger').forEach(btn => {
                        btn.addEventListener('click', function() {
                            const parentPage = this.closest('.page-view');
                            if (parentPage) parentPage.classList.remove('active');
                            const homePage = document.getElementById('page-home');
                            if (homePage) homePage.classList.add('active');
                            scrollBrowserToTop();
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
                            scheduleFrameHeightSync();
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

                    function positionModalInVisibleViewport() {
                        if (!mask) return;

                        let visibleTop = 0;
                        let visibleHeight = Math.max(320, window.innerHeight || 0);

                        try {
                            if (window.frameElement) {
                                const frameRect = window.frameElement.getBoundingClientRect();
                                visibleTop = Math.max(0, Math.round(-frameRect.top));
                            }
                            if (window.parent && window.parent.innerHeight) {
                                visibleHeight = Math.max(320, Math.round(window.parent.innerHeight));
                            }
                        } catch (error) {
                            // 親画面へ直接アクセスできない場合はiframe内の値を使用する。
                        }

                        mask.style.position = 'absolute';
                        mask.style.top = visibleTop + 'px';
                        mask.style.left = '0';
                        mask.style.width = '100%';
                        mask.style.height = visibleHeight + 'px';
                    }

                    function openModal(title, html) {
                        if(mask && modalTitle && modalBody) {
                            positionModalInVisibleViewport();
                            mask.classList.add('show');
                            modalTitle.innerText = title;
                            modalBody.innerHTML = html;
                            bindModalEvents();
                            scheduleFrameHeightSync();
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
                        floatTopBtn.addEventListener('click', scrollBrowserToTop);
                    }

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
        .replace("__SEAT4_RECLINE_AISLE_POSITION_PHOTO__", seat4_recline_aisle_position_photo)
        .replace("__SEAT4_RECLINE_AISLE_OPERATION_PHOTO__", seat4_recline_aisle_operation_photo)
        .replace("__SEAT4_RECLINE_WINDOW_POSITION_PHOTO__", seat4_recline_window_position_photo)
        .replace("__SEAT4_RECLINE_WINDOW_OPERATION_PHOTO__", seat4_recline_window_operation_photo)
        .replace("__SEAT4_POWER_USB_PHOTO__", seat4_power_usb_photo)
        .replace("__OVERHEAD_PHOTO__", overhead_photo)
        .replace("__RECLINE_POSITION_PHOTO__", recline_position_photo)
        .replace("__RECLINE_OPERATION_PHOTO__", recline_operation_photo)
        .replace("__AIR_VENT_OPEN_PHOTO__", air_vent_open_photo)
        .replace("__AIR_VENT_CLOSED_PHOTO__", air_vent_closed_photo)
        .replace("__SIDE_TABLE_UNLOCK_PHOTO__", side_table_unlock_photo)
        .replace("__SIDE_TABLE_DEPLOYED_PHOTO__", side_table_deployed_photo)
        .replace("__LEGREST_OPERATION_PHOTO__", legrest_operation_photo)
        .replace("__ARMREST_LEVER_POSITION_PHOTO__", armrest_lever_position_photo)
        .replace("__ARMREST_LEVER_OPERATION_PHOTO__", armrest_lever_operation_photo)
        .replace("__FOOTREST_PHOTO__", footrest_photo)
        .replace("__AMENITY_BLANKET_PHOTO__", amenity_blanket_photo)
        .replace("__AMENITY_SET_PHOTO__", amenity_set_photo)
    )
    st.components.v1.html(html, height=1400, scrolling=False)

if __name__ == "__main__":
    main()
