import streamlit as st
from views.portal_1_compliance import render_portal_1

def route_to_view():
    """الموجه المركزي لقراءة البوابة النشطة وعرض ملفها المخصص"""
    # قراءة رقم البوابة الحالية الفعالة من الذاكرة السحابية (الافتراضي هو 1)
    current_portal = st.session_state.get("current_portal", 1)
    
    if current_portal == 1:
        render_portal_1()
    else:
        st.write("البوابات الأخرى سيتم حقن أكوادها بالتسلسل")
