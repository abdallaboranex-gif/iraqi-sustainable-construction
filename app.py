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
    - Dynamic injection of ultra-modern, high-contrast dark navy typography & Remix Icons
    """
    
    # 1. Initialize global state variables (language management and session locking)
    initialize_session_state()
    
    # 2. Render Global Sovereign Top Header & Digital ID sidebar
    render_header()
    
    # 3. Inject Remix Icon CDN and premium dark-contrast sidebar typography styles
    st.markdown(
        """
        <!-- Load modern pixel-perfect icons family -->
        <link href="https://jsdelivr.net" rel="stylesheet">
        
        <style>
        /* Force high-contrast dark navy black style across text fields */
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
            font-size: 18px;
            font-weight: 800;
            margin-bottom: 24px;
            padding-bottom: 12px;
            border-bottom: 2px solid #F1F5F9;
        }
        
        /* Modern Button Facelift - Darker Typography & Premium Interaction Dynamics */
        div.stButton > button {
            width: 100% !important;
            text-align: left !important;
            margin-bottom: 6px !important;
            border-radius: 10px !important;
            padding: 10px 14px !important;
            font-size: 14px !important;
            font-weight: 700 !important; /* Thick sharp elements */
            color: #0F172A !important; /* Deepest High-Contrast Navy */
            border: 1px solid #E2E8F0 !important;
            background-color: #F8FAFC !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        /* Hover properties for active states */
        div.stButton > button:hover {
            border-color: #1D4ED8 !important;
            background-color: #EFF6FF !important;
            color: #1D4ED8 !important;
            transform: translateX(2px);
        }
        
        /* Smooth visual identifier for the actively selected viewport page */
        div.stButton button[p_is_active="true"], 
        div.stButton > button:active,
        div.stButton > button:focus {
            background-color: #0F172A !important; /* Premium Dark Sovereign Navy background */
            color: #FFFFFF !important; /* Crisp high contrast white text */
            border-color: #0F172A !important;
            box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.15) !important;
        }
        
        /* Helper utility to handle inline alignment of icons next to text elements */
        .nav-link-wrapper {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .nav-link-wrapper i {
            font-size: 18px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 4. Construct the Sovereign Sidebar Platform Navigation Control Panel
    with st.sidebar:
        st.markdown(f'<div class="sidebar-title"><i class="ri-compass-3-fill"></i> {get_text("Platform Navigation")}</div>', unsafe_allow_html=True)
        
        # Mapping matrix matching the router keys exactly, upgraded with slick 2026 Remix Icons
        navigation_map = [
            ("Main Dashboard", "ri-dashboard-3-line"),
            ("Portal 1: Base Compliance", "ri-building-4-line"),
            ("Portal 2: Sustainability", "ri-leaf-line"),
            ("Portal 3: Data Aggregator", "ri-bar-chart-box-line"),
            ("Portal 4: GIS Spatial Map", "ri-map-pin-range-line"),
            ("Portal 5: Sustainable Infrastructure", "ri-tools-line"),
            ("Portal 6: Site Safety", "ri-shield-cross-line")
        ]
        
        # Render high-contrast programmatic button array for seamless transition logs
        for page_key, icon_class in navigation_map:
            is_active = st.session_state.current_page == page_key
            
            # Construct a pixel-perfect HTML anchor structure inside the button label
            button_label = f'<span class="nav-link-wrapper"><i class="{icon_class}"></i> {get_text(page_key)}</span>'
            
            if st.button(
                label=button_label, 
                key=f"nav_btn_{page_key.replace(' ', '_').lower()}",
                # Passing secondary type to control state dynamically via custom CSS injection rules
                type="secondary"
            ):
                navigate_to(page_key)
                
    # 5. Delegate structural view rendering exclusively to the isolated routing module
    render_active_view()

if __name__ == "__main__":
    main()
