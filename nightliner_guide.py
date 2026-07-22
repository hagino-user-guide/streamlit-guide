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
    
    # 🎯 実際にassetsフォルダにあるファイル名に修正
    seat3_photo = image_data_uri("seat_3_main.jpg")
    seat4_photo = image_data_uri("seat_4_main.jpg")
    overhead_photo = image_data_uri("seat_overhead_console.jpg")
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
    amenity_blanket_photo = image_data_uri("amenity_blanket.jpg")
    amenity_set_photo = image_data_uri("amenity_set.jpg")
    
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
                
                /* ── 🚍 LP風リデザインヘッダー ── */
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

                #page-today .heading { color: #10B981 !important; border-left-color: #10B981 !important; }
                #page-today .step-badge-node { color: #047857; background: #ECFDF5; }
                #page-today .step-icon-inline { color: #10B981; }
                #page-today .step-premium-card { flex: 0 0 178px; min-height: 164px; padding: 16px 14px; border-color: #D1FAE5; box-shadow: 0 4px 12px rgba(16,185,129,0.04); }
                #page-today .step-scroll-wrapper { gap: 12px; padding: 8px 2px 16px 2px; }
                #page-today .step-outer-container-js { display: block !important; margin-bottom: 4px; }
                #page-today #trigger-schedule { border-color: #A7F3D0 !important; background: #FFFFFF; }
                #page-today #trigger-schedule .item-title { color: #065F46 !important; }
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

                /* Help page */
                #page-help {
                    --help-blue: #005BAC; --help-text: #1E293B; --help-muted: #475569; --help-border: #E2E8F0;
                    --help-red: #E53E3E; --help-orange: #F59E0B; --help-coral: #EF4444; --help-green: #10B981;
                    width: 100%; min-width: 0; max-width: 100%; box-sizing: border-box; overflow-x: hidden;
                }
                #page-help *, #page-help *::before, #page-help *::after { box-sizing: border-box; }
                #page-help .breadcrumb-current { color: #C53030; }
                #page-help .heading { color: var(--help-blue) !important; border-left-color: var(--help-blue) !important; margin-bottom: 12px !important; }
                #page-help .help-page-intro { display: flex; align-items: flex-start; gap: 9px; width: 100%; min-width: 0; margin: 2px 0 14px; padding: 12px 13px; border: 1px solid #D8E7F7; border-left: 4px solid var(--help-blue); border-radius: 14px; background: #F8FBFF; color: var(--help-muted); font-size: 12px; line-height: 1.62; font-weight: 700; box-shadow: 0 3px 10px rgba(0, 91, 172, 0.035); }
                #page-help .help-page-intro i { flex: 0 0 auto; margin-top: 1px; color: var(--help-blue); font-size: 18px; line-height: 1; }
                #page-help .help-accordion-list { display: flex; flex-direction: column; gap: 12px; width: 100%; min-width: 0; }
                #page-help .help-main-accordion { width: 100%; min-width: 0; max-width: 100%; margin: 0; border: 1px solid var(--help-border); border-radius: 16px; background: #FFFFFF; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03); overflow: hidden; }
                #page-help .help-main-accordion.open { border-color: #DDE7F1; box-shadow: 0 6px 16px rgba(15, 23, 42, 0.045); }
                #page-help .help-main-accordion .accordion-header { width: 100%; min-width: 0; min-height: 62px; display: flex; align-items: center; justify-content: flex-start; gap: 12px; padding: 12px 13px; background: #FFFFFF; cursor: pointer; user-select: none; -webkit-tap-highlight-color: transparent; transition: background-color .22s ease, box-shadow .22s ease; }
                #page-help .help-main-accordion .accordion-header:hover, #page-help .help-main-accordion .accordion-header:active { background: #F8FAFC; }
                #page-help .help-main-accordion .accordion-header:focus, #page-help .help-main-accordion .accordion-header:focus-visible { outline: none; box-shadow: inset 0 0 0 2px rgba(0, 91, 172, .10); }
                #page-help .help-main-accordion.open .accordion-header { background: #FFFFFF; box-shadow: inset 0 -1px 0 #F1F5F9; }
                #page-help .help-main-icon { width: 38px; height: 38px; flex: 0 0 38px; display: flex; align-items: center; justify-content: center; border-radius: 12px; border: 1px solid #D9E7F7; background: #EFF6FF; color: var(--help-blue); font-size: 20px; line-height: 1; }
                #page-help .help-main-icon i { display: block; line-height: 1; }
                #page-help .help-main-title { flex: 1; min-width: 0; color: var(--help-text); font-size: 13.8px; line-height: 1.4; font-weight: 900; text-align: left; }
                #page-help .help-main-accordion .accordion-arrow { flex: 0 0 auto; margin-left: auto; color: #CBD5E1; font-size: 12px; transition: transform .22s ease, color .22s ease; }
                #page-help .help-main-accordion.open .accordion-arrow { transform: rotate(90deg); }
                
                #page-help .help-accordion-list .help-main-accordion:nth-child(1) .help-main-icon { color: var(--help-red); background: #FFF5F5; border-color: #FED7D7; }
                #page-help .help-accordion-list .help-main-accordion:nth-child(2) .help-main-icon { color: var(--help-orange); background: #FFFBEB; border-color: #FDE68A; }
                #page-help .help-accordion-list .help-main-accordion:nth-child(3) .help-main-icon { color: var(--help-coral); background: #FFF1F2; border-color: #FECDD3; }
                #page-help .help-accordion-list .help-main-accordion:nth-child(4) .help-main-icon { color: var(--help-blue); background: #EFF6FF; border-color: #BFDBFE; }
                #page-help .help-accordion-list .help-main-accordion:nth-child(5) .help-main-icon { color: var(--help-green); background: #ECFDF5; border-color: #A7F3D0; }
                
                #page-help .help-main-accordion .accordion-content { display: grid; grid-template-rows: 0fr; width: 100%; min-width: 0; max-width: 100%; padding: 0 14px; opacity: 0; overflow: hidden; text-align: left !important; transition: grid-template-rows .24s ease, opacity .2s ease, padding .24s ease; }
                #page-help .help-main-accordion.open .accordion-content { display: grid !important; grid-template-rows: 1fr; padding: 13px 14px 15px; opacity: 1; }
                #page-help .help-accordion-inner { min-height: 0; width: 100%; min-width: 0; overflow: hidden; }
                #page-help .help-copy { margin: 0 0 9px; color: var(--help-muted); font-size: 12px; line-height: 1.72; font-weight: 600; overflow-wrap: anywhere; }
                #page-help .help-copy:last-child { margin-bottom: 0; }
                #page-help .help-subheading { display: flex; align-items: center; gap: 7px; margin: 0 0 9px; color: var(--help-text); font-size: 13px; line-height: 1.4; font-weight: 900; }
                #page-help .help-subheading i { width: 23px; height: 23px; flex: 0 0 23px; display: inline-flex; align-items: center; justify-content: center; color: var(--help-blue); font-size: 17px; }
                #page-help .help-emergency-contact .help-subheading { color: #991B1B; }
                #page-help .help-emergency-contact .help-subheading i { color: #C53030; }
                #page-help .help-divider { height: 1px; margin: 14px 0; background: #EEF1F4; }
                #page-help .help-emergency-row { display: grid; grid-template-columns: 46px minmax(0, 1fr); gap: 11px; align-items: flex-start; }
                #page-help .help-emergency-icon { width: 46px; height: 46px; display: flex; align-items: center; justify-content: center; color: var(--help-blue); background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 13px; }
                #page-help .help-emergency-icon svg { width: 30px; height: 30px; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
                #page-help .help-contact-company { margin: 0 0 4px; color: #64748B; font-size: 11.7px; line-height: 1.5; font-weight: 650; }
                #page-help .help-phone-number { display: block; margin: 0 0 8px; color: #1E293B; text-decoration: none; font-size: 20px; line-height: 1.25; font-weight: 900; letter-spacing: .025em; pointer-events: none; }
                #page-help .help-contact-meta { margin: 0 0 8px; color: var(--help-muted); font-size: 11.8px; line-height: 1.6; font-weight: 600; }
                #page-help .help-notice-box { width: 100%; margin: 10px 0; padding: 10px 11px; border: 1px solid #F2D38B; border-left: 4px solid #F59E0B; border-radius: 11px; background: #FFF8E8; color: #6B4708; font-size: 11.6px; line-height: 1.65; font-weight: 700; box-shadow: none; }
                #page-help .help-contact-notice { margin-top: 8px; margin-bottom: 0; }
                #page-help .help-notice-box p { margin: 0 0 4px; }
                #page-help .help-notice-box p:last-child { margin-bottom: 0; }
                #page-help .help-notice-title { display: flex; align-items: center; gap: 5px; margin: 0 0 6px; color: #92400E; font-size: 11.8px; line-height: 1.45; font-weight: 900; }
                #page-help .help-notice-title i { font-size: 14px; }
                #page-help .help-note-list { margin: 0; padding-left: 18px; color: #6B4708; font-size: 11.6px; line-height: 1.66; font-weight: 700; }
                #page-help .help-note-list li { margin-bottom: 3px; }
                #page-help .help-note-list li:last-child { margin-bottom: 0; }
                #page-help .help-emergency-contact .help-notice-box { background: #FFF1F2; border-color: #FECDD3; border-left-color: #EF4444; color: #7F1D1D; }
                #page-help .help-emergency-contact .help-notice-title { color: #B91C1C; }
                #page-help .help-emergency-contact .help-note-list { color: #7F1D1D; }
                #page-help .help-action-btn { width: 100%; min-height: 50px; margin-top: 10px; padding: 12px 13px; display: flex; align-items: center; justify-content: center; gap: 8px; border-radius: 12px; text-decoration: none; font-size: 12.8px; line-height: 1.3; font-weight: 900; letter-spacing: .01em; -webkit-tap-highlight-color: transparent; transition: transform .16s ease, background-color .2s ease, box-shadow .2s ease; }
                #page-help .help-action-btn:active { transform: scale(.98); }
                #page-help .help-action-btn > i:first-child { flex: 0 0 auto; font-size: 18px; }
                #page-help .help-action-btn > span { min-width: 0; overflow-wrap: anywhere; }
                #page-help .help-action-btn > i:last-child { margin-left: auto; font-size: 13px; opacity: .78; }
                #page-help .help-web-btn, #page-help .help-phone-btn { color: var(--help-blue); background: #FFFFFF; border: 1px solid #9ECBF0; box-shadow: 0 3px 8px rgba(0, 91, 172, .055); }
                #page-help .help-web-btn:hover, #page-help .help-phone-btn:hover { background: #F4F9FF; }
                #page-help .help-emergency-btn { color: #FFFFFF; background: #C93D3D; border: 1px solid #B83232; box-shadow: 0 4px 10px rgba(197, 48, 48, .14); }
                #page-help .help-emergency-btn:hover { background: #B83232; }
                #page-help .help-emergency-row strong { color: #B83232; font-weight: 900; }

                /* 横スクロールステップUI */
                .step-outer-container-js { position: relative; width: 100%; display: flex; align-items: center; box-sizing: border-box; }
                .step-scroll-wrapper { display: flex; gap: 16px; overflow-x: auto; padding: 8px 4px 20px 4px; scroll-snap-type: x mandatory; -webkit-overflow-scrolling: touch; scrollbar-width: none; position: relative; width: 100%; box-sizing: border-box; }
                .step-scroll-wrapper::-webkit-scrollbar { display: none; }
                .step-premium-card { flex: 0 0 210px; background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 20px 16px; box-sizing: border-box; scroll-snap-align: start; position: relative; z-index: 2; box-shadow: 0 4px 12px rgba(0,0,0,0.02); text-align: left; display: flex; flex-direction: column; gap: 8px; }
                .step-card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
                .step-badge-node { font-size: 10px; font-weight: 900; color: #005bac; background: #EFF6FF; padding: 3px 10px; border-radius: 20px; letter-spacing: 0.5px; display: inline-block; }
                .step-icon-inline { font-size: 20px; color: #1E293B; display: flex; align-items: center; margin-top: 2px; }
                .step-premium-card .step-card-title { font-size: 14px !important; font-weight: 800 !important; color: #1E293B !important; line-height: 1.3; text-align: left; margin: 4px 0 2px 0; }

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

                .prohibit-group-box { border-radius: 14px; padding: 14px; margin-bottom: 14px; box-sizing: border-box; width: 100%; text-align: left; border: 2px solid #E2E8F0; }
                .prohibit-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 7px; }
                .prohibit-card-node { background: #FFFFFF; border-radius: 10px; padding: 8px 4px; min-height: 64px; border: 1px solid #CBD5E1; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); text-align: center; }
                .prohibit-card-node i { font-size: 20px; color: #EF4444; }
                .prohibit-card-lbl { font-size: 10.5px; font-weight: 800; color: #1E293B; line-height: 1.25; }
                .prohibit-guidance-box { margin-top: 10px; padding: 9px 10px; border-radius: 10px; border: 1px solid #FECACA; background: #FFFFFF; }
                .prohibit-guidance-title { display: flex; align-items: center; gap: 5px; margin: 0 0 5px 0; color: #9B2C2C; font-size: 11px; font-weight: 900; }
                .prohibit-guidance-list { margin: 0; padding-left: 16px; color: #475569; font-size: 10.5px; font-weight: 500; line-height: 1.55; }

                .bus-select-box { width: 100%; height: 44px; border: 2px solid #E2E8F0; border-radius: 8px; padding: 0 12px; font-size: 13px; color: #1E293B; outline: none; background-color: #FFFFFF; margin-bottom: 12px; font-weight: 700; box-sizing: border-box; }

                /* アメニティ */
                .amenity-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; width:100%; box-sizing:border-box; margin-bottom:12px; }
                .amenity-select-card { position:relative; width:100%; min-width:0; min-height:126px; padding:14px 10px 12px; border:1px solid #D8E3F0; border-radius:15px; background:linear-gradient(180deg,#FFFFFF 0%,#F8FBFF 100%); cursor:pointer; box-sizing:border-box; box-shadow:0 5px 14px rgba(0,31,77,.055); text-align:center; -webkit-tap-highlight-color:transparent; touch-action:manipulation; transition:transform .18s ease,border-color .2s ease,box-shadow .2s ease,background .2s ease; display:flex; flex-direction:column; align-items:center; justify-content:center; gap:10px; }
                .amenity-select-card:hover { transform:translateY(-3px); border-color:#B8D8F1; box-shadow:0 10px 22px rgba(0,31,77,.1); }
                .amenity-select-card.is-active { background:linear-gradient(180deg,#F4FAFF 0%,#EAF5FF 100%); border-color:#5DA0D7; box-shadow:0 9px 20px rgba(0,91,172,.12),0 0 0 3px rgba(93,182,255,.09); transform:translateY(-2px); }
                .amenity-line-icon-wrap { width:58px; height:58px; border-radius:17px; display:flex; align-items:center; justify-content:center; background:linear-gradient(145deg,#F4F9FF 0%,#E7F2FC 100%); border:1px solid #CFE3F5; color:#005BAC; }
                .amenity-line-icon { width:36px; height:36px; display:block; overflow:visible; }
                .amenity-line-icon * { fill:none; stroke:currentColor; stroke-width:2.15; stroke-linecap:round; stroke-linejoin:round; }
                .amenity-card-name { display:block; color:#17324F; font-size:12px; line-height:1.35; font-weight:900; }
                .amenity-detail-shell { display:grid; grid-template-rows:0fr; opacity:0; overflow:hidden; margin:0; transition:grid-template-rows .38s cubic-bezier(.2,.72,.2,1),opacity .22s ease,margin .38s ease; }
                .amenity-detail-shell.is-open { grid-template-rows:1fr; opacity:1; margin:2px 0 14px; }
                .amenity-detail-shell-inner { min-height:0; overflow:hidden; }
                .amenity-detail-card { background:linear-gradient(180deg,#FFFFFF 0%,#F7FBFF 100%); border:1px solid #BFDDF4; border-radius:15px; padding:15px; box-shadow:0 5px 14px rgba(0,91,172,.05); text-align:left; }
                .amenity-detail-header { display:flex; align-items:center; gap:9px; margin-bottom:9px; }
                .amenity-detail-icon { width:32px; height:32px; border-radius:10px; display:flex; align-items:center; justify-content:center; background:#EAF4FF; border:1px solid #CFE5F7; color:#005BAC; font-size:17px; flex-shrink:0; }
                .amenity-detail-title { color:#005BAC; font-size:13.5px; font-weight:900; }
                .amenity-detail-text { margin:0; color:#334155; font-size:12px; line-height:1.7; font-weight:600; }
                .amenity-detail-highlight { display:block; margin-top:11px; padding:10px 11px; background:#FFF9E8; border:1px solid #F3D98B; border-left:4px solid #E5B93E; border-radius:10px; color:#5A4A1E; font-size:11.5px; line-height:1.6; font-weight:750; }

                /* シートビュー */
                .seat-toggle-bar { display: flex; background: #F1F5F9; border-radius: 10px; padding: 4px; gap: 4px; margin-bottom: 16px; }
                .seat-toggle-btn { flex: 1; border: none; background: transparent; padding: 10px; font-size: 13px; font-weight: 800; color: #64748B; border-radius: 8px; cursor: pointer; }
                .seat-toggle-btn.active { background: #FFFFFF; color: #005bac; box-shadow: 0 2px 8px rgba(0,0,0,0.05); }
                .seat-toggle-main { display:block; font-size:12.5px; font-weight:900; }
                .seat-toggle-sub { display:block; font-size:10px; font-weight:800; opacity:.78; }
                .seat-guide-intro { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:14px; padding:10px 12px; margin:0 0 8px; color:#475569; font-size:11.5px; line-height:1.5; font-weight:650; text-align:left; }
                .seat-map-wrapper { position:relative; width:100%; max-width:358px; aspect-ratio:3/4; height:auto; border:1px solid rgba(0,91,172,.24); border-radius:20px; margin:0 auto; overflow:hidden; background:#001F4D; box-shadow:0 14px 30px rgba(0,31,77,.14); isolation:isolate; }
                .seat-photo-main { position:absolute; inset:0; width:100%; height:100%; object-fit:contain; object-position:center; opacity:0; transition:opacity .25s ease; z-index:1; }
                .view-seat3 .seat-photo-seat3 { opacity:1; }
                .view-seat4 .seat-photo-seat4 { opacity:1; }
                .seat-photo-chip { position:absolute; left:12px; top:12px; z-index:15; display:inline-flex; align-items:center; gap:5px; background:rgba(0,31,77,.82); color:#FFFFFF; border:1px solid rgba(255,255,255,.28); border-radius:999px; padding:7px 11px; font-size:11px; font-weight:900; }
                
                .hotspot-btn { position:absolute; width:44px; height:44px; border:none; background:transparent; color:#FFFFFF; border-radius:50%; cursor:pointer; z-index:30; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:900; line-height:1; transition:all .18s ease; -webkit-tap-highlight-color:transparent; touch-action:manipulation; }
                .hotspot-btn::after { content:''; position:absolute; left:50%; top:50%; width:20px; height:20px; border-radius:50%; border:1.3px solid rgba(255,255,255,.96); background:radial-gradient(circle at 32% 24%,#6ED0FF 0%,#1681D8 46%,#004A86 100%); box-shadow:0 5px 10px rgba(0,48,106,.25); transform:translate(-50%,-50%); z-index:1; }
                .hotspot-btn i { position:relative; z-index:2; font-size:10.5px; color:#FFFFFF; }
                .hotspot-btn.active::after { background:radial-gradient(circle at 32% 24%,#1A88D8 0%,#005BAC 52%,#003B72 100%); border:2px solid #F2C95B; }
                .seat-map-wrapper.view-seat3 .hotspot-btn { margin-left:-22px; margin-top:-22px; }
                .seat-map-wrapper.view-seat4 .hotspot-btn { margin-left:-22px; margin-top:-22px; }

                .seat-hotspot-info { display:none; width:100%; max-width:358px; margin:10px auto 0; box-sizing:border-box; text-align:left; background:linear-gradient(180deg,#FFFFFF 0%,#FBFDFF 100%); border:1px solid #D8E3F0; border-radius:16px; padding:13px 14px; box-shadow:0 6px 16px rgba(0,91,172,.055); }
                .seat-hotspot-info.show { display:block; }
                .seat-hotspot-info-title { margin:0 0 6px; color:#003B72; font-size:14px; font-weight:900; }
                .seat-hotspot-info-desc { margin:0; color:#334155; font-size:12.2px; line-height:1.62; font-weight:650; }
                .seat-hotspot-info-extra { display:none; margin-top:10px; padding-top:10px; border-top:1px solid #E4EEF8; color:#475569; font-size:11.8px; line-height:1.55; }

                /* モーダル */
                .modal-mask { position: absolute !important; top: 0; left: 0 !important; width: 100% !important; height: 100vh; background: rgba(15,23,42,0.6) !important; display: none; align-items: center; justify-content: center; padding: 16px; box-sizing: border-box; z-index: 999999 !important; }
                .modal-mask.show { display: flex !important; }
                .modal-box { width: 100%; max-width: 390px; background: #FFFFFF; border-radius: 20px; padding: 22px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); display: flex; flex-direction: column; max-height: 88vh; box-sizing: border-box; }
                .modal-top { font-size: 15px; font-weight: 800; color: #005bac; margin-bottom: 12px; border-bottom: 1px solid #E2E8F0; padding-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
                .modal-close-icon { cursor: pointer; color: #64748B; font-size: 20px; }
                .modal-scroll { overflow-y: auto; padding-right: 2px; }

                .floating-top-btn { position: fixed !important; bottom: calc(20px + env(safe-area-inset-bottom, 0px)) !important; right: calc(20px + env(safe-area-inset-right, 0px)) !important; width: 50px !important; height: 50px !important; border-radius: 25px !important; background: #005bac !important; color: white !important; display: flex !important; flex-direction: column !important; align-items: center !important; justify-content: center !important; box-shadow: 0 4px 16px rgba(0,0,0,0.2) !important; cursor: pointer !important; z-index: 9999 !important; border: none !important; }
                .floating-top-btn i { font-size: 16px; margin-bottom: 2px; }
                .floating-top-btn span { font-size: 8.5px; font-weight: 900; }
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

                        <div class="category-card card-red page-trigger" data-target="page-help">
                            <div class="card-icon-box bg-red"><i class="ph-bold ph-question"></i></div>
                            <div class="card-main-text">
                                <span class="card-title">困ったときは（FAQ）</span>
                                <p class="card-subtitle">緊急時の対応やお問い合わせ先をご確認いただけます。</p>
                            </div>
                            <div class="card-chevron"><i class="ph-bold ph-caret-right"></i></div>
                        </div>
                    </div>

                    <!-- 1. 乗車前の準備 -->
                    <div id="page-prep" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ 乗車前の準備</span>
                        </div>
                        <div class="heading">最重要｜モバイルバッテリー・リチウムイオン電池製品について</div>
                        <div class="ud-status-box ud-box-danger" style="background:#FFFFFF;">
                            <div class="ud-sign-header"><span class="ud-sign-header-icon"><i class="ph-bold ph-warning"></i></span><span>必ず車内へお持ち込みください</span></div>
                            <p style="font-size:11.5px; color:#475569; font-weight:600; margin:0 0 14px 0; line-height:1.6;">モバイルバッテリーなどのリチウムイオン電池製品は、必ず車内へお持ち込みください。発火防止のため、トランクへのお預けは禁止しています。</p>
                            <div class="ud-grid">
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-battery-charging"></i></div><div class="ud-item-label"><span class="ud-main-lbl">モバイルバッテリー</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-device-mobile"></i></div><div class="ud-item-label"><span class="ud-main-lbl">スマートフォン</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-laptop"></i></div><div class="ud-item-label"><span class="ud-main-lbl">ノートPC</span></div></div>
                                <div class="ud-item"><div class="ud-icon-large"><i class="ph-bold ph-fan"></i></div><div class="ud-item-label"><span class="ud-main-lbl">携帯扇風機</span></div></div>
                            </div>
                        </div>
                    </div>

                    <!-- 2. 当日の流れ -->
                    <div id="page-today" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ 当日の流れ・のりば</span>
                        </div>
                        <div class="heading">乗車場所・降車場所のご案内</div>
                        <div class="info-card today-notice-card">
                            <p class="info-text today-notice-label"><i class="ph-bold ph-warning-circle"></i>ご乗車前にご確認ください</p>
                            <div class="today-priority-row">
                                <span class="today-priority-icon"><i class="ph-bold ph-clock-countdown"></i></span>
                                <span><span class="today-priority-kicker">集合時間</span><strong class="today-priority-main">出発10分前です</strong></span>
                            </div>
                        </div>
                    </div>

                    <!-- 3. シートの使い方 -->
                    <div id="page-recline" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ シートの使い方・設備</span>
                        </div>
                        <div class="heading">シートについて</div>
                        <div class="seat-toggle-bar">
                            <button class="seat-toggle-btn active" id="js-btn-seat3"><span class="seat-toggle-main">3列独立シート</span><span class="seat-toggle-sub">トイレ付</span></button>
                            <button class="seat-toggle-btn" id="js-btn-seat4"><span class="seat-toggle-main">4列シート</span><span class="seat-toggle-sub">スタンダード</span></button>
                        </div>
                        
                        <div class="seat-map-wrapper view-seat3" id="seat-canvas-container">
                            <img class="seat-photo-main seat-photo-seat3" src="__SEAT3_PHOTO__" alt="3列独立シート全景">
                            <img class="seat-photo-main seat-photo-seat4" src="__SEAT4_PHOTO__" alt="4列シート全景">
                            <div class="seat-photo-chip" id="js-seat-photo-label">3列独立シート 設備ガイド</div>

                            <div class="hotspot-btn" id="pin-luggage" data-key="luggage"><i class="ph-bold ph-bag"></i></div>
                            <div class="hotspot-btn" id="pin-overhead" data-key="overhead"><i class="ph-bold ph-lightbulb"></i></div>
                            <div class="hotspot-btn" id="pin-recline" data-key="recline"><i class="ph-bold ph-arrow-counter-clockwise"></i></div>
                        </div>

                        <div class="seat-hotspot-info" id="js-seat-hotspot-info">
                            <div class="seat-hotspot-info-title" id="js-seat-info-title"></div>
                            <p class="seat-hotspot-info-desc" id="js-seat-info-desc"></p>
                        </div>
                    </div>

                    <!-- 4. 車内のご利用案内 -->
                    <div id="page-manner" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ 車内のご利用案内</span>
                        </div>
                        <div class="manner-accordion-list">
                            <div class="simple-accordion manner-main-accordion">
                                <div class="accordion-header"><span class="manner-main-title">シートベルトについて</span><span class="accordion-arrow">▶</span></div>
                                <div class="accordion-content"><p class="manner-copy">法律により、全席で着用が義務付けられています。</p></div>
                            </div>
                        </div>
                    </div>

                    <!-- 5. 困ったときは -->
                    <div id="page-help" class="page-view">
                        <div class="breadcrumb-bar">
                            <span class="breadcrumb-back back-to-home-trigger"><i class="ph-bold ph-caret-left"></i> ホーム</span>
                            <span class="breadcrumb-current">/ 困ったときは</span>
                        </div>
                        <div class="help-accordion-list">
                            <div class="simple-accordion help-main-accordion">
                                <div class="accordion-header"><span class="help-main-title">体調が優れない場合</span><span class="accordion-arrow">▶</span></div>
                                <div class="accordion-content"><p class="help-copy">乗車中に気分が悪くなられた場合は、お早めに乗務員へお知らせください。</p></div>
                            </div>
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

                    document.querySelectorAll('.simple-accordion').forEach(acc => {
                        const header = acc.querySelector('.accordion-header');
                        if (header) {
                            header.addEventListener('click', function() {
                                acc.classList.toggle('open');
                            });
                        }
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

                    const floatTopBtn = document.getElementById('js-float-top');
                    if (floatTopBtn) {
                        floatTopBtn.addEventListener('click', function() { window.scrollTo(0, 0); });
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
