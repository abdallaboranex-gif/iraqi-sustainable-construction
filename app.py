import os
import sys

# Core Architectural Fix: Enforce project root injection into Python search path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import streamlit as st

# Enforce Sovereign Layout Configuration at the absolute application execution entrypoint
st.set_page_config(
    page_title="Iraqi Green Construction Data Platform",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Core Architectural Imports from the centralized system controllers
from core.state_manager import initialize_session_state
from core.router import render_sovereign_split_layout, navigate_to
from utils.localization import get_text
from components.header import render_header

def main():
    """
    Main Executive Entrypoint for the Iraqi Green Construction Data Platform.
    Strictly cleaned and decoupled. Delegates 100% of spatial rendering 
    and views distribution to core/router.py.
    """
    
    # 1. Initialize global state variables (language management and session locking)
    initialize_session_state()
    
    # 2. Render Global Sovereign Top Header & Digital ID sidebar
    render_header()
    
    # 3. Inject premium dark-contrast sidebar typography styles
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: #0F172A !important;
            font-weight: 800 !important;
        }
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        .sidebar-title {
            color: #0F172A !important;
            font-size: 19px;
            font-weight: 800;
            margin-bottom: 20px;
            padding-bottom: 12px;
            border-bottom: 2px solid #F1F5F9;
        }
        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
            padding: 4px !important;
            background-color: #F8FAFC !important;
        }
        div[data-baseweb="select"] * {
            color: #0F172A !important;
            font-weight: 700 !important;
            font-size: 14px !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 4. Construct the Sovereign Sidebar Platform Navigation Control Panel
    with st.sidebar:
        st.markdown(f'<div class="sidebar-title">🧭 {get_text("Platform Navigation")}</div>', unsafe_allow_html=True)
        
        # Mapping matrix for localized options matching centralized localization dictionary
        navigation_options = {
            f"📊 {get_text('Main Dashboard')}": "Main Dashboard",
            f"🧱 {get_text('Compliance Audits')}": "Portal 1: Base Compliance",
            f"🌱 {get_text('Energy Management')}": "Portal 2: Sustainability",
            f"📈 {get_text('Data Center')}": "Portal 3: Data Aggregator",
            f"🗺️ {get_text('Telemetry Indicators')}": "Portal 4: GIS Spatial Map",
            f"🏗️ {get_text('Digital Payments')}": "Portal 5: Sustainable Infrastructure",
            f"🛡️ {get_text('Site Safety')}": "Portal 6: Site Safety"
        }
        
        current_page_state = st.session_state.current_page
        default_index = 0
        
        for idx, (display_label, internal_key) in enumerate(navigation_options.items()):
            if internal_key == current_page_state:
                default_index = idx
                break
                
        selected_display_label = st.selectbox(
            label="Navigation Switcher Matrix",
            options=list(navigation_options.keys()),
            index=default_index,
            label_visibility="collapsed",
            key="navigation_selectbox_trigger"
        )
        
        target_page_key = navigation_options[selected_display_label]
        
        if target_page_key != current_page_state:
            navigate_to(target_page_key)
                
    st.markdown("<br>", unsafe_allow_html=True)

    # 5. DELEGATE SPLIT EXECUTION ENTIRELY TO THE ROUTER (Absolute Separation of Concerns)
    render_sovereign_split_layout()

if __name__ == "__main__":
    main()
