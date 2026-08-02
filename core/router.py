import streamlit as st
from utils.localization import get_text

# Dynamic extraction of isolated baseline views
from views.main_dashboard import render_main_dashboard
from views.portal_1_compliance import render_portal_1_compliance
from views.portal_2_sustainability import render_portal_2_sustainability
from views.portal_3_aggregator import render_portal_3_aggregator
from views.portal_4_gis_map import render_portal_4_gis_map
from views.portal_5_infrastructure import render_portal_5_infrastructure
from views.portal_6_site_safety import render_portal_6_site_safety

def initialize_router_state():
    """Ensures page session tokens are locked on initialization context."""
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Main Dashboard"

def navigate_to(page_key: str):
    """Executes state-driven instantaneous session rewrites."""
    st.session_state.current_page = page_key
    st.rerun()

def render_dynamic_input_canvas():
    """
    Internal dynamic lookup router that checks session status 
    and injects the correct input portal inside the layout.
    """
    active_page = st.session_state.current_page
    
    if active_page == "Main Dashboard" or active_page == "Portal 1: Base Compliance":
        render_portal_1_compliance()
    elif active_page == "Portal 2: Sustainability":
        render_portal_2_sustainability()
    elif active_page == "Portal 3: Data Aggregator":
        render_portal_3_aggregator()
    elif active_page == "Portal 4: GIS Spatial Map":
        render_portal_4_gis_map()
    elif active_page == "Portal 5: Sustainable Infrastructure":
        render_portal_5_infrastructure()
    elif active_page == "Portal 6: Site Safety":
        render_portal_6_site_safety()

def render_sovereign_split_layout():
    """
    Core Architecture Orchestrator. 
    Handles splitting the view grid cleanly into a 40% Telemetry Monitor 
    and 60% Input Canvas, decoupling app.py entirely from view logic.
    """
    initialize_router_state()
    
    # Executing the exact standard Streamlit multi-columns split matrix (40% vs 60%)
    col_live_telemetry, col_input_canvas = st.columns([4.0, 6.0], gap="large")
    
    # LEFT PANEL FRAME (40%): Live persistent dashboard tracking
    with col_live_telemetry:
        render_main_dashboard()
        
    # RIGHT PANEL FRAME (60%): Dynamically injected active forms canvas
    with col_input_canvas:
        render_dynamic_input_canvas()
