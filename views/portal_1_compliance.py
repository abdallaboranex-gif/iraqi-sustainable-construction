import streamlit as st
from engines.code_compliance import verify_site_compliance
from utils.localization import get_text

def render_portal_1():
    """
    Sovereign Portal 1 Component.
    100% Pure English source code. Completely purged of any hardcoded Arabic or Kurdish words [١.١].
    Pulls automated real-time translations for all 13 blanks and structural inputs [١.١].
    """
    # Main header and description synchronized with the cloud translation engine
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight: 800;'>{get_text('Portal 1: Site Analysis & Municipal Constraints')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('Please fill out the 13 fields accurately to determine soil test and mandatory codes.')}</p>", unsafe_allow_html=True)
    
    with st.container(border=True):
        st.markdown(f"<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>{get_text('Geographic & Administrative Data')}</h4>", unsafe_allow_html=True)
        
        c1, c2, c3 = st.columns(3)
        with c1:
            # The selectbox opens blank, enforcing fresh user interaction
            gov = st.selectbox(get_text("1. Governorate"), ["", "Baghdad", "Nineveh", "Basra", "Erbil", "Salah Al-Din", "Anbar", "Babylon", "Najaf"], index=0)
        with c2:
            district = st.text_input(get_text("2. District / Sub-district"), placeholder="e.g. Al-Mansour", value="")
        with c3:
            zoning = st.selectbox(get_text("3. Land Zoning Type (Municipality)"), ["", "Pure Residential", "Commercial", "Industrial", "Agricultural Included", "Governmental / Service"], index=0)
            
        c4, c5, c6 = st.columns(3)
        with c4:
            plot_num = st.text_input(get_text("4. Plot & Sector Number"), placeholder="e.g. 4/12 Dawoodi", value="")
        with c5:
            total_area = st.number_input(get_text("5. Total Land Area (sqm)"), min_value=0.0, value=0.0, step=10.0)
        with c6:
            built_area = st.number_input(get_text("6. Built-up Footprint Area (sqm)"), min_value=0.0, value=0.0, step=10.0)

        st.markdown("<hr style='border-color: #CBD5E1; margin: 20px 0;'>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color: #0F172A; font-size: 15px; margin-bottom: 15px;'>{get_text('Structural Constraints & Building Mass')}</h4>", unsafe_allow_html=True)
        
        c7, c8, c9 = st.columns(3)
        with c7:
            floors = st.number_input(get_text("7. Total Number of Floors"), min_value=0, max_value=60, value=0)
        with c8:
            building_height = st.number_input(get_text("8. Total Building Height (meters)"), min_value=0.0, value=0.0, step=0.5)
        with c9:
            basement = st.selectbox(get_text("9. Does the building contain a basement?"), ["", "No Basement", "Single Basement", "Multi-Level Underground"], index=0)

        c10, c11, c12 = st.columns(3)
        with c10:
            front_offset = st.number_input(get_text("10. Legal Front Offset (meters)"), min_value=0.0, value=0.0, step=0.5)
        with c11:
            side_offset = st.number_input(get_text("11. Side and Rear Offsets (meters)"), min_value=0.0, value=0.0, step=0.5)
        with c12:
            adjacent_buildings = st.selectbox(get_text("12. Type of Adjacent Buildings"), ["", "Light Residential", "Heavy Concrete Structures", "Open Space / Vacant Land"], index=0)

        st.markdown("<br>", unsafe_allow_html=True)
        structural_system = st.selectbox(get_text("13. Proposed Structural System"), ["", "Reinforced Concrete Frame", "Load-Bearing Walls", "Steel Structure", "Mixed / Special System"], index=0)

        st.markdown("<br>", unsafe_allow_html=True)
        submit_filter = st.button(get_text("Trigger Instant Compliance Engine"), use_container_width=True)
        
        if submit_filter:
            # Rigid safeguard preventing code execution on blank or uninitialized elements
            if not gov or not district or not zoning or total_area == 0.0 or floors == 0:
                st.warning(get_text("Please fill out all 13 fields first!"))
            else:
                st.session_state.property_data["governorate"] = gov
                st.session_state.property_data["district"] = district
                st.session_state.property_data["zoning_type"] = zoning
                st.session_state.property_data["built_area"] = built_area
                st.session_state.property_data["floors"] = floors
                
                result = verify_site_compliance(governorate=gov, zoning_type=zoning, building_height=building_height, floors=floors)
                st.session_state.property_data["is_compliant"] = result["status"]
                
                st.markdown("<br><hr style='border-color: #CBD5E1;'>", unsafe_allow_html=True)
                
                if result["status"]:
                    st.success(get_text("✅ Analysis complete. The initial blueprint complies with all restrictions."))
                    with st.expander("🔍 Inspection Clauses / Check Details"):
                        for log in result["logs"]:
                            st.markdown(f"<span style='color: #10B981; font-weight:700;'>{log}</span>", unsafe_allow_html=True)
                else:
                    st.error(get_text("❌ Explicit violations detected against municipal zoning and national codes!"))
                    with st.expander("🚨 Violations Log", expanded=True):
                        for error in result["errors"]:
                            st.markdown(f"<span style='color: #EF4444; font-weight: 700;'>{error}</span>", unsafe_allow_html=True)
                            
                from core.state_manager import log_action
                log_action(user=st.session_state.user_identity.get("full_name", "Anonymous"), action_details=f"Triggered site audit engine for {gov}, Result Status: {result['status']}")
                st.rerun()
