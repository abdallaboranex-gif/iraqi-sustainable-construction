import streamlit as st

def initialize_session_state():
    """
    State Manager: Sovereign Session State Registry.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys [1.1]
    - Absolute blank context tracking initialized with 0.0 values or empty vectors [1.1]
    - Single source of truth for dynamic internationalization logic [1.1]
    - Correct signature naming to resolve the Streamlit Cloud execution crash [1.1]
    """
    
    # 1. Universal Localization Variable Lock (Defaults to English sovereign key)
    if "language" not in st.session_state:
        st.session_state.language = "EN"
        
    # 2. Central Navigation Variable Pointer (Synchronized with core/router.py)
    if "current_page" not in st.session_state:
        st.session_state.current_page = "Main Dashboard"
        
    # 3. Purged Absolute Zero Audit Pipeline Log Sequence
    if "audit_log" not in st.session_state:
        st.session_state.audit_log = []
        
    # 4. Sovereign User Identity Registration Profile (Fully Cleaned & Staged)
    if "user_identity" not in st.session_state:
        st.session_state.user_identity = {
            "registered": False,
            "full_name": "",
            "rank_title": "Guest Contributor",
            "national_id": "",
            "syndicate_id": "",
            "avatar_url": "",
            "days_left": 0.0,  # Enforced clean 0.0 float baseline boundary [1.1]
            "projects_list": []
        }
        
    # 5. Zero-State Regional GIS Property Boundary Footprints
    if "property_data" not in st.session_state:
        st.session_state.property_data = {
            "governorate": "",
            "district": "",
            "zoning_type": "",
            "is_compliant": False,
            "built_area": 0.0,  # Enforced clean 0.0 float baseline boundary [1.1]
            "floors": 0
        }

def log_action(user_credential: str, action_details: str):
    """
    Isolated backend event logging interceptor using standardized timestamp tracking.
    """
    import datetime
    if "audit_log" in st.session_state:
        st.session_state.audit_log.append({
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user": user_credential,
            "action": action_details
        })
