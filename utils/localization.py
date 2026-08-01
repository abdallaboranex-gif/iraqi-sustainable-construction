import streamlit as st

# 1. قاموس المصطلحات والـ 13 حقل باللغة العربية
AR_DICTIONARY = {
    # الهيدر ولوحة التحكم العامة
    "platform_title": "منصة البناء المستدام",
    "platform_sub": "الحوكمة الرقمية والامتثال البيئي",
    "nav_title": "🎛️ لوحة التحكم السيادية للمنصة",
    "current_location": "الموقع الحالي",
    "lang_label": "اللغة",
    
    # أزرار الأبواب الستة الرئيسية
    "btn_portal_1": "🚪 الباب 1\nالتدقيق والتربة",
    "btn_portal_2": "🌱 الباب 2\nالطاقة والاستدامة",
    "btn_portal_3": "📊 الباب 3\nحصر المواد المركزي",
    "btn_portal_4": "🗺️ الباب 4\nخارطة GIS العراق",
    "btn_portal_5": "💳 الباب 5\nالبنية والمالية",
    "btn_portal_6": "🦺 الباب 6\nالسلامة الموقعية",
    
    # لوحة المؤشرات الاستراتيجية الجانبية
    "side_title": "📊 لوحة المؤشرات الحية",
    "compliance_score": "المطابقة الهندسية / Compliance",
    "integrity_score": "السلامة الإنشائية / Integrity",
    "energy_score": "استدامة الطاقة / Energy Score",
    
    # بوابة الهوية والمسؤولية القانونية
    "user_unregistered": "حساب غير مسجل",
    "user_action_verify": "اضغط لتأكيد الهوية",
    "drawer_title": "🔐 بوابة التوثيق والمسؤولية القانونية",
    "drawer_desc": "يجب إكمال رفع الهويات الرسمية لتتحمل المسؤولية القانونية الكاملة عن البيانات والمخططات الهندسية.",
    "lbl_user_name": "الاسم الرباعي الكامل للمخدم:",
    "lbl_user_role": "الصفة الفنية في المشروع:",
    "lbl_national_id": "رقم البطاقة الوطنية الموحدة (12 رقماً):",
    "lbl_syndicate_id": "رقم هوية نقابة المهندسين العراقية النافذة:",
    "lbl_upload_avatar": "ارفع صورتك الشخصية الرسمية (PNG/JPG):",
    "btn_submit_auth": "🔒 اعتماد وتوثيق الهوية وإطلاق الصلاحيات السيادية",
    "badge_verified": "🛡️ حساب موثق سيادياً ونقابياً | Professional Verified",
    "badge_desc": "المرتبة المعتمدة: مهندس استشاري مرخص",
    "crypto_notice": "*الحقول مشفرة عسكرياً بموجب AES-256 لحماية سرية المعلومات الشخصية.*",
    "btn_reset": "🔄 خروج وتصفير السجل التجريبي (Reset)",
    
    # البوابة الأولى: الـ 13 حقل والفلترة الجغرافية
    "title_p1": "📋 الباب الأول: تحليل الموقع ومحددات البلدية",
    "desc_p1": "يرجى ملء الحقول الـ 13 بدقة لتحديد متطلبات فحص التربة والمدونات الهندسية الإلزامية لمشروعك وفقاً للوائح العراقية.",
    "lbl_gov": "1. المحافظة",
    "lbl_district": "2. القضاء / الناحية",
    "lbl_zoning": "3. تصنيف جنس العقار (البلدية)",
    "lbl_plot": "4. رقم القطعة والمقاطعة",
    "lbl_area": "5. المساحة الكلية للأرض (متر مربع)",
    "lbl_built_area": "6. مساحة البناء الطابقي (متر مربع)",
    "lbl_floors": "7. عدد الطوابق الكلي",
    "lbl_height": "8. الارتفاع الكلي للمبنى (متر)",
    "lbl_basement": "9. هل يحتوي المبنى على سرداب (قبو)؟",
    "lbl_offset_f": "10. الارتداد الأمامي القانوني (متر)",
    "lbl_offset_s": "11. الارتدادات الجانبية والخلفية (متر)",
    "lbl_adjacent": "12. طبيعة الملاصقة والأبنية المجاورة",
    "lbl_structure": "13. النظام الإنشائي المقترح للهيكل",
    
    # محرك اتخاذ القرار والرسائل
    "btn_trigger_compliance": "🚀 تشغيل محرك المطابقة الفوري وفحص القيود",
    "warning_empty_fields": "⚠️ يرجى ملء كافة البيانات الجغرافية والإنشائية الـ 13 أولاً؛ لا يمكن تشغيل محرك المطابقة على حقول فارغة!",
    "success_msg": "✅ تهانينا! المخطط الأولي مطابق تماماً لكافة قيود البناء والمدونات المعتمدة جغرافياً في بلدية المنطقة.",
    "error_msg": "❌ تم رصد مخالفات صريحة لشروط البناء والمدونات الوطنية! تم تجميد المعاملة وقفل شهادة التوصية بالإجازة إلكترونياً."
}
# 2. قاموس المصطلحات والـ 13 حقل باللغة الإنكليزية
EN_DICTIONARY = {
    "platform_title": "Iraqi Green Construction Data Platform",
    "platform_sub": "Digital Governance & Environmental Compliance",
    "nav_title": "🎛️ Platform Sovereign Control Panel",
    "current_location": "Current Location",
    "lang_label": "Language",
    
    "btn_portal_1": "🚪 Portal 1\nZoning & Soil Test",
    "btn_portal_2": "🌱 Portal 2\nEnergy & Green Score",
    "btn_portal_3": "📊 Portal 3\nCentral Materials BOQ",
    "btn_portal_4": "🗺️ Portal 4\nIraq GIS Map View",
    "btn_portal_5": "💳 Portal 5\nFinance & Payback",
    "btn_portal_6": "🦺 Portal 6\nField Site Safety",
    
    "side_title": "📊 Live Indicators Panel",
    "compliance_score": "Engineering Compliance",
    "integrity_score": "Structural Integrity",
    "energy_score": "Energy Score",
    
    "user_unregistered": "Unregistered Account",
    "user_action_verify": "Click to Verify Identity",
    "drawer_title": "🔐 Documentation & Legal Accountability Portal",
    "drawer_desc": "Official IDs must be uploaded to bear full legal accountability for the data and engineering blueprints.",
    "lbl_user_name": "User's Full Quadruple Name:",
    "lbl_user_role": "Technical Role in the Project:",
    "lbl_national_id": "National Unified ID Number (12 Digits):",
    "lbl_syndicate_id": "Valid Iraqi Engineers Syndicate ID Number:",
    "lbl_upload_avatar": "Upload Your Official Profile Photo (PNG/JPG):",
    "btn_submit_auth": "🔒 Approve, Verify Identity & Launch Sovereign Permissions",
    "badge_verified": "🛡️ Account Verified Sovereignly and النقابية | Professional Verified",
    "badge_desc": "Approved Rank: Licensed Consultant Engineer",
    "crypto_notice": "*Fields are encrypted military-grade via AES-256 to protect personal data confidentiality.*",
    "btn_reset": "🔄 Logout & Reset Empirical Log",
    
    "title_p1": "📋 Portal 1: Site Analysis & Municipal Constraints",
    "desc_p1": "Please fill out the 13 fields accurately to determine soil test requirements and mandatory engineering codes for your project in accordance with Iraqi regulations.",
    "lbl_gov": "1. Governorate",
    "lbl_district": "2. District / Sub-district",
    "lbl_zoning": "3. Land Zoning Type (Municipality)",
    "lbl_plot": "4. Plot & Sector Number",
    "lbl_area": "5. Total Land Area (sqm)",
    "lbl_built_area": "6. Built-up Footprint Area (sqm)",
    "lbl_floors": "7. Total Number of Floors",
    "lbl_height": "8. Total Building Height (meters)",
    "lbl_basement": "9. Does the building contain a basement?",
    "lbl_offset_f": "10. Legal Front Offset (meters)",
    "lbl_offset_s": "11. Side and Rear Offsets (meters)",
    "lbl_adjacent": "12. Type of Adjacent Buildings",
    "lbl_structure": "13. Proposed Structural System",
    
    "btn_trigger_compliance": "🚀 Trigger Instant Compliance Engine & Check Constraints",
    "warning_empty_fields": "⚠️ Please fill out all 13 geographical and structural fields first; the compliance engine cannot run on empty fields!",
    "success_msg": "✅ Congratulations! The initial blueprint complies with all building restrictions and approved national codes.",
    "error_msg": "❌ Explicit violations detected against municipal zoning and national codes! File frozen and recommendation certificate locked electronically."
}
# 3. قاموس المصطلحات والـ 13 حقل باللغة الكردية الصافية
KU_DICTIONARY = {
    "platform_title": "سەکۆی بیناسازی بەردەوام",
    "platform_sub": "حوکمڕانی دیجیتاڵی و پابەندبوونی ژینگەیی",
    "nav_title": "🎛️ لۆگۆی کۆنترۆڵی سیادی سەکۆکە",
    "current_location": "شوێنی ئێستا",
    "lang_label": "زمان",
    
    "btn_portal_1": "🚪 دەروازەی ١\nپشکنینی خاک",
    "btn_portal_2": "🌱 دەروازەی ٢\nوزە و بەردەوامی",
    "btn_portal_3": "📊 دەروازەی ٣\nکۆکردنەوەی ماددەکان",
    "btn_portal_4": "🗺️ دەروازەی ٤\nنەخشەی جی ئێس",
    "btn_portal_5": "💳 دەروازەی ٥\nدارایی و قازانج",
    "btn_portal_6": "🦺 دەروازەی ٦\nسەلامەتی مەیدانی",
    
    "side_title": "📊 پانێڵی نیشاندەرە زیندووەکان",
    "compliance_score": "گونجانی ئەندازیاری",
    "integrity_score": "سەلامەتی پێکهاتەیی",
    "energy_score": "بەردەوامی وزە",
    
    "user_unregistered": "هەژماری تۆمارنەکراو",
    "user_action_verify": "کلیک بکە بۆ پشتڕاستکردنەوەی ناسنامە",
    "drawer_title": "🔐 دەروازەی بەڵگەنامە و بەرپرسیارێتی یاسایی",
    "drawer_desc": "پێویستە ناسنامە فەرمییەکان بەرزبکرێنەوە بۆ لەئەستۆگرتنی بەرپرسیارێتی یاسایی تەواو لەسەر زانیاری و نەخشە ئەندازیارییەکان.",
    "lbl_user_name": "ناوی چوارینەی تەواوی بەکارهێنەر:",
    "lbl_user_role": "ڕۆڵی تەکنیکی لە پڕۆژەکەدا:",
    "lbl_national_id": "ژمارەی ناسنامەی نیشتمانی یەکگرتوو (١٢ ژمارە):",
    "lbl_syndicate_id": "ژمارەی ناسنامەی کارای سەندیکای ئەندازیارانی عێراق:",
    "lbl_upload_avatar": "وێنەی پرۆفایلی فەرمی خۆت بەرزبکەرەوە (PNG/JPG):",
    "btn_submit_auth": "🔒 پەسەندکردن، پشتڕاستکردنەوەی ناسنامە و دەستپێکردنی مۆڵەتە سیادییەکان",
    "badge_verified": "🛡️ هەژمارەکە بە شێوەیەکی سیادی و سەندیکایی پشتڕاستکراوەتەوە",
    "badge_desc": "پلەی پەسەندکراو: ئەندازیاری ڕاوێژکاری مۆڵەتپێدراو",
    "crypto_notice": "*خانەکان بە شێوازی سەربازی لە ڕێگەی AES-256ـەوە کۆدکراون بۆ پاراستنی نهێنی زانیارییە کەسییەکان.*",
    "btn_reset": "🔄 چوونەدەرەوە و تصفیرکردنی تۆماری تاقیکاری",
    
    "title_p1": "📋 دەروازەی یەکەم: شیکردنەوەی شوێن و سنووردارکردنی شارەوانی",
    "desc_p1": "تکایە ١٣ خانەکە بە دروستی پڕبکەرەوە بۆ دیاریکردنی پێویستییەکانی پشکنینی خاک و کۆدەکانی ئەندازیاری زۆرەملێ بۆ پڕۆژەکەت بەپێی ڕێساکانی عێراق.",
    "lbl_gov": "١. پارێزگا",
    "lbl_district": "٢. قەزا / ناحیە",
    "lbl_zoning": "٣. پۆلێنکردنی زەوی (شارەوانی)",
    "lbl_plot": "٤. ژمارەی پارچە زەوی و کەرت",
    "lbl_area": "٥. ڕووبەری گشتی زەوی (مەتر دووجا)",
    "lbl_built_area": "٦. ڕووبەری بیناسازی نهۆمی (مەتر دووجا)",
    "lbl_floors": "٧. ژمارەی گشتی نهۆمەکان",
    "lbl_height": "٨. بەرزی گشتی بیناکە (مەتر)",
    "lbl_basement": "٩. ئایا بیناکە ژێرزەمینی تێدایە؟",
    "lbl_offset_f": "١٠. کشانەوەی پێشەوەی یاسایی (مەتر)",
    "lbl_offset_s": "١١. کشانەوەی تەنیشت و دواوە (مەتر)",
    "lbl_adjacent": "١٢. سروشتی تەنیشت و بینا هاوسێیەکان",
    "lbl_structure": "١٣. سیستەمی پێکهاتەیی پێشنیارکراو بۆ چوارچێوەکە",
    
    "btn_trigger_compliance": "🚀 دەستپێکردنی بزوێنەری هاوتاکردنی دەستبەجێ و پشکنینی بەربەستەکان",
    "warning_empty_fields": "⚠️ تکایە سەرەتا سەرجەم خانە جوگرافی و پێکهاتەیییەکانی ١٣ پڕبکەرەوە؛ بزوێنەری هاوتاکردن ناتوانێت لەسەر خانەی خاڵی کاربکات!",
    "success_msg": "✅ پیرۆزە! نەخشەی سەرەتایی بە تەواوی هاوتایە لەگەڵ سەرجەم بەربەستەکانی بیناسازی و کۆدە پەسەندکراوەکان.",
    "error_msg": "❌ سەرپێچی ئاشکرا لە مەرجەکانی بیناسازی و کۆدە نیشتمانییەکان دۆزرایەوە! مامەڵەکە بەسترا و بڕوانامەی ڕاسپاردە بە شێوەی ئەلیکترۆنی قفڵکرا."
}

# دمج القواميس الثلاثة بشكل نهائي ومستقل تماماً داخل السيرفر
DICTIONARY = {
    "ar": AR_DICTIONARY,
    "en": EN_DICTIONARY,
    "ku": KU_DICTIONARY
}

def get_text(key):
    """دالة قراءة لغة الجلسة وبث الكلمة المطابقة بالملي ثانية وبأمان تام"""
    current_lang = st.session_state.get("language", "ar")
    lang_dict = DICTIONARY.get(current_lang, DICTIONARY["ar"])
    return lang_dict.get(key, key)
