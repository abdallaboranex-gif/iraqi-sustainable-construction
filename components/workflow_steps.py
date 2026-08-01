import streamlit as st

def render_workflow_steps():
    """
    مكون الخطوات الزمنية والتسلسل الصارم للأبواب الستة.
    يعرض حالة كل بوابة (مكتملة بالـ QR، نشطة للرفع، مقفلة بالقفل).
    """
    st.markdown("<h3 style='color: #F8FAFC; font-size: 20px; margin-bottom: 20px;'>🏗️ مسار حوكمة رخصة البناء المستدام</h3>", unsafe_allow_html=True)
    
    # جلب الخطوة الحالية النشطة من الذاكرة السحابية للمنصة
    current_step = st.session_state.property_data.get("current_step", 2)
    
    # تعريف البوابات الستة وأسمائها القانونية باللغتين
    steps_definition = [
        {"id": 1, "title": "الباب الأول: التدقيق الإنشائي الأولي", "sub": "Site Compliance & Initial Zoning"},
        {"id": 2, "title": "الباب الثاني: فحص التربة وتصميم الأسس", "sub": "Soil Mechanics & Foundations Design"},
        {"id": 3, "title": "الباب الثالث: إدارة الطاقة والاستدامة والعزل", "sub": "Energy Score & Thermal Insulation"},
        {"id": 4, "title": "الباب الرابع: التجميع المركزي وحصر المواد", "sub": "Materials Aggregator & Granular BOQ"},
        {"id": 5, "title": "الباب الخامس: الجدوى وحاسبات الكلفة التشغيلية", "sub": "Financial Engineering & Payback Period"},
        {"id": 6, "title": "الباب السادس: السلامة الموقعية وواقع الحال", "sub": "Field Safety & Site Reality Audit"}
    ]
    
    # المرور على البوابات الستة برمجياً ورسمها بناءً على حالتها في السحاب
    for step in steps_definition:
        step_id = step["id"]
        
        # الحالة الأولى: البوابة مكتملة ومطابقة تماماً (اللون الأخضر)
        if step_id < current_step:
            with st.container(border=True):
                col_text, col_action = st.columns([4, 1.5])
                with col_text:
                    st.markdown(
                        f"""
                        <div style='display: flex; align-items: center; gap: 10px;'>
                            <div style='width: 24px; height: 24px; background-color: #10B981; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #0F172A; font-weight: bold; font-size: 12px;'>✓</div>
                            <div>
                                <strong style='color: #10B981; font-size: 15px;'>{step['title']}</strong>
                                <span style='color: #64748B; font-size: 11px; display: block;'>{step['sub']}</span>
                            </div>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                with col_action:
                    # زر ذكي لتحميل تقرير الـ PDF الموثق بالـ QR Code للخطوة المكتملة
                    st.button(f"📥 تقرير PDF المعتمد", key=f"pdf_btn_{step_id}", use_container_width=True)
                    
        # الحالة الثانية: البوابة نشطة حالياً وتنتظر رفع المخططات (اللون السحري الفوسفوري)
        elif step_id == current_step:
            st.markdown(
                f"""
                <div style='background-color: #1E293B; border: 2px solid #00FFCC; border-radius: 8px; padding: 15px; margin-bottom: 12px;'>
                    <div style='display: flex; align-items: center; gap: 10px; margin-bottom: 10px;'>
                        <div style='width: 24px; height: 24px; background-color: #00FFCC; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #0F172A; font-weight: bold; font-size: 12px;'>➔</div>
                        <div>
                            <strong style='color: #00FFCC; font-size: 16px;'>{step['title']} (الخطوة الحالية)</strong>
                            <span style='color: #94A3B8; font-size: 12px; display: block;'>{step['sub']}</span>
                        </div>
                    </div>
                </div>
                """, 
                unsafe_allow_html=True
            )
            
            # حقن مكون صندوق الرفع الذكي (Drag & Drop) مؤقتاً داخل الخطوة النشطة
            with st.container(border=False):
                uploaded_file = st.file_uploader(
                    label="ارفع تقرير المختبر المعتمد أو مخططات الـ CAD/BIM (.dwg, .rvt, .pdf)",
                    type=["pdf", "dwg", "rvt"],
                    key=f"uploader_{step_id}",
                    help="الحد الأقصى لحجم الملف 50 ميجابايت وفقاً لإعدادات السيرفر القياسية"
                )
                if uploaded_file is not None:
                    st.success("🔄 جاري إرسال الملف إلى الـ Sandbox وتفكيك الطبقات برمجياً...")
                    
            st.markdown("</div>", unsafe_allow_html=True) # إغلاق حاوية الخطوة النشطة
            
        # الحالة الثالثة: البوابة مقفلة ولا يمكن تجاوز النظام لها (اللون الرمادي الصارم)
        else:
            with st.container(border=True):
                st.markdown(
                    f"""
                    <div style='display: flex; align-items: center; justify-content: space-between; opacity: 0.4;'>
                        <div style='display: flex; align-items: center; gap: 10px;'>
                            <div style='width: 24px; height: 24px; background-color: #334155; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: #94A3B8; font-weight: bold; font-size: 12px;'>{step_id}</div>
                            <div>
                                <strong style='color: #94A3B8; font-size: 15px;'>{step['title']}</strong>
                                <span style='color: #64748B; font-size: 11px; display: block;'>{step['sub']}</span>
                            </div>
                        </div>
                        <div style='color: #64748B; font-size: 18px;'>🔒</div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
