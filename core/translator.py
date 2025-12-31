from deep_translator import GoogleTranslator

def translate(text: str, target_lang: str):
    if not text:
        return text
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception:
        return text