import streamlit as st
from deep_translator import GoogleTranslator

@st.cache_data(show_spinner=False, max_entries=1000, ttl=86400)
def fetch_online_fallback_translation(text: str, target_lang: str) -> str:
    """
    Emergency online translator fallback to process remaining fields 
    across all portals and dashboard metrics dynamically.
    """
    try:
        translated = GoogleTranslator(source='en', target=target_lang).translate(text)
        return translated if translated else text
    except Exception:
        return text

def get_text(english_key: str) -> str:
    """
    Universal Localization Engine Middleware (Hybrid Sovereign Architecture).
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - Enforces exact user-defined official nomenclature for top-level navigation.
    - Routes all remaining dynamic form text inputs to the cached translation pipeline.
    """
    # Safeguard 1: Safe fallback if session state variables are momentarily uninitialized
    if "language" not in st.session_state:
        return english_key

    selected_language = st.session_state.language

    # If pure English layout mode is selected, bypass mapping metrics entirely in 0.0 seconds
    if selected_language != "العربية":
        return english_key

    if not english_key.strip():
        return english_key

    # 1. HARD-LOCKED SOVEREIGN DICTIONARY (Takes absolute precedence for exact text execution)
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

    # If the key is officially defined in our sovereign core block, return it immediately (0.0ms)
    if english_key in sovereign_dictionary:
        return sovereign_dictionary[english_key]

    # 2. AUTOMATED CASCADE (Translates the rest of the building portals automatically via cloud network)
    return fetch_online_fallback_translation(text=english_key, target_lang="ar")
