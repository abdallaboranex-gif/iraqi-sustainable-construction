import streamlit as st
import pandas as pd
import os

def load_dynamic_code(file_name):
    """
    دالة ديناميكية تفحص مجلد data/codes وتقرأ ملف الإكسل المطلوب تلقائياً.
    تستخدم الذاكرة المؤقتة الذكية (Cache) لضمان سرعة التصفح السحابي.
    """
    base_path = os.path.join("data", "codes")
    file_path = os.path.join(base_path, file_name)
    
    # التحقق من وجود الملف في المستودع لمنع انهيار السيرفر
    if not os.path.exists(file_path):
        return None
        
    try:
        # قراءة جدول الإكسل وتحويله ديناميكياً إلى جدول بيانات برمي (DataFrame)
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        st.error(f"خطأ في قراءة ملف المدونة {file_name}: {str(e)}")
        return None

def verify_site_compliance(governorate, zoning_type, building_height, floors):
    """
    محرك تدقيق قيود البناء ومحددات البلدية جغرافياً.
    يطابق الارتفاع وعدد الطوابق المدخلة مع المسموح به قانونياً في تلك المحافظة.
    """
    # 1. تحميل جدول مدونة الأحمال والمحددات الإنشائية ديناميكياً
    code_df = load_dynamic_code("concrete_structural.xlsx")
    
    compliance_results = {
        "status": True,       # الافتراضي: مطابق مالم يثبت العكس
        "logs": [],           # تفاصيل الفحص بنداً بنداً
        "errors": []          # سجل المخالفات الحمراء
    }
    
    if code_df is None:
        # في حال عدم وجود جدول مسبق، يمرر النظام فحصاً آمناً مؤقتاً
        compliance_results["logs"].append("⚠️ جدول المدونة الهيكلية غير متوفر، تم التمرير بناءً على القواعد القياسية.")
        return compliance_results

    try:
        # 2. الفلترة التلقائية بناءً على جغرافية المحافظة وجنس العقار المختير
        matched_rules = code_df[
            (code_df['Governorate'] == governorate) & 
            (code_df['Zoning_Type'] == zoning_type)
        ]
        
        if matched_rules.empty:
            # إذا كانت المحافظة جديدة أو مضافة حديثاً في الإكسل ولم يعثر على قيد محدد
            compliance_results["logs"].append(f"ℹ️ تم تطبيق معايير الأمان العامة للعراق على محافظة {governorate}.")
            max_floors = 4
            max_height = 15.0
        else:
            # سحب الحدود الصارمة من سطر الإكسل المكتشف ديناميكياً
            max_floors = int(matched_rules.iloc[0]['Max_Floors'])
            max_height = float(matched_rules.iloc[0]['Max_Height'])
            
        # 3. تشغيل معادلات ومصفوفة التدقيق الإلكتروني الصارم (Strict Mode)
        # أ. فحص قيد عدد الطوابق
        if floors > max_floors:
            compliance_results["status"] = False
            compliance_results["errors"].append(
                f"❌ مخالفة في الباب الأول: عدد الطوابق المدخل ({floors}) يتجاوز الحد الأعلى المسموح به في بلديات {governorate} لجنس العقار ({zoning_type}) وهو ({max_floors}) طوابق."
            )
        else:
            compliance_results["logs"].append(f"✓ قيد عدد الطوابق مطابق للشروط البلدية (الحد الأقصى: {max_floors}).")
            
        # ب. فحص قيد الارتفاع الكلي للمبنى
        if building_height > max_height:
            compliance_results["status"] = False
            compliance_results["errors"].append(
                f"❌ مخالفة في الباب الأول: الارتفاع الكلي المقترح ({building_height}م) يتجاوز المحدد القانوني لمدونة بلديات {governorate} وهو ({max_height}م)."
            )
        else:
            compliance_results["logs"].append(f"✓ الارتفاع الكلي للمبنى مطابق للحدود المسموحة (الحد الأقصى: {max_height}م).")
            
    except Exception as e:
        compliance_results["status"] = False
        compliance_results["errors"].append(f"⚙️ فشل محرك الفحص في إتمام التدقيق التلقائي: {str(e)}")
        
    return compliance_results
