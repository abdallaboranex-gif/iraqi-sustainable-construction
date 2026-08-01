import streamlit as st

def route_to_view():
    """توجيه المستخدم مؤقتاً إلى واجهة لوحة التحكم الرئيسية"""
    st.markdown(
        """
        <div style='background-color: #1E293B; border: 1px solid #334155; border-radius: 8px; padding: 20px; text-align: center;'>
            <h3 style='color: #00FFCC; margin-0;'>🛠️ منطقة مسار الأبواب الستة الرئيسية</h3>
            <p style='color: #94A3B8; font-size: 14px;'>هنا سيتم عرض خطوات التقديم ورفع مخططات الـ CAD والـ BIM بعد المعاينة.</p>
        </div>
        """, 
        unsafe_allow_html=True
    )
