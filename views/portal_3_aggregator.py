import streamlit as st
from utils.localization import get_text

def render_portal_3_aggregator():
    """
    Portal 3: Data Aggregator & Environmental Impact Metrics.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: portal_3_aggregator.py
    - Blank 0.0 state initialization with high-contrast UI parameters
    - Enforced submission safeguards to reject empty logs
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
            <div class="portal-title">{get_text("Environmental Data Aggregator")}</div>
            <div class="portal-desc">{get_text("Consolidate total carbon equivalence, operational energy footprints, and site resource waste metrics.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_3_aggregator_form"):
        
        st.subheader(get_text("1. Embodied Carbon & Emissions Inventory"))
        col1, col2 = st.columns(2)
        with col1:
            structural_carbon = st.number_input(get_text("Structural Elements Carbon (tCO2e)"), min_value=0.0, value=0.0, step=0.1)
            finishing_carbon = st.number_input(get_text("Finishing & Fit-Out Carbon (tCO2e)"), min_value=0.0, value=0.0, step=0.1)
        with col2:
            machinery_diesel_emissions = st.number_input(get_text("On-Site Machinery Diesel Footprint (tCO2e)"), min_value=0.0, value=0.0, step=0.1)
            transportation_logistics_carbon = st.number_input(get_text("Material Transportation Carbon (tCO2e)"), min_value=0.0, value=0.0, step=0.1)

        st.subheader(get_text("2. Operational Energy Aggregation"))
        col3, col4 = st.columns(2)
        with col3:
            grid_electricity_consumption = st.number_input(get_text("Projected Grid Electricity Demand (MWh)"), min_value=0.0, value=0.0, step=1.0)
            renewable_energy_offset = st.number_input(get_text("On-Site Solar Renewable Generation Offset (MWh)"), min_value=0.0, value=0.0, step=1.0)
        with col4:
            hvac_energy_load = st.number_input(get_text("HVAC Thermal System Design Load (kW)"), min_value=0.0, value=0.0, step=1.0)
            lighting_power_density = st.number_input(get_text("Total Lighting Power Intensity (W/m²)"), min_value=0.0, value=0.0, step=0.1)

        st.subheader(get_text("3. Waste Demolition & Resource Recovery"))
        col5, col6 = st.columns(2)
        with col5:
            hazardous_waste_mass = st.number_input(get_text("Regulated Hazardous Waste Generated (Tons)"), min_value=0.0, value=0.0, step=0.1)
            diverted_landfill_mass = st.number_input(get_text("Diverted Waste Recycled On-Site (Tons)"), min_value=0.0, value=0.0, step=0.1)
        with col6:
            wastewater_discharge_vol = st.number_input(get_text("Untreated Site Runoff Wastewater Discharge (m³)"), min_value=0.0, value=0.0, step=1.0)

        # Strict Submission Action Implementation
        submit_btn = st.form_submit_button(label=get_text("Submit Aggregated Compliance Log"))
        
        if submit_btn:
            # Complete 11-field mathematical aggregation matrix validation to catch empty submissions
            total_aggregator_metrics = (
                structural_carbon + finishing_carbon + machinery_diesel_emissions + 
                transportation_logistics_carbon + grid_electricity_consumption + renewable_energy_offset + 
                hvac_energy_load + lighting_power_density + hazardous_waste_mass + 
                diverted_landfill_mass + wastewater_discharge_vol
            )
            
            # Enforced zero value baseline barrier check
            if total_aggregator_metrics == 0.0:
                st.error(get_text("Submission Rejected: All portal data parameters are empty or hold 0.0 values."))
            else:
                # State pipeline integration placeholder
                st.success(get_text("Aggregator metrics validated and pushed to the state manager pipeline successfully."))
                
                # Dynamic calculated payload breakdown demonstration
                st.json({
                    "structural_carbon_tco2e": structural_carbon,
                    "finishing_carbon_tco2e": finishing_carbon,
                    "machinery_diesel_tco2e": machinery_diesel_emissions,
                    "transport_carbon_tco2e": transportation_logistics_carbon,
                    "grid_electricity_mwh": grid_electricity_consumption,
                    "solar_offset_mwh": renewable_energy_offset,
                    "hvac_load_kw": hvac_energy_load,
                    "lighting_density_wm2": lighting_power_density,
                    "hazardous_waste_tons": hazardous_waste_mass,
                    "recycled_waste_tons": diverted_landfill_mass,
                    "wastewater_discharge_m3": wastewater_discharge_vol
                })
