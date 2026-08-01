import streamlit as st
from utils.localization import get_text

def render_portal_6():
    """
    واجهة الباب السادس المترجمة بالكامل للغات الثلاث.
    تمتلك سلطة تجميد وقفل المعاملة بالكامل في السحاب لحماية السلامة [١.١].
    """
    st.markdown(f"<h2 style='color: #1D4ED8; font-size: 22px; margin-bottom: 5px; font-weight: 800;'>{get_text('p6_title')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #0F172A; font-size: 13px;'>{get_text('p6_desc')}</p>", unsafe_allow_html=True)
    
    is_compliant = st.session_state.property_data.get("is_compliant", True)
    
    with st.container(border=True):
        st.markdown("🚨 **حالة الموقع الميداني في السجل السحابي العام:**")
        if is_compliant:
            st.success("🟢 موقع العمل نشط وسليم [مطابق لواقع الحال حالياً] - لا توجد مخالفات ميدانية مرصودة.")
        else:
            st.error("🔴 [المعاملة مجمدة وموقوفة بالكامل] - تم قفل رخصة العقار لوجود خروقات لشروط السلامة أو المدونات.")

    st.markdown("<br>", unsafe_allow_html=True)
    tab_audit, tab_rectification = st.tabs(["🔍 كشف واقع الحال ورصد الخروقات", "🛠️ توثيق رفع المخالفات واستئناف العمل"])
    
    with tab_audit:
        safety_violation = st.checkbox("1. عدم الالتزام بمدونة السلامة الموقعية وغياب معدات الحماية (PPE Violation)")
        violation_details = st.text_area("أدخل تفاصيل الخرق الإنشائي أو البيئي المرصود في الموقع بالتفصيل:")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(get_text("p6_btn_freeze"), use_container_width=True):
            if safety_violation or violation_details:
                st.session_state.property_data["is_compliant"] = False
                st.error("🛑 تم تجميد ملف العقار وقفل المعاملة بنجاح!")
                st.rerun()
                
    with tab_rectification:
        if is_compliant:
            st.info("ℹ️ المعاملة سليمة ومفتوحة حالياً ولا توجد أي مخالفات نشطة تتطلب تقديم طلب تصحيح.")
        else:
            rectification_details = st.text_area("وصف الإجراءات والحلول الهندسية التي اتخذت لتصحيح وتصفية الخطأ ميدانياً:")
            if st.button(get_text("p6_btn_resume"), use_container_width=True):
                if rectification_details:
                    st.session_state.property_data["is_compliant"] = True
                    st.success("🎉 ممتاز! تم فك تجميد ملف العقار تلقائياً واعادة تفعيل الصلاحيات.")
                    st.rerun()
