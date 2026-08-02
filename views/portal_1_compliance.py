import streamlit as st
from utils.localization import get_text
from engines.code_compliance import evaluate_code_compliance_matrix
from core.state_manager import log_action

def render_portal_1_compliance():
    """
    Portal 1: Site Analysis & Municipal Constraints.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Filename matching structural blueprint: views/portal_1_compliance.py
    - 13 Blanks initialized with empty string options and 0.0 metrics [1.1]
    - Direct integration with verified evaluate_code_compliance_matrix engine [1.1]
    """
    
    # Custom light theme high-contrast injection for layout alignment
    st.markdown(
        """
        <style>
        .portal-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            border: 1px solid #E2E8F0;
            margin-bottom: 24px;
        }
        .portal-title { color: #0F172A; font-size: 24px; font-weight: 700; margin-bottom: 8px; }
        .portal-desc { color: #475569; font-size: 14px; margin-bottom: 20px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sovereign Top Banner Card
    st.markdown(
        f'''
        <div class="portal-card">
            <div class="portal-title">{get_text("Portal 1: Site Analysis & Municipal Constraints")}</div>
            <div class="portal-desc">{get_text("Please fill out the 13 fields accurately to determine soil test and mandatory national building codes.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )
    
    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_1_compliance_form"):
        st.subheader(get_text("Geographic & Administrative Data"))
        
        c1, c2, c3 = st.columns(3)
        with c1:
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

        st.markdown("<hr style='border-color: #E2E8F0; margin: 20px 0;'>", unsafe_allow_html=True)
        st.subheader(get_text("Structural Constraints & Building Mass"))
        
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
        submit_btn = st.form_submit_button(label=get_text("Trigger Instant Compliance Engine"))
        
        if submit_btn:
            # Rigid baseline barrier checklist checking critical variables against blank uninitialized entries [1.1]
            if not gov or not district or not zoning or total_area == 0.0 or floors == 0 or building_height == 0.0:
                st.warning(get_text("Submission Rejected: All primary building metrics and location constraints must exceed 0.0 values."))
            else:
                # Save sanitized inputs to sovereign session state configuration variables
                st.session_state.property_data["governorate"] = gov
                st.session_state.property_data["district"] = district
                st.session_state.property_data["zoning_type"] = zoning
                st.session_state.property_data["built_area"] = built_area
                st.session_state.property_data["floors"] = floors
                
                # Bundle localized metric inputs array to pass to the updated compliance evaluator module
                input_payload = {
                    "total_area": total_area,
                    "built_area": built_area,
                    "floors": floors,
                    "building_height": building_height,
                    "front_offset": front_offset,
                    "side_offset": side_offset
                }
                
                # Dynamic compliance parsing calculation block
                result_report = evaluate_code_compliance_matrix(portal_data_payload=input_payload)
                st.session_state.property_data["is_compliant"] = result_report["is_compliant"]
                
                st.markdown("<br><hr style='border-color: #E2E8F0;'>", unsafe_allow_html=True)
                
                # Evaluate response status dictionary tags to render high-contrast telemetry notifications
                if result_report["is_compliant"]:
                    st.success(result_report["audit_summary_message"])
                    st.info(f"{get_text('National Sustainable Evaluation Score:')} {result_report['compliance_rating_percentage']}%")
                else:
                    st.error(result_report["audit_summary_message"])
                
                # Direct call to sovereign log pipeline interceptor
                log_action(
                    user_credential=st.session_state.user_identity.get("full_name", "Anonymous Operative"), 
                    action_details=f"Triggered Portal 1 municipal constraints audit for {gov}. Status: {result_report['legislative_status_token']}"
                )
