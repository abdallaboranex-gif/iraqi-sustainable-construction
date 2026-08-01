import streamlit as st

# مصفوفة القاموس الثلاثي السيادي لإدارة المصطلحات باللغات الثلاث
DICTIONARY = {
    "ar": {
        "title": "منصة البناء المستدام",
        "btn_portal_1": "🚪 الباب 1\nالتدقيق والتربة",
        "btn_portal_2": "🌱 الباب 2\nالطاقة والاستدامة",
        "btn_portal_3": "📊 الباب 3\nحصر المواد المركزي",
        "btn_portal_4": "🗺️ الباب 4\nخارطة GIS العراق",
        "btn_portal_5": "💳 الباب 5\nالبنية والمالية",
        "btn_portal_6": "🦺 الباب 6\nالسلامة الموقعية",
        "nav_title": "🎛️ لوحة التحكم السيادية للمنصة",
        "compliance_score": "المطابقة الهندسية",
        "energy_score": "استدامة الطاقة",
        "integrity_score": "السلامة الإنشائية",
        "footer_text": "منصة البناء المستدام © 2026 - جميع الحقوق محفوظة | متوافق مع المدونات العراقية"
    },
    "en": {
        "title": "Iraqi Green Construction Data Platform",
        "btn_portal_1": "🚪 Portal 1\nZoning & Soil Test",
        "btn_portal_2": "🌱 Portal 2\nEnergy & Green Score",
        "btn_portal_3": "📊 Portal 3\nCentral Materials BOQ",
        "btn_portal_4": "🗺️ Portal 4\nIraq GIS Map View",
        "btn_portal_5": "💳 Portal 5\nFinance & Payback",
        "btn_portal_6": "🦺 Portal 6\nField Site Safety",
        "nav_title": "🎛️ Platform Sovereign Control Panel",
        "compliance_score": "Engineering Compliance",
        "energy_score": "Energy Score",
        "integrity_score": "Structural Integrity",
        "footer_text": "Iraqi Green Construction Data Platform © 2026 - All Rights Reserved | Compliant with National Codes"
    },
    "ku": {
        "title": "سەکۆی بیناسازی بەردەوام",
        "btn_portal_1": "🚪 دەروازەی ١\nپشکنینی خاک",
        "btn_portal_2": "🌱 دەروازەی ٢\nوزە و بەردەوامی",
        "btn_portal_3": "📊 دەروازەی ٣\nکۆکردنەوەی ماددەکان",
        "btn_portal_4": "🗺️ دەروازەی ٤\nنەخشەی جی ئێس",
        "btn_portal_5": "💳 دەروازەی ٥\nدارایی و قازانج",
        "btn_portal_6": "🦺 دەروازەی ٦\nسەلامەتی مەیدانی",
        "nav_title": "🎛️ لۆگۆی کۆنترۆڵی سیادی سەکۆکە",
        "compliance_score": "گونجانی ئەندازیاری",
        "energy_score": "بەردەوامی وزە",
        "integrity_score": "سەلامەتی پێکهاتەیی",
        "footer_text": "سەکۆی بیناسازی بەردەوام © 2026 - هەموو مافەکان پارێزراون | هاوتایە لەگەڵ کۆدەکانی عێراق"
    }
}

def get_text(key):
    """دالة قراءة اللغة الفعالة حالياً وسحب نصها المقابل لحظياً"""
    current_lang = st.session_state.get("language", "ar")
    # حماية بديلة في حال لم يعثر على الكلمة المفتاحية
    return DICTIONARY.get(current_lang, DICTIONARY["ar"]).get(key, key)
