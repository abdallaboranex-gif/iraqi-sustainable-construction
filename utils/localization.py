def get_text(text_to_translate):
    """
    [نسخة مصححة ومطابقة] دالة المحرك الذكي التلقائي.
    تطابق كلمات الوجت الحية ("العربية"، "كردي"، "EN") مع الذاكرة السحابية
    لتفعيل التحول الفوري للغات الثلاث دفعة واحدة وبمحو الجمود نهائياً [١.١].
    """
    if not text_to_translate:
        return ""
        
    # 1. قراءة لغة الجلسة الحالية الفعالة والمحدثة مباشرة من أزرار الهيدر
    # نضع القيمة الافتراضية "العربية" لتفتح المنصة بيضاء وموثقة بلغتك الوطنية
    current_lang = st.session_state.get("language_selection_trigger", "العربية")
    
    # 2. إذا كانت اللغة هي العربية، تبث النص كما هو فوراً للحفاظ على السرعة الخارقة
    if current_lang == "العربية":
        return text_to_translate
        
    # تحويل حالة الرمز برمجياً ليتطابق مع مصفوفات التراجم والاصطلاحات الهندسية
    lang_code = "en" if current_lang == "EN" else "ku"
    
    # 3. التحقق من صمام الأمان (قاموس الاستثناءات الهندسية الصارم) لبلديات العراق
    exceptions_dict = TECHNICAL_EXCEPTIONS.get(lang_code, {})
    if text_to_translate in exceptions_dict:
        return exceptions_dict[text_to_translate]
        
    # 4. مصفوفة المحاكاة اللغوية المحدثة والمحاذاة ديناميكياً مع اللغتين الإنكليزية والكردية
    simulated_translations = {
        "en": {
            "منصة البناء المستدام": "Sustainable Construction Platform",
            "الحوكمة الرقمية والامتثال البيئي": "Digital Governance & Environmental Compliance",
            "🎛️ لوحة التحكم السيادية للمنصة": "🎛️ Platform Sovereign Control Panel",
            "الموقع الحالي": "Current Location",
            "اللغة": "Language",
            "حساب غير مسجل": "Unregistered Account",
            "اضغط لتأكيد الهوية": "Click to Verify Identity",
            "📋 الباب الأول: تحليل الموقع ومحددات البلدية": "📋 Portal 1: Site Analysis & Municipal Constraints",
            "يرجى ملء الحقول الـ 13 بدقة لتحديد متطلبات فحص التربة والمدونات الهندسية الإلزامية للمشروع.": "Please fill out the 13 fields accurately to determine soil test and mandatory codes.",
            "1. المحافظة": "1. Governorate",
            "2. القضاء / الناحية": "2. District / Sub-district",
            "4. رقم القطعة والمقاطعة": "4. Plot & Sector Number",
            "5. المساحة الكلية للأرض (متر مربع)": "5. Total Land Area (sqm)",
            "6. مساحة البناء الطابقي (متر مربع)": "6. Built-up Footprint Area (sqm)",
            "7. عدد الطوابق الكلي": "7. Total Number of Floors",
            "8. الارتفاع الكلي للمبنى (متر)": "8. Total Building Height (meters)",
            "9. هل يحتوي المبنى على سرداب (قبو)؟": "9. Does the building contain a basement?",
            "10. الارتداد الأمامي القانوني (متر)": "10. Legal Front Offset (meters)",
            "11. الارتدادات الجانبية والخلفية (متر)": "11. Side and Rear Offsets (meters)",
            "12. طبيعة الملاصقة والأبنية المجاورة": "12. Type of Adjacent Buildings",
            "🚀 تشغيل محرك المطابقة الفوري وفحص القيود": "🚀 Trigger Instant Compliance Engine",
            "⚠️ يرجى ملء كافة البيانات الجغرافية والإنشائية الـ 13 أولاً؛ لا يمكن تشغيل محرك المطابقة على حقول فارغة!": "⚠️ Please fill out all 13 fields first!",
            "🧱 1. العزل الحراري وغلاف المبنى": "🧱 1. Thermal Insulation & Building Envelope",
            "❄️ 2. أحمال التكييف والمنظومات": "❄️ 2. HVAC Cooling Loads & Systems",
            "☀️ 3. تصميم منظومة الألواح الشمسية": "☀️ 3. Solar PV System Design"
        },
        "ku": {
            "منصة البناء المستدام": "سەکۆی بیناسازی بەردەوام",
            "الحوكمة الرقمية والامتثال البيئي": "حوکمڕانی دیجیتاڵی و پابەندبوونی ژینگەیی",
            "🎛️ لوحة التحكم السيادية للمنصة": "🎛️ لۆگۆی کۆنترۆڵی سیادی سەکۆکە",
            "الموقع الحالي": "شوێنی ئێستا",
            "اللغة": "زمان",
            "حساب غير مسجل": "هەژماری تۆمارنەکراو",
            "اضغط لتأكيد الهوية": "کلیک بکە بۆ ناسنامە",
            "📋 الباب الأول: تحليل الموقع ومحددات البلدية": "📋 دەروازەی یەکەم: شیکردنەوەی شوێن",
            "1. المحافظة": "١. پارێزگا",
            "2. القضاء / الناحية": "٢. قەزا / ناحیە",
            "7. عدد الطوابق الكلي": "٧. ژمارەی گشتی نهۆمەکان",
            "8. الارتفاع الكلي للمبنى (متر)": "٨. بەرزی گشتی بیناکە (مەتر)",
            "🚀 تشغيل محرك المطابقة الفوري وفحص القيود": "🚀 دەستپێکردنی بزوێنەری هاوتاکردن",
            "🧱 1. العزل الحراري وغلاف المبنى": "🧱 ١. دابڕانی گەرمی بیناکە",
            "❄️ 2. أحمال التكييف والمنظومات": "❄️ ٢. بارەکانی ساردکردنەوەی HVAC",
            "☀️ 3. تصميم منظومة الألواح الشمسية": "☀️ ٣. دیزاینی سیستەمی سۆلار PV"
        }
    }
    
    # سحب النص المترجم وبثه تلقائياً وبمرونة تامة
    lang_pool = simulated_translations.get(lang_code, {})
    return lang_pool.get(text_to_translate, text_to_translate)
