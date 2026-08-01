import streamlit as st

def render_footer():
    """تذييل الصفحة السفلي"""
    st.markdown(
        """
        <div style='text-align: center; color: #64748B; font-size: 12px;'>
            منصة البناء المستدام © 2026 - جميع الحقوق محفوظة للشركة المالكة | متوافق مع المدونات الهندسية العراقية
        </div>
        """, 
        unsafe_allow_html=True
    )
