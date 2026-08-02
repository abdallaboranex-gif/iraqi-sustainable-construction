import streamlit as st

def get_text(english_key: str) -> str:
    """
    Universal Localization Engine Middleware (Sovereign Static Override Blueprint).
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys passed to get_text() from app.py [1.1]
    - Completely bypasses external cloud translator latency and memory cache locks [1.1]
    - Delivers exact, pixel-perfect official Iraqi green building terminology [1.1]
    """
    # Safeguard 1: Safe fallback if session state variables are momentarily uninitialized
    if "language" not in st.session_state:
        return english_key

    selected_language = st.session_state.language

    # If pure English layout mode is selected, bypass mapping metrics entirely in 0.0 seconds
    if selected_language != "العربية":
        return english_key

    # Core Sovereign Translation Matrix - Hard-locked to eliminate any automated cloud distortion
    sovereign_dictionary = {
        "Platform Navigation": "لوحة التنقل في المنصة",
        "Main Dashboard": "لوحة التحكم الرئيسية",
        "Compliance Audits": "مطابقة الكودات الهندسية العراقية",
        "Energy Management": "ادارة الطاقة والاستدامة",
        "Data Center": "مركز البيانات",
        "Telemetry Indicators": "لوحة التحكم والموشرات",
        "Digital Payments": "تفعيل الاشتراك والدفع الرقمي",
        "Site Safety": "ادارة السلامة الموقعية والبيئية",
        "Language": "اللغة",
        "Current Location": "الموقع الحالي",
        "Unregistered Account": "حساب غير مسجل",
        "Click to Verify Identity": "اضغط للتحقق من الهوية",
        "Close & Return": "إغلاق والعودة"
    }

    # Safeguard 2: Return the mapped token if exists, otherwise fallback safely to the english key
    return sovereign_dictionary.get(english_key, english_key)
