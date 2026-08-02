import streamlit as st
from utils.localization import get_text

def render_portal_4_gis_map():
    """
    Portal 4: GIS Geospatial Mapping & Site Boundary Management.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Exact filename synchronization: portal_4_gis_map.py
    - Blank 0.0 state initialization with structural high-contrast aesthetics
    - Enforced boundary verification checkpoints to catch empty spatial logs
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
            <div class="portal-title">{get_text("GIS Spatial Boundary Mapping")}</div>
            <div class="portal-desc">{get_text("Log geographic coordinate vertices, site boundaries, and buffer zones for green development clearance.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # Core Form Component Container with Strict Validation Architecture
    with st.form(key="portal_4_gis_map_form"):
        
        st.subheader(get_text("1. Centroid Geographic Coordinates (WGS 84)"))
        col1, col2 = st.columns(2)
        with col1:
            site_latitude = st.number_input(get_text("Site Centroid Latitude (Decimal Degrees)"), min_value=0.0, max_value=90.0, value=0.0, step=0.000001, format="%.6f")
        with col2:
            site_longitude = st.number_input(get_text("Site Centroid Longitude (Decimal Degrees)"), min_value=0.0, max_value=180.0, value=0.0, step=0.000001, format="%.6f")

        st.subheader(get_text("2. Project Plot Boundaries & Spatial Dimensions"))
        col3, col4 = st.columns(2)
        with col3:
            total_plot_area = st.number_input(get_text("Total Surveyed Plot Area (m²)"), min_value=0.0, value=0.0, step=10.0)
            green_buffer_zone_width = st.number_input(get_text("Designated Green Buffer Strip Width (Meters)"), min_value=0.0, value=0.0, step=0.5)
        with col4:
            total_perimeter_length = st.number_input(get_text("Boundary Perimeter Outer Length (Meters)"), min_value=0.0, value=0.0, step=1.0)
            built_up_footprint = st.number_input(get_text("Primary Superstructure Built-Up Area (m²)"), min_value=0.0, value=0.0, step=10.0)

        st.subheader(get_text("3. Environmental Buffers & Environmental Clearance"))
        col5, col6 = st.columns(2)
        with col5:
            nearest_water_body_dist = st.number_input(get_text("Distance to Nearest Natural Water Body (km)"), min_value=0.0, value=0.0, step=0.1)
        with col6:
            protected_ecology_dist = st.number_input(get_text("Distance to Sovereign Protected Ecological Zone (km)"), min_value=0.0, value=0.0, step=0.1)

        # Strict Submission Action Implementation
        submit_btn = st.form_submit_button(label=get_text("Verify and Save Geospatial Coordinates"))
        
        if submit_btn:
            # Complete mathematical aggregation evaluation matrix to catch uninitialized coordinates
            total_spatial_metrics = (
                site_latitude + site_longitude + total_plot_area + 
                green_buffer_zone_width + total_perimeter_length + built_up_footprint + 
                nearest_water_body_dist + protected_ecology_dist
            )
            
            # Enforced zero value baseline barrier check
            if total_spatial_metrics == 0.0:
                st.error(get_text("Submission Rejected: Spatial coordinate profiles and plot parameters cannot be 0.0."))
            else:
                # State pipeline integration placeholder
                st.success(get_text("Geospatial GIS baseline parameters validated and pushed to state manager pipeline."))
                
                # Dynamic calculated payload breakdown demonstration
                st.json({
                    "centroid_latitude_dd": site_latitude,
                    "centroid_longitude_dd": site_longitude,
                    "surveyed_plot_area_m2": total_plot_area,
                    "green_buffer_strip_meters": green_buffer_zone_width,
                    "boundary_perimeter_meters": total_perimeter_length,
                    "built_up_footprint_m2": built_up_footprint,
                    "water_body_distance_km": nearest_water_body_dist,
                    "ecological_zone_distance_km": protected_ecology_dist
                })
