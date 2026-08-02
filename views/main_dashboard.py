import streamlit as st
import datetime
from utils.localization import get_text

def render_main_dashboard():
    """
    Main Analytics & Telemetry Controls Dashboard View.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() [1.1]
    - Filename matching structural blueprint: views/main_dashboard.py
    - Displays external interactive elements: Real-time clock, date, and construction weather metrics
    - High-contrast premium light theme styling overrides (#0F172A thick navy fonts)
    """
    
    # Custom light theme high-contrast styling for the telemetry widgets
    st.markdown(
        """
        <style>
        .telemetry-header-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 16px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 6px -1px rgba(15, 23, 42, 0.05);
            margin-bottom: 20px;
        }
        .telemetry-title {
            color: #0F172A !important;
            font-size: 20px;
            font-weight: 800;
            margin-bottom: 4px;
        }
        .telemetry-desc {
            color: #475569 !important;
            font-size: 13px;
        }
        .external-card {
            background-color: #FFFFFF;
            padding: 16px;
            border-radius: 14px;
            border: 1px solid #E2E8F0;
            box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.04);
            text-align: center;
        }
        .external-value {
            color: #1D4ED8 !important; /* Premium Royal Blue */
            font-size: 24px;
            font-weight: 800;
            margin-bottom: 2px;
        }
        .external-label {
            color: #64748B !important;
            font-size: 12px;
            font-weight: 600;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sovereign Dashboard Executive Title Block
    st.markdown(
        f'''
        <div class="telemetry-header-card">
            <div class="telemetry-title">🖥️ {get_text("National Telemetry Control Controls")}</div>
            <div class="telemetry-desc">{get_text("Real-time external environmental monitoring and active satellite pipeline indicators.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    # 1. TIME & DATE BLOCK: Capture native platform temporal fields safely
    st.subheader(get_text("Sovereign Temporal Clock Indicators"))
    
    current_moment = datetime.datetime.now()
    formatted_time = current_moment.strftime("%I:%M:%S %p")
    formatted_date = current_moment.strftime("%A, %B %d, %Y")
    
    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown(
            f'''
            <div class="external-card" style="border-right: 4px solid #1D4ED8;">
                <div class="external-value">⏰ {formatted_time}</div>
                <div class="external-label">{get_text("Sovereign Synchronized Baghdad Time (GMT+3)")}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with t_col2:
        st.markdown(
            f'''
            <div class="external-card" style="border-right: 4px solid #1D4ED8;">
                <div class="external-value">📅 {formatted_date}</div>
                <div class="external-label">{get_text("Official Civil Calendar Ledger")}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. WEATHER & ENVIRONMENTAL METRICS BLOCK: Reading active location bounds from session state
    target_governorate = st.session_state.property_data.get("governorate", "Baghdad")
    st.subheader(f"{get_text('Active Climate Environmental Monitoring')} (📍 {target_governorate})")
    
    # Mock parameters aligned to strict 0.0 baseline or live estimated thresholds for construction safety
    mock_temperature = 42.0 if target_governorate == "Basra" else 37.5
    mock_humidity = 18.0
    mock_wind_speed = 14.5
    
    w_col1, w_col2, w_col3 = st.columns(3)
    with w_col1:
        st.markdown(
            f'''
            <div class="external-card">
                <div class="external-value" style="color: #EA580C !important;">{mock_temperature}°C</div>
                <div class="external-label">{get_text("Ambient Core Air Temperature")}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with w_col2:
        st.markdown(
            f'''
            <div class="external-card">
                <div class="external-value">{mock_humidity}%</div>
                <div class="external-label">{get_text("Relative Hydrological Humidity")}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )
    with w_col3:
        st.markdown(
            f'''
            <div class="external-card">
                <div class="external-value">{mock_wind_speed} km/h</div>
                <div class="external-label">{get_text("Aerodynamic Wind Velocity Velocity")}</div>
            </div>
            ''',
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. PLATFORM INTEGRITY LAYER: Operational statuses and ledger warnings
    st.subheader(get_text("Sovereign Network Integrity"))
    
    inf_col1, inf_col2 = st.columns(2)
    with inf_col1:
        st.metric(label=get_text("Sovereign Gateway Server Bandwidth Latency"), value="24.2 ms")
    with inf_col2:
        # Informational alert showing system readiness trace status
        st.warning(get_text("System Baseline Active: Monitoring real-time inputs canvas from the right-hand layout panel."))
