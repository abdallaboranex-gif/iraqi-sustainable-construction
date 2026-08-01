import streamlit as st

def init_session_state():
    """
    تهيئة وإعداد ذاكرة الجلسة السحابية بحقول بيضاء وفارغة تماماً.
    تنتظر إدخال المستخدم وتوثيق هويته ديناميكياً بقوة القانون [١.١].
    """
    if "language" not in st.session_state:
        st.session_state.language = "ar"
        
    if "current_portal" not in st.session_state:
        st.session_state.current_portal = 1
        
    if "audit_log" not in st.session_state:
        st.session_state.audit_log = []
        
    # [تحديث] تصفير الهوية الرقمية للمستخدم وجعلها فارغة تماماً عند بدء النظام
    if "user_identity" not in st.session_state:
        st.session_state.user_identity = {
            "registered": False,       # حالة التسجيل (False تعني فارغ وغير مسجل)
            "full_name": "",           # الاسم الكامل فارغ
            "rank_title": "مواطن / مقاول", # الصفة الافتراضية قبل التحقق النقابي
            "national_id": "",         # الرقم الوطني فارغ
            "syndicate_id": "",        # رقم النقابة فارغ [١.١]
            "avatar_url": "https://unsplash.com", # صورة رمادية افتراضية للمجهول
            "days_left": 365,
            "projects_list": []        # سجل المشاريع فارغ وينتظر التسجيل
        }
        
    if "property_data" not in st.session_state:
        st.session_state.property_data = {
            "governorate": "Baghdad",
            "district": "",
            "zoning_type": "Residential",
            "is_compliant": True,
            "current_step": 2,
            "built_area": 150.0,
            "floors": 2
        }
        
    if "uploaded_files_cache" not in st.session_state:
        st.session_state.uploaded_files_cache = {}

def set_portal(portal_number):
    st.session_state.current_portal = portal_number

def log_action(user, action_details):
    import datetime
    log_entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "action": action_details
    }
    st.session_state.audit_log.append(log_entry)
