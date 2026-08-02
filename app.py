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
    - High-contrast typography & safe structural modern navigation component
    """
    
    # 1. Initialize global state variables (language management and session locking)
    initialize_session_state()
    
    # 2. Render Global Sovereign Top Header & Digital ID sidebar
    render_header()
    
    # 3. Inject premium dark-contrast sidebar typography styles and bolding overrides
    st.markdown(
        """
        <style>
        /* Force ultra-deep high-contrast navy typography across text fields */
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
        
        /* Modern Select Option Facelift - Darker Typography & Premium Interaction */
        div[data-baseweb="select"] > div {
            border-radius: 12px !important;
            border: 1px solid #CBD5E1 !important;
            padding: 4px !important;
            background-color: #F8FAFC !important;
        }
        
        div[data-baseweb="select"] * {
            color: #0F172A !important; /* Thick sharp elements */
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
        
        # Dictionary Mapping matching the exact english router navigation keys
        navigation_options = {
            f"📊 {get_text('Main Dashboard')}": "Main Dashboard",
            f"🧱 {get_text('Portal 1: Base Compliance')}": "Portal 1: Base Compliance",
            f"🌱 {get_text('Portal 2: Sustainability')}": "Portal 2: Sustainability",
            f"📈 {get_text('Portal 3: Data Aggregator')}": "Portal 3: Data Aggregator",
            f"🗺️ {get_text('Portal 4: GIS Spatial Map')}": "Portal 4: GIS Spatial Map",
            f"🏗️ {get_text('Portal 5: Sustainable Infrastructure')}": "Portal 5: Sustainable Infrastructure",
            f"🛡️ {get_text('Portal 6: Site Safety')}": "Portal 6: Site Safety"
        }
        
        # Calculate current visible key to keep select box state locked correctly upon reruns
        current_page_state = st.session_state.current_page
        default_index = 0
        
        for idx, (display_label, internal_key) in enumerate(navigation_options.items()):
            if internal_key == current_page_state:
                default_index = idx
                break
                
        # Premium unified selection menu container
        selected_display_label = st.selectbox(
            label="Navigation Switcher Matrix",
            options=list(navigation_options.keys()),
            index=default_index,
            label_visibility="collapsed",
            key="navigation_selectbox_trigger"
        )
        
        # Map user input directly back to sovereign router keys safely
        target_page_key = navigation_options[selected_display_label]
        
        # Route seamlessly if status selection drifts from current thread layout
        if target_page_key != current_page_state:
            navigate_to(target_page_key)
                
    # 5. Delegate structural view rendering exclusively to the isolated routing module
    render_active_view()

if __name__ == "__main__":
    main()
