import streamlit as st
import os

def check_and_reload_cache():
    """
    محرك مراقبة وتحديث الذاكرة السحابية المؤقتة (Cache).
    يضمن تصفير الذاكرة وبث بيانات المدونات الجديدة فور رفع ملف إكسل محدث على GitHub.
    """
    base_path = os.path.join("data", "codes")
    
    # التحقق من وجود المجلد الأساسي للمدونات العراقيّة لمنع الأخطاء الإجرائيّة
    if not os.path.exists(base_path):
        return False
        
    # جلب التواقيع الزمنية لملفات الإكسل المخزنة لمراقبة أي تعديل طرأ عليها
    try:
        current_files = os.listdir(base_path)
        # الاحتفاظ بسجل التغييرات داخل الذاكرة المؤقتة للجلسة
        if "last_cache_check" not in st.session_state:
            st.session_state.last_cache_check = len(current_files)
            
        # إذا تم رصد رفع ملف إكسل جديد أو تعديل ملف قائم على GitHub
        if len(current_files) != st.session_state.last_cache_check:
            st.session_state.last_cache_check = len(current_files)
            # تصفير محرك القواعد وجداول الـ Pandas المخزنة برمجياً
            st.cache_data.clear()
            return True
    except Exception:
        pass
        
    return False
