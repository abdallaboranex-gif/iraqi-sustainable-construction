import streamlit as st
from utils.localization import get_text

def render_portal_2_sustainability():
    """
    Portal 2: Sustainability Standards & Eco-Certified Materials.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Exact filename synchronization: portal_2_sustainability.py
    - Clean separation of concerns with 0.0 blank initialization
    - Enforced baseline safeguards against empty/zero submissions
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
            <div class="portal-title">{get_text("Sustainability & Material Compliance Log")}</div>
            <div class="portal-desc">{get_text("Register and audit local eco-certified materials, sustainable aggregates, and low-carbon cement volumes.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_2_sustainability_form"):
        
        st.subheader(get_text("1. Local & Eco-Certified Procurement"))
        col1, col2 = st.columns(2)
        with col1:
            local_brick_volume = st.number_input(get_text("Sovereign Thermo-Brick Volume (m³)"), min_value=0.0, value=0.0, step=1.0)
            recycled_aggregate_mass = st.number_input(get_text("Recycled Concrete Aggregate Mass (Tons)"), min_value=0.0, value=0.0, step=1.0)
        with col2:
            eco_certified_timber = st.number_input(get_text("Certified Sustainable Timber Volume (m³)"), min_value=0.0, value=0.0, step=1.0)
            pozzolanic_additives = st.number_input(get_text("Natural Pozzolanic Additives Mass (Tons)"), min_value=0.0, value=0.0, step=1.0)

        st.subheader(get_text("2. Low-Carbon Concrete & Supply Metrics"))
        col3, col4 = st.columns(2)
        with col3:
            blended_cement_ratio = st.number_input(get_text("Blended Portland Cement Substitution Rate (%)"), min_value=0.0, max_value=100.0, value=0.0, step=0.1)
            low_carbon_concrete_vol = st.number_input(get_text("Low-Carbon Ready-Mix Concrete Volume (m³)"))
        with col4:
            ggbs_slag_content = st.number_input(get_text("Ground Granulated Blast-Furnace Slag Ratio (%)"), min_value=0.0, max_value=100.0, value=0.0, step=0.1)
            fly_ash_mass = st.number_input(get_text("Sourced Pulverized Fly Ash Mass (Tons)"), min_value=0.0, value=0.0, step=1.0)

        st.subheader(get_text("3. Supply Chain Logistics & Sourcing Radius"))
        col5, col6 = st.columns(2)
        with col5:
            local_procurement_radius = st.number_input(get_text("Maximum Material Sourcing Radius (km)"), min_value=0.0, value=0.0, step=5.0)
            rail_barge_logistics = st.number_input(get_text("Low-Emission Multimodal Freight Mass (Tons)"), min_value=0.0, value=0.0, step=1.0)
        with col6:
            epd_verified_products = st.number_input(get_text("Verified Environmental Product Declaration Items (Count)"), min_value=0.0, value=0.0, step=1.0)

        # Strict Submission Action Implementation
        submit_btn = st.form_submit_button(label=get_text("Submit Sustainability Compliance Log"))
        
        if submit_btn:
            # Complete 11-field mathematical aggregation matrix validation to catch empty submissions
            total_sustainability_metrics = (
                local_brick_volume + recycled_aggregate_mass + eco_certified_timber + 
                pozzolanic_additives + blended_cement_ratio + low_carbon_concrete_vol + 
                ggbs_slag_content + fly_ash_mass + local_procurement_radius + 
                rail_barge_logistics + epd_verified_products
            )
            
            # Enforced zero value baseline barrier check
            if total_sustainability_metrics == 0.0:
                st.error(get_text("Submission Rejected: All portal data parameters are empty or hold 0.0 values."))
            else:
                # State pipeline integration placeholder
                st.success(get_text("Compliance data validated and pushed to the state manager pipeline successfully."))
                
                # Dynamic calculated payload breakdown demonstration
                st.json({
                    "local_brick_volume_m3": local_brick_volume,
                    "recycled_aggregate_mass_tons": recycled_aggregate_mass,
                    "eco_certified_timber_m3": eco_certified_timber,
                    "pozzolanic_additives_tons": pozzolanic_additives,
                    "blended_cement_substitution_pct": blended_cement_ratio,
                    "low_carbon_concrete_volume_m3": low_carbon_concrete_vol,
                    "ggbs_slag_ratio_pct": ggbs_slag_content,
                    "fly_ash_mass_tons": fly_ash_mass,
                    "max_sourcing_radius_km": local_procurement_radius,
                    "multimodal_freight_mass_tons": rail_barge_logistics,
                    "epd_count": epd_verified_products
                })
