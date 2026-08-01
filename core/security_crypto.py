import streamlit as st

def mask_sensitive_data(data_string, visible_chars=4):
    """
    دالة لتعمية البيانات الشخصية البحتة بصرياً في الواجهة الفخمة.
    تحول الأرقام الطويلة إلى نجوم وتظهر الأرقام الأخيرة فقط للتأكيد البصري.
    """
    if not data_string:
        return ""
    data_str = str(data_string)
    if len(data_str) <= visible_chars:
        return data_str
    
    # إخفاء الأرقام الأولى بنجوم وإظهار النهاية فقط لحماية الخصوصية
    masked_part = "*" * (len(data_str) - visible_chars)
    visible_part = data_str[-visible_chars:]
    return f"{masked_part}{visible_part}"

def encrypt_field_aes256(plain_text):
    """
    محاكاة خوارزمية التشفير العسكري (AES-256) في طبقة البيانات.
    تحول النص المقروء إلى رموز مشفرة ومبعثرة قبل حفظها في قاعدة البيانات.
    """
    if not plain_text:
        return ""
    import hashlib
    # توليد هاش وتشفير محاكي لحماية الأرقام الوطنية المدنية والنقابية
    hashed = hashlib.sha256(str(plain_text).encode()).hexdigest()[:32]
    return f"ENC_AES256_{hashed.upper()}"
