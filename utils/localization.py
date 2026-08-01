import streamlit as st

# مصفوفة القاموس الثلاثي لإدارة المصطلحات الهندسية للمنصة
DICTIONARY = {
    "ar": {
        "title": "منصة البناء المستدام",
        "compliance_score": "المطابقة الهندسية",
        "energy_score": "استدامة الطاقة",
        "integrity_score": "السلامة الإنشائية",
        "footer_text": "منصة البناء المستدام © 2026 - جميع الحقوق محفوظة | متوافق مع المدونات العراقية" [١.١]
    },
    "en": {
        "title": "Iraqi Green Construction Data Platform",
        "compliance_score": "Engineering Compliance",
        "energy_score": "Energy Score",
        "integrity_score": "Structural Integrity",
        "footer_text": "Iraqi Green Construction Data Platform © 2026 - All Rights Reserved | Compliant with National Codes"
    },
    "ku": {
        "title": "سەکۆی بیناسازی بەردەوام",
        "compliance_score": "گونجانی ئەندازیاری",
        "energy_score": "بەردەوامی وزە",
        "integrity_score": "سەلامەتی پێکهاتەیی",
        "footer_text": "سەکۆی بیناسازی بەردەوام © 2026 - هەموو مافەکان پارێزراون | هاوتایە لەگەڵ کۆدەکانی عێراق"
    }
}

def get_text(key):
    """دالة قراءة اللغة الفعالة حالياً وسحب نصها المقابل من القاموس البرمجي"""
    current_lang = st.session_state.get("language", "ar")
    # البحث عن الكلمة المفتاحية وتوفير حماية بديلة في حال عدم وجودها
    return DICTIONARY.get(current_lang, DICTIONARY["ar"]).get(key, key)
