import os
import sys

# Core Architectural Fix: Enforce project root injection into Python search path
# This strictly resolves the Streamlit Cloud Linux relative import pipeline exceptions
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

# Core Architectural Imports from the purged baseline modules
from core.state_manager import initialize_session_state
from core.router import render_active_view, navigate_to
from utils.localization import get_text
from components.header import render_header

def main():
    """
    Main Executive Entrypoint for the Iraqi Green Construction Data Platform.
    Strictly follows the platform design rules:
    - 100% Pure Standard English keys passed to get_text()
    - Direct integration with core/router.py to enforce absolute separation of concerns
    - Premium light-theme high-contrast visualization elements (#0F172A navy elements)
    """
    
    # 1. Initialize global state variables (language management and session locking)
    initialize_session_state()
    
    # 2. Render Global Sovereign Top Header & Identity Navigation component
    render_header()
    
    # 3. Custom Sidebar Styling Injection to guarantee clean light contrast and borders
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"] {
            background-color: #FFFFFF !important;
            border-right: 1px solid #E2E8F0 !important;
        }
        .sidebar-title {
            color: #0F172A;
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #F1F5F9;
        }
        div.stButton > button {
            width: 100% !important;
            text-align: left !important;
            margin-bottom: 4px !important;
            border-radius: 8px !important;
            font-size: 13px !important;
            font-weight: 600 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 4. Construct the Sovereign Sidebar Platform Navigation Control Panel
    with st.sidebar:
        st.markdown(f'<div class="sidebar-title">📌 {get_text("Platform Navigation")}</div>', unsafe_allow_html=True)
        
        # Reference mapping matrix matching the router engine keys exactly (Pure English Keys)
        navigation_map = [
            ("Main Dashboard", "📊 "),
            ("Portal 1: Base Compliance", "🧱 "),
            ("Portal 2: Sustainability", "🌱 "),
            ("Portal 3: Data Aggregator", "📈 "),
            ("Portal 4: GIS Spatial Map", "🗺️ "),
            ("Portal 5: Sustainable Infrastructure", "🏗️ "),
            ("Portal 6: Site Safety", "🛡️ ")
        ]
        
        # Render high-contrast programmatic button array for seamless transition logs
        for page_key, icon_prefix in navigation_map:
            # Highlight current active page dynamically for enhanced UX visibility
            is_active = st.session_state.current_page == page_key
            button_label = f"{icon_prefix}{get_text(page_key)}"
            
            if st.button(
                label=button_label, 
                key=f"nav_btn_{page_key.replace(' ', '_').lower()}",
                type="primary" if is_active else "secondary"
            ):
                navigate_to(page_key)
                
    # 5. Delegate structural view rendering exclusively to the isolated routing module
    render_active_view()

if __name__ == "__main__":
    main()
