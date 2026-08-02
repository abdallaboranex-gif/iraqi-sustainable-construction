import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def handle_language_switch():
    new_lang = st.session_state.get("temp_lang_selector")
    if new_lang:
        st.session_state.language = new_lang

def render_header():
    """
    هيدر مبسط ومضخم الخطوط يعتمد على توزيع الأعمدة القياسي الصافي.
    """
    user_data = st.session_state.user_identity
    display_name = user_data["full_name"] if user_data["registered"] else get_text("Unregistered Account")
    display_rank = user_data["rank_title"] if user_data["registered"] else get_text("Click to Verify Identity")
    current_gov = st.session_state.property_data.get("governorate", "Baghdad")

    # حقن كود صارم لتكبير وتغميق كافة نصوص الهيدر والـ metrics
    st.markdown(
        """
        <style>
        /* تكبير وتغميق نصوص المنصة بالكامل */
        .stMarkdown div p, .stMarkdown div h2, .stMarkdown div h3, .stMarkdown div h4 {
            color: #0F172A !important;
            font-size: 20px !important;
            font-weight: 900 !important;
        }
        /* تكبير وتغميق أرقام بطاقة الموقع الحالي */
        [data-testid="stMetricValue"] {
            font-size: 26px !important;
            font-weight: 900 !important;
            color: #1D4ED8 !important;
        }
        /* تكبير وتغميق عناوين بطاقات المقياس */
        [data-testid="stMetricLabel"] p {
            font-size: 14px !important;
            font-weight: 800 !important;
            color: #475569 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # تقسيم المساحات بالتساوي لإعطاء النصوص مساحة كاملة تمنع التداخل
    col_brand, col_context, col_user = st.columns([4.0, 2.5, 2.5], gap="large")
    
    with col_brand:
        st.markdown(f"### Iraqi Green Construction Data Platform")
        st.markdown(f"**{get_text('Iraqi Green Construction Data Platform')}**")
        st.caption("DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY")
        
    with col_context:
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            st.metric(label=get_text("Current Location"), value=f"📍 {current_gov}")
        with sub_col2:
            st.markdown(f"**{get_text('Language')}**")
            lang_options = ["العربية", "EN"]
            current_lang = st.session_state.get("language", "العربية")
            default_idx = 1 if current_lang == "EN" else 0
            
            st.segmented_control(
                label="Language Selector", 
                options=lang_options, 
                default=lang_options[default_idx], 
                label_visibility="collapsed", 
                key="temp_lang_selector",
                on_change=handle_language_switch
            )

    with col_user:
        sub_col_avatar, sub_col_btn = st.columns([1.0, 3.0])
        with sub_col_avatar:
            avatar_src = user_data["avatar_url"] if user_data["avatar_url"] else "https://unsplash.com"
            st.image(avatar_src, width=55)
        with sub_col_btn:
            st.markdown(f"**{display_name}**")
            st.caption(display_rank)
            
        if st.button(get_text("Click to Verify Identity"), key="open_profile_drawer", use_container_width=True):
            st.session_state.show_profile_drawer = True
            
    if st.session_state.get("show_profile_drawer", False):
        with st.sidebar:
            if st.button(get_text("Close & Return"), use_container_width=True):
                st.session_state.show_profile_drawer = False
                st.rerun()
            st.markdown(f"## {get_text('Documentation & Legal Accountability Portal')}")
