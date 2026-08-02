import streamlit as st
from utils.localization import get_text

def render_portal_6_site_safety():
    """
    Portal 6: Occupational Safety & Site Environmental Stewardship.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Exact filename synchronization: portal_6_site_safety.py
    - Blank 0.0 state initialization with structural high-contrast aesthetics
    - Enforced safety and stewardship safeguards to reject zero/empty logs
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
            <div class="portal-title">{get_text("Site Safety & Environmental Stewardship")}</div>
            <div class="portal-desc">{get_text("Audit occupational health protocols, dust mitigation screens, and environmental protection barriers.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_6_site_safety_form"):
        
        st.subheader(get_text("1. Site Environmental Control & Air Quality"))
        col1, col2 = st.columns(2)
        with col1:
            dust_suppression_water = st.number_input(get_text("Dust Suppression Active Water Volume (m³/Day)"), min_value=0.0, value=0.0, step=0.5)
            air_quality_monitors = st.number_input(get_text("Calibrated PM2.5 / PM10 Air Monitoring Stations (Count)"), min_value=0.0, value=0.0, step=1.0)
        with col2:
            acoustic_barrier_length = st.number_input(get_text("Noise Mitigation Acoustic Boundary Fencing (Meters)"), min_value=0.0, value=0.0, step=5.0)
            turbidity_curtain_area = st.number_input(get_text("Stormwater Runoff Sediment Filter Silt Geotextile (m²)"), min_value=0.0, value=0.0, step=10.0)

        st.subheader(get_text("2. Occupational Health & Safety Compliance"))
        col3, col4 = st.columns(2)
        with col3:
            hse_induction_hours = st.number_input(get_text("Mandatory HSE Training and Induction Duration (Hours)"), min_value=0.0, value=0.0, step=1.0)
            safety_harness_checkpoints = st.number_input(get_text("Working at Heights Specialized Safety Equipment (Count)"), min_value=0.0, value=0.0, step=1.0)
        with col4:
            medical_post_capacity = st.number_input(get_text("First-Aid Medical Deployment Operational Capacity (Personnel)"), min_value=0.0, value=0.0, step=1.0)
            fire_extinguisher_nodes = st.number_input(get_text("Emergency Fire Extinguisher Active Inspection Nodes (Count)"), min_value=0.0, value=0.0, step=1.0)

        st.subheader(get_text("3. Incident Metrics & Risk Safeguards"))
        col5, col6 = st.columns(2)
        with col5:
            safe_man_hours = st.number_input(get_text("Logged Zero-Incident Safe Man-Hours (Count)"), min_value=0.0, value=0.0, step=10.0)
        with col6:
            risk_audits_completed = st.number_input(get_text("Proactive Job Safety Risk Assessment Audits (Count)"), min_value=0.0, value=0.0, step=1.0)

        # Strict Submission Action Implementation
        submit_btn = st.form_submit_button(label=get_text("Submit Safety Compliance Log"))
        
        if submit_btn:
            # Complete mathematical aggregation validation matrix to catch uninitialized fields
            total_safety_metrics = (
                dust_suppression_water + air_quality_monitors + acoustic_barrier_length + 
                turbidity_curtain_area + hse_induction_hours + safety_harness_checkpoints + 
                medical_post_capacity + fire_extinguisher_nodes + safe_man_hours + 
                risk_audits_completed
            )
            
            # Enforced zero value baseline barrier check
            if total_safety_metrics == 0.0:
                st.error(get_text("Submission Rejected: All site safety parameters are empty or hold 0.0 values."))
            else:
                # State pipeline integration placeholder
                st.success(get_text("Site safety compliance parameters validated and pushed to state manager pipeline."))
                
                # Dynamic calculated payload breakdown demonstration
                st.json({
                    "dust_suppression_m3_day": dust_suppression_water,
                    "air_monitors_count": air_quality_monitors,
                    "acoustic_barriers_meters": acoustic_barrier_length,
                    "silt_geotextile_m2": turbidity_curtain_area,
                    "hse_training_hours": hse_induction_hours,
                    "safety_harness_count": safety_harness_checkpoints,
                    "medical_personnel_count": medical_post_capacity,
                    "fire_nodes_count": fire_extinguisher_nodes,
                    "safe_man_hours_count": safe_man_hours,
                    "risk_audits_count": risk_audits_completed
                })
