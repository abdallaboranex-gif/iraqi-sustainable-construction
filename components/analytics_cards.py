import streamlit as st
from utils.localization import get_text

def render_side_analytics():
    """
    Sovereign Live Indicators Component.
    100% Pure English source strings mapped directly to the automated translation engine [١.١].
    """
    st.markdown(f"<h3 style='color: #0F172A; font-size: 18px; margin-bottom: 15px; font-weight: 700;'>📊 {get_text('Live Indicators Panel')}</h3>", unsafe_allow_html=True)
    
    # 1. Engineering Compliance Metric Card
    with st.container(border=True):
        st.markdown(
            f"""
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('Engineering Compliance')}</span>
                    <h2 style='color: #1D4ED8; margin: 0; font-weight: 800; font-size: 26px;'>42%</h2>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.progress(0.42)
        
    # 2. Structural Integrity Metric Card
    with st.container(border=True):
        st.markdown(
            f"""
            <div>
                <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('Structural Integrity')}</span>
                <div style='display: flex; align-items: center; gap: 10px; margin-top: 4px;'>
                    <h2 style='color: #EF4444; margin: 0; font-weight: 800; font-size: 26px;'>0%</h2>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 3. Energy Sustainability Metric Card
    with st.container(border=True):
        st.markdown(
            f"""
            <div>
                <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('Energy Score')}</span>
                <h2 style='color: #10B981; margin: 0; font-weight: 800; font-size: 26px;'>27%</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
