import requests
import unicodedata

LIBRE_TRANSLATE_URL = "https://libretranslate.de/translate"

def translate_en_to_hi(text: str) -> str:
    if not text or not text.strip():
        return text

    payload = {
        "q": text,
        "source": "en",
        "target": "hi",
        "format": "text"
    }

    response = requests.post(
        LIBRE_TRANSLATE_URL,
        json=payload,
        timeout=8
    )

    print("STATUS:", response.status_code)
    print("RAW RESPONSE:", response.text)

    response.raise_for_status()

    data = response.json()
    translated = data.get("translatedText", "")

    if not translated or translated.strip().lower() == text.strip().lower():
        raise ValueError("Translation not applied")

    return unicodedata.normalize("NFC", translated)