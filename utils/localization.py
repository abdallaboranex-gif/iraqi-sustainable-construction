import streamlit as st
from utils.locales.ar import AR_TRANSLATION
from utils.locales.en import EN_TRANSLATION
from utils.locales.ku import KU_TRANSLATION

# دمج القواميس الثلاثة المستقلة في مصفوفة لغوية موحدة ومؤمنة
DICTIONARY = {
    "ar": AR_TRANSLATION,
    "en": EN_TRANSLATION,
    "ku": KU_TRANSLATION
}

def get_text(key):
    """دالة قراءة اللغة الفعالة وسحب النص المقابل لها بالملي ثانية"""
    current_lang = st.session_state.get("language", "ar")
    # حماية بديلة باللغة العربية في حال عدم وجود المفتاح
    lang_dict = DICTIONARY.get(current_lang, DICTIONARY["ar"])
    return lang_dict.get(key, key)
