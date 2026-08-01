import streamlit as st

def init_session_state():
    """
    دالة مركزية لتهيئة وإعداد ذاكرة الجلسة السحابية للمستخدم.
    تضمن حفظ بيانات العقار والمطابقة وتوافق اللغات طوال فترة التصفح.
    """
    
    # 1. تهيئة لغة المنصة الافتراضية (العربية)
    if "language" not in st.session_state:
        st.session_state.language = "ar"
        
    # 2. تهيئة البوابة النشطة حالياً (الافتراضية: البوابة الأولى - التدقيق والتربة)
    if "current_portal" not in st.session_state:
        st.session_state.current_portal = 1
        
    # 3. تهيئة السجل التاريخي للصندوق الأسود (Audit Trail) لتوثيق المسؤولية القانونية (15 سنة)
    if "audit_log" not in st.session_state:
        st.session_state.audit_log = []
        
    # 4. تهيئة بيانات العقار المدخلة والـ 13 حقل رئيسي للفلترة الجغرافية
    if "property_data" not in st.session_state:
        st.session_state.property_data = {
            "governorate": "Baghdad", # المحافظة الافتراضية
            "district": "",          # القضاء
            "zoning_type": "Residential", # نوع الاستخدام (سكني/تجاري/صناعي)
            "is_compliant": True,     # حالة العقار العامة (أخضر مطابق / أحمر مخالف)
            "current_step": 2         # الخطوة الحالية النشطة في مسار البناء (مطابق للصورة)
        }
        
    # 5. تهيئة الذاكرة المؤقتة لملفات المختبرات والخرائط الجاري تدقيقها
    if "uploaded_files_cache" not in st.session_state:
        st.session_state.uploaded_files_cache = {}

def set_portal(portal_number):
    """دالة ديناميكية للانتقال بين البوابات الستة وتحديث حالة التوجيه في السحاب"""
    st.session_state.current_portal = portal_number

def log_action(user, action_details):
    """دالة الصندوق الأسود لتسجيل وحفظ حركات المستخدم بشكل فوري لحماية البيانات قانونياً"""
    import datetime
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "action": action_details
    }
    st.session_state.audit_log.append(log_entry)
