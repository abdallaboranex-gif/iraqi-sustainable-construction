import streamlit as st

# 1. Page Configuration for Wide Layout
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Premium CSS Injection for Light Theme and High-Contrast Typography
st.markdown(
    """
    <link rel="preconnect" href="https://googleapis.com">
    <link rel="preconnect" href="https://gstatic.com" crossorigin>
    <link href="https://googleapis.com/css2?family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
    
    <style>
        /* Global Background and Typography Sync */
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F1F5F9 !important;
            font-family: 'Tajawal', sans-serif !important;
        }
        
        /* Dark Navy Typography for Maximum Readability */
        p, span, label, .stMarkdown, [data-testid="stWidgetLabel"] p {
            font-family: 'Tajawal', sans-serif !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            color: #0F172A !important;
        }
        
        /* Deep Bold Titles and Accents */
        h1, h2, h3, h4, strong {
            font-family: 'Tajawal', sans-serif !important;
            color: #020617 !important;
            font-weight: 800 !important;
        }
        
        /* Container Cards Styling with Smooth Shadow */
        [data-testid="stElementContainer"] > div[data-testid="stVerticalBlockBorderContainer"] {
            border: 1px solid #CBD5E1 !important;
            border-radius: 16px !important;
            background-color: #FFFFFF !important;
            box-shadow: 0 10px 15px -3px rgba(148, 163, 184, 0.12) !important;
            padding: 22px !important;
            margin-bottom: 15px !important;
        }
        
        /* Portal Navigation Buttons Premium Styling */
        .stButton > button {
            border-radius: 10px !important;
            border: 1px solid #94A3B8 !important;
            padding: 12px 18px !important;
            font-size: 15px !important;
            font-weight: 800 !important;
            background-color: #FFFFFF !important;
            color: #0F172A !important;
            transition: all 0.25s ease !important;
        }
        
        /* High Contrast Royal Blue for Active States */
        .stButton > button[data-testid="baseButton-primary"] {
            background-color: #1D4ED8 !important;
            color: #FFFFFF !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# 3. Core Framework Imports and Automated Localization Pipeline Ingestion
from core.state_manager import init_session_state
from core.router import route_to_view
from components.header import render_header
from components.footer import render_footer
from components.analytics_cards import render_side_analytics
from utils.localization import get_text

# 4. Initialize Core Session Parameters
init_session_state()

# 5. Execute Sovereign Header (Includes Logo, Location Frame, and Language Selector)
render_header()

st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 6. Navigation Interface Section (100% Pure English source strings mapped to Translation Engine)
st.markdown(f"<h4 style='color: #0F172A; font-size: 17px !important; margin-bottom: 12px; font-weight:800;'>{get_text('Sovereign Control Panel')}</h4>", unsafe_allow_html=True)

nav_cols = st.columns(6)
portals_titles = [
    get_text("Portal 1: Site Analysis & Municipal Constraints"),
    get_text("Portal 2: Energy & Green Score"),
    get_text("Portal 3: Central Materials BOQ"),
    get_text("Portal 4: Iraq GIS Map View"),
    get_text("Portal 5: Finance & Payback"),
    get_text("Portal 6: Field Site Safety")
]

for idx, col in enumerate(nav_cols):
    portal_num = idx + 1
    is_active = st.session_state.current_portal == portal_num
    
    with col:
        if st.button(
            portals_titles[idx], 
            key=f"nav_btn_{portal_num}", 
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.current_portal = portal_num
            st.rerun()

st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 7. Split Central Screen Layout Into Parallel Functional Columns
col_main, col_side = st.columns([2.8, 1.2], gap="large")

with col_main:
    route_to_view()

with col_side:
    render_side_analytics()

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #CBD5E1; margin: 15px 0;'>", unsafe_allow_html=True)

# 8. Render Global Standard Framework Footer
render_footer()
