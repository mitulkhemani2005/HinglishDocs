import requests
import unicodedata

LIBRE_TRANSLATE_URL = "https://translate.argosopentech.com/translate"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0"  # important for some instances
}

def translate_en_to_hi(text: str) -> str:
    """
    Cloud-safe English → Hindi translation.
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
            json=payload,
            headers=HEADERS,
            timeout=10
        )

        # If server responds but with no body
        if not response.text or not response.text.strip():
            return text

        # Try JSON safely
        try:
            data = response.json()
        except Exception:
            return text

        hindi = data.get("translatedText")

        # Validate translation
        if not hindi or hindi.strip().lower() == text.strip().lower():
            return text

        return unicodedata.normalize("NFC", hindi)

    except Exception:
        # ABSOLUTE FAIL-SAFE
        return text
