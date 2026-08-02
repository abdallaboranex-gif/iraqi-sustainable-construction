import streamlit as st

def init_session_state():
    """
    تهيئة وإعداد ذاكرة الجلسة السحابية بحقول بيضاء وفارغة تماماً.
    منظفة من الحشو ومثبتة لقفل اللغة الصريح 'language' لتصفير انجماد الأزرار [١.١].
    """
    # [تحديث صارم] توحيد اسم المتغير المركزي ليعتمد الكلمة النصية الصريحة للغات الثلاث
    if "language" not in st.session_state:
        st.session_state.language = "العربية"
        
    if "current_portal" not in st.session_state:
        st.session_state.current_portal = 1
        
    if "audit_log" not in st.session_state:
        st.session_state.audit_log = []
        
    if "user_identity" not in st.session_state:
        st.session_state.user_identity = {
            "registered": False,
            "full_name": "",
            "rank_title": "مواطن / مقاول",
            "national_id": "",
            "syndicate_id": "",
            "avatar_url": "https://unsplash.com",
            "days_left": 365,
            "projects_list": []
        }
        
    if "property_data" not in st.session_state:
        st.session_state.property_data = {
            "governorate": "Baghdad",
            "district": "",
            "zoning_type": "",
            "is_compliant": True,
            "built_area": 0.0,
            "floors": 0
        }

def log_action(user, action_details):
    import datetime
    st.session_state.audit_log.append({
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user": user,
        "action": action_details
    })
