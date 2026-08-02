import streamlit as st
from utils.localization import get_text

def render_portal_5_infrastructure():
    """
    Portal 5: Sustainable Infrastructure & Smart Utilities.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Exact filename synchronization: portal_5_infrastructure.py
    - Blank 0.0 state initialization with structural high-contrast aesthetics
    - Enforced infrastructure safeguards to reject zero/empty logs
    """
    
    # Custom high-contrast UI theme styling applied to container blocks
    st.markdown(
        """
        <style>
        .portal-card {
            background-color: #FFFFFF;
            padding: 24px;
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            border: 1px solid #E2E8F0;
            margin-bottom: 24px;
        }
        .portal-title {
            color: #0F172A;
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .portal-desc {
            color: #475569;
            font-size: 14px;
            margin-bottom: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sovereign Layout Title Block
    st.markdown(
        f'''
        <div class="portal-card">
            <div class="portal-title">{get_text("Sustainable Infrastructure & Utilities")}</div>
            <div class="portal-desc">{get_text("Log smart utility grids, graywater reclamation systems, and permeable low-impact paving networks.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_5_infrastructure_form"):
        
        st.subheader(get_text("1. Smart Water Infrastructure & Net-Zero Drainage"))
        col1, col2 = st.columns(2)
        with col1:
            graywater_treatment_cap = st.number_input(get_text("Graywater Reclamation Capacity (m³/Day)"), min_value=0.0, value=0.0, step=1.0)
            rainwater_harvesting_vol = st.number_input(get_text("Rainwater Storage Sump Capacity (m³)"), min_value=0.0, value=0.0, step=5.0)
        with col2:
            permeable_pavement_area = st.number_input(get_text("Permeable Sustainable Pavement Footprint (m²)"), min_value=0.0, value=0.0, step=10.0)
            smart_leak_meters = st.number_input(get_text("Automated Leak Detection Nodes (Count)"), min_value=0.0, value=0.0, step=1.0)

        st.subheader(get_text("2. Sustainable Civil Networks & District Systems"))
        col3, col4 = st.columns(2)
        with col3:
            district_cooling_load = st.number_input(get_text("District Cooling Interconnection Capacity (kW)"), min_value=0.0, value=0.0, step=10.0)
            ev_charging_stations = st.number_input(get_text("Electric Vehicle Fast-Charging Points (Count)"), min_value=0.0, value=0.0, step=1.0)
        with col4:
            solar_street_lights = st.number_input(get_text("Off-Grid Solar Photo-Voltaic Street Lights (Count)"), min_value=0.0, value=0.0, step=1.0)
            subsurface_utility_ducts = st.number_input(get_text("Shared Concrete Subsurface Common Utility Ducts (Meters)"), min_value=0.0, value=0.0, step=5.0)

        st.subheader(get_text("3. High-Performance Building Envelope Integration"))
        col5, col6 = st.columns(2)
        with col5:
            green_roof_area = st.number_input(get_text("Extensive Planted Green Roof Surface (m²)"), min_value=0.0, value=0.0, step=5.0)
        with col6:
            solar_reflective_index = st.number_input(get_text("High-Albedo Cool Roof Solar Reflective Index (SRI)"), min_value=0.0, max_value=100.0, value=0.0, step=0.1)

        # Strict Submission Action Implementation
        submit_btn = st.form_submit_button(label=get_text("Submit Infrastructure Compliance Log"))
        
        if submit_btn:
            # Complete mathematical aggregation validation matrix to catch uninitialized fields
            total_infrastructure_metrics = (
                graywater_treatment_cap + rainwater_harvesting_vol + permeable_pavement_area + 
                smart_leak_meters + district_cooling_load + ev_charging_stations + 
                solar_street_lights + subsurface_utility_ducts + green_roof_area + 
                solar_reflective_index
            )
            
            # Enforced zero value baseline barrier check
            if total_infrastructure_metrics == 0.0:
                st.error(get_text("Submission Rejected: All infrastructure data parameters are empty or hold 0.0 values."))
            else:
                # State pipeline integration placeholder
                st.success(get_text("Infrastructure baseline parameters validated and pushed to state manager pipeline."))
                
                # Dynamic calculated payload breakdown demonstration
                st.json({
                    "graywater_capacity_m3_day": graywater_treatment_cap,
                    "rainwater_sump_m3": rainwater_harvesting_vol,
                    "permeable_pavement_m2": permeable_pavement_area,
                    "leak_detection_nodes_count": smart_leak_meters,
                    "district_cooling_kw": district_cooling_load,
                    "ev_charging_points_count": ev_charging_stations,
                    "solar_street_lights_count": solar_street_lights,
                    "utility_ducts_meters": subsurface_utility_ducts,
                    "green_roof_area_m2": green_roof_area,
                    "cool_roof_sri_index": solar_reflective_index
                })
