import requests
import unicodedata

# More stable public instance
LIBRE_TRANSLATE_URL = "https://libretranslate.de/translate"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def translate_en_to_hi(text: str) -> str:
    """
    Translates English → Hindi.
    NEVER crashes PDF generation.
    """

    if not text or not text.strip():
        return text

    payload = {
        "q": text,
        "source": "en",
        "target": "hi",
        "format": "text"
    }

    try:
        response = requests.post(
            LIBRE_TRANSLATE_URL,
            json=payload,          # IMPORTANT: json= not data=
            headers=HEADERS,
            timeout=8
        )

        response.raise_for_status()

        result = response.json()
        hindi = result.get("translatedText", text)

        # Normalize Unicode for proper Hindi rendering
        return unicodedata.normalize("NFC", hindi)

    except Exception:
        # HARD FAIL-SAFE
        # If translation fails, return original text
        # so PDF generation NEVER breaks
        return text
