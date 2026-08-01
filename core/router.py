import streamlit as st
from views.portal_1_compliance import render_portal_1
from views.portal_2_sustainability import render_portal_2 # استيراد البوابة الثانية
from views.portal_3_aggregator import render_portal_3

def route_to_view():
    """الموجه المركزي لقراءة البوابة النشطة وعرض واجهتها المخصصة في السحاب"""
    current_portal = st.session_state.get("current_portal", 1)
    
    if current_portal == 1:
        render_portal_1()
    elif current_portal == 2:
        render_portal_2()
    elif current_portal == 3:
        render_portal_3()
    else:
        st.markdown(
            f"""
            <div style='background-color: #1E293B; border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center;'>
                <h4 style='color: #00FFCC; margin: 0;'>🚧 البوابة رقم {current_portal} جاهزة هيكلياً</h4>
                <p style='color: #94A3B8; font-size: 13px; margin: 5px 0 0 0;'>جاري حقن منطق العمل البرمجي التخصصي الخاص بها تتابعاً.</p>
            </div>
            """, 
            unsafe_allow_html=True
        )
