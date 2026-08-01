import streamlit as st

def render_portal_6():
    """
    واجهة الباب السادس: إدارة السلامة الموقعية والبيئية وكشف واقع الحال.
    تمتلك سلطة تجميد المعاملات عند المخالفة، وتوثيق المزامنة والتصحيح بالصور.
    """
    st.markdown("<h2 style='color: #00FFCC; font-size: 22px; margin-bottom: 5px;'>🦺 الباب السادس: إدارة السلامة الموقعية والامتثال البيئي الميداني</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #94A3B8; font-size: 13px;'>الواجهة التنفيذية للمفتشين واللجان الرقابية لتوثيق واقع الحال ومطابقة التنفيذ الفعلي مع المخططات والمدونات الرسمية [١.١].</p>", unsafe_allow_html=True)
    
    # جلب بيانات العقار والحالة الحالية وحالة الامتثال من الذاكرة السحابية
    property_info = st.session_state.property_data
    gov = property_info.get("governorate", "بغداد")
    is_compliant = property_info.get("is_compliant", True)
    
    # إنشاء حاوية لعرض حالة الموقع الميدانية الحالية بلون بVisual Anchor قوي
    with st.container(border=True):
        st.markdown("🚨 **الحالة الحالية للموقع في السجل السحابي العام:**")
        if is_compliant:
            st.success("🟢 موقع العمل نشط وسليم [مطابق لواقع الحال حالياً] - لا توجد مخالفات ميدانية مرصودة.")
        else:
            st.error("🔴 [المعاملة مجمدة وموقوفة بالكامل] - تم قفل رخصة العقار لوجود خروقات لشروط السلامة أو المدونات [١.١].")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # تقسيم العمل الميداني إلى قسمين: رصد المخالفات، وتوثيق إجراءات التصحيح وإعادة البث
    tab_audit, tab_rectification = st.tabs([
        "🔍 كشف واقع الحال ورصد الخروقات", 
        "🛠️ توثيق رفع المخالفات واستئناف العمل"
    ])
    
    # ---------------------------------------------------------
    # القسم الأول: كشف واقع الحال ورصد الخروقات (تجميد المعاملة)
    # ---------------------------------------------------------
    with tab_audit:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 12px;'>🔍 استمارة التفتيش الحقلي وإصدار أوامر التجميد</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #64748B; font-size: 11px;'>*تدعم هذه الواجهة وضع (Offline-First)؛ وسيتم خزن المدخلات محلياً على جهازك ومزامنتها فور توفر الإنترنت.*</p>", unsafe_allow_html=True)
        
        # بنود قائمة الفحص المستوحاة من مدونة السلامة العراقية [١.١]
        safety_item_1 = st.checkbox("1. عدم التزام العمال بارتداء معدات الحماية الشخصية والخوذ الجدارية (PPE Violation)")
        safety_item_2 = st.checkbox("2. غياب تدابير حماية وسقالات العمل في المرتفعات أو وجود مخاطر سقوط")
        safety_item_3 = st.checkbox("3. رصد عدم مطابقة في صب الخرسانة لواقع الحال (عدم مطابقة المواد للمخطط المعتمد)")
        safety_item_4 = st.checkbox("4. رمي أو التخلص غير الآمن من النفايات الإنشائية وخروقات البيئة المستدامة")
        
        st.markdown("<br>", unsafe_allow_html=True)
        violation_details = st.text_area("أدخل تفاصيل الخرق الإنشائي أو البيئي المرصود في الموقع بالتفصيل:")
        
        # صندوق رفع الأدلة البصرية (صور المخالفة الميدانية)
        violation_image = st.file_uploader(
            label="التقط أو ارفع صورة حية تثبت المخالفة المرصودة من موقع العمل:",
            type=["png", "jpg", "jpeg"],
            key="violation_img_uploader"
        )
        
        st.markdown("<br>", unsafe_allow_html=True)
        freeze_button = st.button("🔴 إرسال التقرير الميداني وتجميد المعاملة فوراً", use_container_width=True)
        
        if freeze_button:
            if safety_item_1 or safety_item_2 or safety_item_3 or safety_item_4 or violation_details:
                # تشغيل "الفرامل البرمجية" وقفل ملف العقار في السحاب
                st.session_state.property_data["is_compliant"] = False
                st.error("🛑 تم تجميد ملف العقار بنجاح! تم رفع راية الحظر وتجميد شهادة التوصية بالإجازة إلكترونياً.")
                
                # تسجيل المخالفة واسم المفتش في الصندوق الأسود السيادي لمدة 15 سنة
                from core.state_manager import log_action
                log_action(
                    user="Inspector Ahmad", 
                    action_details=f"أصدر أمر إيقاف وتجميد للمعاملة في {gov} لوجود خروقات إنشائية وميدانية موثقة بالصور."
                )
                st.rerun()
            else:
                st.warning("⚠️ يرجى تحديد بند واحد على الأقل من قائمة الخروقات أعلاه لتشغيل نظام حظر المعاملة.")

    # ---------------------------------------------------------
    # القسم الثاني: توثيق رفع المخالفات وإجراءات استئناف العمل
    # ---------------------------------------------------------
    with tab_rectification:
        st.markdown("<h4 style='color: #F8FAFC; font-size: 15px; margin-bottom: 12px;'>🛠️ نموذج معالجة المخالفات وطلب إعادة بث واستئناف العمل</h4>", unsafe_allow_html=True)
        
        if is_compliant:
            st.info("ℹ️ المعاملة سليمة ومفتوحة حالياً ولا توجد أي مخالفات نشطة تتطلب تقديم طلب تصحيح.")
        else:
            st.markdown("<p style='color: #94A3B8; font-size: 13px;'>بعد قيام المقاول بمعالجة الخطأ على الأرض، يدخل المفتش لرفع الدليل والتقرير التصحيحي لإعادة تفعيل رخصة البناء:</p>", unsafe_allow_html=True)
            
            rectification_details = st.text_area("وصف الإجراءات والحلول الهندسية التي اتخذت لتصحيح وتصفية الخطأ ميدانياً:")
            
            # رفع الصورة المؤكدة لإزالة المخالفة
            rectification_image = st.file_uploader(
                label="ارفع الصورة الحية الجديدة التي تثبت معالجة الخطأ وإزالة الخرق تماماً:",
                type=["png", "jpg", "jpeg"],
                key="rectification_img_uploader"
            )
            
            st.markdown("<br>", unsafe_allow_html=True)
            resume_button = st.button("🟢 إعتماد تقرير التصحيح وفك قفل المعاملة لاستئناف العمل", use_container_width=True)
            
            if resume_button and rectification_details and rectification_image:
                # إزالة الحظر وتفعيل الملف مجدداً تلقائياً في قاعدة البيانات السحابية
                st.session_state.property_data["is_compliant"] = True
                
                st.success("🎉 ممتاز! تم فك تجميد ملف العقار تلقائياً. أصبحت المعاملة نشطة وسليمة وجاهزة لإصدار الموافقات.")
                
                # توثيق سلسلة المسؤولية والتصحيح بالاسم والتاريخ والصور في السجل التاريخي للصندوق الأسود
                from core.state_manager import log_action
                log_action(
                    user="Inspector Ahmad", 
                    action_details=f"أكّد إزالة المخالفة وتصحيح الخطأ هندسياً بناءً على الكشف الميداني المؤرخ بالصور المرفقة وتم استئناف العمل."
                )
                st.rerun()
            elif resume_button:
                st.warning("⚠️ يرجى ملء وصف الحلول الهندسية وإرفاق الصورة الميدانية المؤكدة للتصحيح لكي يقبل النظام فك الحظر.")
