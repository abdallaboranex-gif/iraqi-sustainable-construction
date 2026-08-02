import streamlit as st
from deep_translator import GoogleTranslator

@st.cache_data(show_spinner=False, max_entries=1000, ttl=86400)
def fetch_cached_translation(text: str, target_lang: str) -> str:
    """
    Isolated In-Memory Cache Core.
    Intercepts dynamic translator requests and preserves tokens in server RAM.
    Eliminates repetitive HTTP network requests and stops page latency loops.
    """
    try:
        # Secure automated single text translation via heavy global pipeline
        translated = GoogleTranslator(source='en', target=target_lang).translate(text)
        return translated if translated else text
    except Exception:
        # Absolute structural fail-safe fallback to prevent platform crash
        return text

def get_text(english_key: str) -> str:
    """
    Universal Localization Engine Middleware.
    Strictly follows the Iraqi Green Construction Data Platform architecture:
    - 100% Pure Standard English keys processed dynamic on-the-fly [1.1]
    - Zero static dictionary clutter or hardcoded manual arrays [1.1]
    - Dynamic session switching between Arabic (العربية) and Kurdish (كردي) [1.1]
    - Wrapped around fetch_cached_translation to deliver instant zero-lag rendering [1.1]
    """
    # Safeguard 1: Safe fallback if session state variables are momentarily uninitialized
    if "language" not in st.session_state:
        return english_key

    selected_language = st.session_state.language

    # Structural mapping matrix to convert platform session choices to ISO-639 codes
    if selected_language == "العربية":
        target_iso = "ar"
    elif selected_language == "كردي":
        target_iso = "ku"
    else:
        # Fallback benchmark for pure English or unrecognized language configurations
        return english_key

    # Safeguard 2: Instantly bypass empty keys or whitespace inputs to protect network socket
    if not english_key.strip():
        return english_key

    # Trigger the highly accelerated cached memory query engine
    return fetch_cached_translation(text=english_key, target_lang=target_iso)
