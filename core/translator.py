<<<<<<< HEAD
from deep_translator import GoogleTranslator

def translate(text: str, target_lang: str):
    if not text:
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception:
=======
from deep_translator import GoogleTranslator

def translate(text: str, target_lang: str):
    if not text:
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception:
>>>>>>> 2474df5d08a01f1f2c138d72edd5319b730733be
        return text