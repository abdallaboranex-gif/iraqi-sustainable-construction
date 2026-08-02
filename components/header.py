import streamlit as st
from utils.localization import get_text
from core.state_manager import log_action

def handle_language_switch():
    new_lang = st.session_state.get("temp_lang_selector")
    if new_lang:
        st.session_state.language = new_lang

@st.dialog("Sovereign Identity Registration")
def render_identity_dialog():
    """
    نافذة توثيق الهوية والمسؤولية القانونية المنبثقة في منتصف الشاشة.
    مصفاة بالكامل ومحمية من تضارب الأشرطة الجانبية.
    """
    user_data = st.session_state.user_identity
    
    st.markdown(f"### 🛡️ {get_text('Documentation & Legal Accountability Portal')}")
    st.markdown(f"<p style='color: #475569; font-size: 13px;'>{get_text('Official IDs must be uploaded to bear full legal accountability for the data and engineering blueprints.')}</p>", unsafe_allow_html=True)
    
    if not user_data["registered"]:
        st.markdown(f"<h4 style='color: #1D4ED8; font-size: 15px;'>{get_text('Create Register:')}</h4>", unsafe_allow_html=True)
        input_name = st.text_input(get_text("User's Full Quadruple Name:"), placeholder="Eng. Abdulla Omar")
        user_role = st.selectbox(get_text("Technical Role in the Project:"), ["Consultant Engineer", "Property Owner", "Certified Contractor"])
        input_nid = st.text_input(get_text("National Unified ID Number (12 Digits):"), max_chars=12, placeholder="199204358112")
        
        if st.button(get_text("Approve, Verify Identity & Launch Sovereign Permissions"), use_container_width=True, type="primary"):
            if input_name and input_nid:
                st.session_state.user_identity["registered"] = True
                st.session_state.user_identity["full_name"] = input_name
                st.session_state.user_identity["rank_title"] = get_text(user_role)
                st.session_state.user_identity["national_id"] = input_nid
                
                log_action(user_credential=input_name, action_details="Registered official digital ID profile.")
                st.success(get_text("Verified Successfully!"))
                st.rerun()
            else:
                st.warning(get_text("Required Fields!"))
    else:
        st.markdown(f"<h4 style='color: #10B981; font-size: 15px;'>✔️ {get_text('Identity Verified Status')}</h4>", unsafe_allow_html=True)
        st.text_input(get_text("Registered Operator Nominee"), value=user_data["full_name"], disabled=True)
        st.text_input(get_text("Sovereign Technical Rank"), value=user_data["rank_title"], disabled=True)
        
        if st.button(get_text("Revoke Profile Authorization Logs"), use_container_width=True, type="primary"):
            st.session_state.user_identity["registered"] = False
            log_action(user_credential=user_data["full_name"], action_details="Revoked operator profile context.")
            st.rerun()

def render_header():
    """
    هيدر مغلظ الخطوط ومنسق التوزيع أفقياً مع زر تفعيل نافذة الحساب المنبثقة.
    """
    user_data = st.session_state.user_identity
    display_name = user_data["full_name"] if user_data["registered"] else get_text("Unregistered Account")
    display_rank = user_data["rank_title"] if user_data["registered"] else get_text("Click to Verify Identity")
    current_gov = st.session_state.property_data.get("governorate", "Baghdad")

    # حقن ستايل الكحلي الداكن الغامق والخطوط العريضة لضمان وضوح وتناسق القراءة
    st.markdown(
        """
        <style>
        .header-main-title { color: #0F172A !important; font-size: 24px !important; font-weight: 900 !important; margin: 0 !important; line-height: 1.2 !important; }
        .header-sub-title { color: #0F172A !important; font-size: 16px !important; font-weight: 800 !important; margin: 4px 0 0 0 !important; }
        .header-slogan-text { color: #475569 !important; font-size: 11px !important; font-weight: 700 !important; letter-spacing: 1px !important; margin: 6px 0 0 0 !important; }
        
        .clean-location-card { text-align: center !important; margin-top: 10px !important; }
        .clean-location-label { color: #475569 !important; font-size: 13px !important; font-weight: 800 !important; display: block !important; }
        .clean-location-value { color: #1D4ED8 !important; font-size: 18px !important; font-weight: 900 !important; display: block !important; margin-top: 4px !important; }
        
        .clean-user-panel { text-align: right !important; margin-top: 2px !important; }
        .clean-user-name { color: #0F172A !important; font-size: 16px !important; font-weight: 900 !important; display: block !important; }
        .clean-user-rank { color: #475569 !important; font-size: 12px !important; font-weight: 700 !important; display: block !important; margin-top: 2px !important; }
        
        .flat-user-avatar {
            background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://w3.org" viewBox="0 0 24 24" fill="%231D4ED8"><path d="M12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 2 12 2ZM12 4C14.2091 4 16 5.79086 16 8C16 10.2091 14.2091 12 12 12C9.79086 12 8 10.2091 8 8C8 5.79086 9.79086 4 12 4ZM12 14C16.4183 14 20 16.4183 20 19H4C4 16.4183 7.58172 14 12 14Z"/></svg>');
            display: inline-block; width: 44px; height: 44px; border-radius: 50%; border: 2px solid #1D4ED8;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    col_brand, col_context, col_user = st.columns([3.6, 2.0, 2.4], gap="medium")
    
    with col_brand:
        st.markdown('<div class="header-main-title">Iraqi Green Construction Data Platform</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="header-sub-title">{get_text("Iraqi Green Construction Data Platform")}</div>', unsafe_allow_html=True)
        st.markdown('<div class="header-slogan-text">DATA • COMPLIANCE • SUSTAINABILITY • EFFICIENCY</div>', unsafe_allow_html=True)
        
    with col_context:
        sub_col_loc, sub_col_lang = st.columns([1.0, 1.0], gap="small")
        with sub_col_loc:
            st.markdown(f'<div class="clean-location-card"><span class="clean-location-label">{get_text("Current Location")}</span><strong class="clean-location-value">📍 {get_text(current_gov)}</strong></div>', unsafe_allow_html=True)
        with sub_col_lang:
            st.markdown(f"<span style='color: #0F172A; font-size: 13px !important; font-weight: 800; display: block; margin-top: 8px; text-align: center;'>{get_text('Language')}</span>", unsafe_allow_html=True)
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
        sub_col_text, sub_col_img = st.columns([2.2, 0.8])
        with sub_col_text:
            st.markdown(f'<div class="clean-user-panel"><span class="clean-user-name">{display_name}</span><span class="clean-user-rank">{display_rank}</span></div>', unsafe_allow_html=True)
        with sub_col_img:
            st.markdown('<div class="flat-user-avatar"></div>', unsafe_allow_html=True)
            
        # تفعيل استدعاء النافذة المنبثقة الذكية فوراً عند الضغط لكسر تعليق التداخل الجانبي
        if st.button(get_text("Click to Verify Identity"), key="open_profile_drawer", use_container_width=True):
            render_identity_dialog()
