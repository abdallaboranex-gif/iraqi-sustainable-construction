import streamlit as st
from utils.localization import get_text

from views.main_dashboard import render_main_dashboard
from views.portal_1_compliance import render_portal_1_compliance
from views.portal_2_sustainability import render_portal_2_sustainability
from views.portal_3_aggregator import render_portal_3_aggregator
from views.portal_4_gis_map import render_portal_4_gis_map
from views.portal_5_infrastructure import render_portal_5_infrastructure
from views.portal_6_site_safety import render_portal_6_site_safety

def initialize_router_state():
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Main Dashboard"

def navigate_to(page_key: str):
    st.session_state.current_page = page_key
    st.rerun()

def render_active_view():
    initialize_router_state()
    active_page = st.session_state.current_page

    if active_page == "Main Dashboard":
        render_main_dashboard()
    elif active_page == "Portal 1: Base Compliance":
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
    else:
        st.error(get_text("Routing Exception: Selected view token is unrecognized by the platform controller."))
        if st.button(get_text("Reset to Main Dashboard")):
            navigate_to("Main Dashboard")
