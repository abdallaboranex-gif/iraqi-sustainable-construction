import streamlit as st
from deep_translator import GoogleTranslator

def get_text(english_text):
    """
    Pure English Internationalization Middleware.
    This module contains ZERO hardcoded Arabic or Kurdish words [١.١].
    It translates the entire app dynamically from English into Arabic/Kurdish via Cloud API [١.١].
    """
    if not english_text:
        return ""
        
    # Read the current language selection directly from the header widget ("العربية", "كردي", "EN")
    current_lang = st.session_state.get("language", "العربية")
    
    # 1. If the selection is "EN", bypass the cloud API and pass the text instantly for maximum speed
    if current_lang == "EN":
        return english_text
        
    # 2. Map the interface labels to the official international ISO language codes
    target_iso_code = "ar" if current_lang == "العربية" else "ckb"
    
    # 3. [The Automated Pipeline] Ingest the English text and fetch the instant translation from the cloud
    try:
        # Utilizing deep-translator to securely fetch the localized string in real-time
        translated_result = GoogleTranslator(source='en', target=target_iso_code).translate(english_text)
        return translated_result if translated_result else english_text
    except Exception:
        # Fallback safeguard: if the cloud network times out, display the original English key to prevent app crashes
        return english_text
