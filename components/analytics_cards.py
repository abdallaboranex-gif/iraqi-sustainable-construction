import streamlit as st
from utils.localization import get_text # استيراد دالة الترجمة الفورية

def render_side_analytics():
    """
    رسم كروت المؤشرات الستة المتقدمة المشرقة والمربوطة بالترجمة الثلاثية الكاملة.
    تعرض نسب المطابقة، السلامة، وتوفير الطاقة بحروف غامقة حادة وعالية التباين.
    """
    st.markdown(f"<h3 style='color: #0F172A; font-size: 18px; margin-bottom: 15px; font-weight: 700;'>📊 {get_text('side_title')}</h3>", unsafe_allow_html=True)
    
    # 1. كرت مؤشر المطابقة الهندسية المترجم
    with st.container(border=True):
        st.markdown(
            f"""
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('compliance_score')}</span>
                    <h2 style='color: #1D4ED8; margin: 0; font-weight: 800; font-size: 26px;'>42%</h2>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        st.progress(0.42)
        
    # 2. كرت السلامة الإنشائية والامتثال للمدونة المترجم
    with st.container(border=True):
        st.markdown(
            f"""
            <div>
                <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('integrity_score')}</span>
                <div style='display: flex; align-items: center; gap: 10px; margin-top: 4px;'>
                    <h2 style='color: #EF4444; margin: 0; font-weight: 800; font-size: 26px;'>0%</h2>
                </div>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # 3. كرت استدامة الطاقة والمنظومات المترجم
    with st.container(border=True):
        st.markdown(
            f"""
            <div>
                <span style='color: #475569; font-size: 12px; font-weight: 700; display: block;'>{get_text('energy_score')}</span>
                <h2 style='color: #10B981; margin: 0; font-weight: 800; font-size: 26px;'>27%</h2>
            </div>
            """, 
            unsafe_allow_html=True
        )
