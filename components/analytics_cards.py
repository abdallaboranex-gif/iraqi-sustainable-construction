import streamlit as st

def render_side_analytics():
    """رسم كروت المؤشرات الستة في العمود الجانبي الأيمن"""
    st.markdown("<h3 style='color: #F8FAFC; font-size: 18px; margin-bottom: 15px;'>📊 لوحة المؤشرات الحية</h3>", unsafe_allow_html=True)
    
    # كرت مؤشر المطابقة الهندسية
    with st.container(border=True):
        st.markdown("<span style='color: #94A3B8; font-size: 12px;'>المطابقة الهندسية / Compliance</span>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #00FFCC; margin: 0;'>42%</h2>", unsafe_allow_html=True)
        
    # كرت السلامة الإنشائية
    with st.container(border=True):
        st.markdown("<span style='color: #94A3B8; font-size: 12px;'>السلامة الإنشائية / Integrity</span>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #EF4444; margin: 0;'>0%</h2>", unsafe_allow_html=True)
        
    # كرت كفاءة الطاقة
    with st.container(border=True):
        st.markdown("<span style='color: #94A3B8; font-size: 12px;'>استدامة الطاقة / Energy Score</span>", unsafe_allow_html=True)
        st.markdown("<h2 style='color: #00FFCC; margin: 0;'>27%</h2>", unsafe_allow_html=True)
