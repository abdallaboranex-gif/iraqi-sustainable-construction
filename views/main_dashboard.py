import streamlit as st
from utils.localization import get_text

def render_main_dashboard():
    """
    Main Analytics & Compliance Dashboard View.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text()
    - Filename matching structural blueprint: views/main_dashboard.py
    - High-contrast UI style elements (#0F172A text, 16px radius cards)
    - All analytical indices and aggregate metrics initialize at clean 0.0 or blank
    """
    st.markdown(
        """
        <style>
        .dashboard-header-card { background-color: #FFFFFF; padding: 24px; border-radius: 16px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); border: 1px solid #E2E8F0; margin-bottom: 24px; }
        .dashboard-title { color: #0F172A; font-size: 28px; font-weight: 700; margin-bottom: 8px; }
        .dashboard-desc { color: #475569; font-size: 15px; }
        .metric-card { background-color: #FFFFFF; padding: 20px; border-radius: 16px; box-shadow: 0 2px 4px -1px rgba(0, 0, 0, 0.06); border: 1px solid #E2E8F0; text-align: center; }
        .metric-value { color: #0F172A; font-size: 32px; font-weight: 800; margin-bottom: 4px; }
        .metric-label { color: #64748B; font-size: 14px; font-weight: 500; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="dashboard-header-card">
            <div class="dashboard-title">{get_text("National Green Construction Analytics Control")}</div>
            <div class="dashboard-desc">{get_text("Real-time aggregated compliance monitoring across all sovereign regional project logs.")}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.subheader(get_text("Sovereign Sustainability Performance Indices"))
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.markdown(f'<div class="metric-card"><div class="metric-value">0.0%</div><div class="metric-label">{get_text("Overall Project Compliance Rate")}</div></div>', unsafe_allow_html=True)
    with m_col2:
        st.markdown(f'<div class="metric-card"><div class="metric-value">0.00</div><div class="metric-label">{get_text("Aggregated Carbon Mitigation (tCO2e)")}</div></div>', unsafe_allow_html=True)
    with m_col3:
        st.markdown(f'<div class="metric-card"><div class="metric-value">0.0%</div><div class="metric-label">{get_text("Sustainable Material Sourcing Quotient")}</div></div>', unsafe_allow_html=True)
    with m_col4:
        st.markdown(f'<div class="metric-card"><div class="metric-value">0.0</div><div class="metric-label">{get_text("Active Registered Green Sites (Count)")}</div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col_left, col_right = st.columns(2)
    with col_left:
        st.subheader(get_text("Portal Compliance Breakdown Status"))
        st.info(get_text("No active compliance vectors submitted yet. Cumulative data charts will render automatically upon portal submissions."))
        st.caption(f"📊 {get_text('Geospatial GIS data layers: 0 active maps linked.')}")
        st.caption(f"🏗️ {get_text('Infrastructure network points: 0 smart utilities monitored.')}")
    with col_right:
        st.subheader(get_text("System Integrity & Alerts"))
        st.warning(get_text("System Baseline Established: Awaiting compliance pipeline transmission logs from site managers."))
