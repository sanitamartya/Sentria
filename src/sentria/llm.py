
from google import genai

from sentria.config import settings


def ask_model(prompt: str) -> str:
    if settings.gemini_api_key is None:
        raise RuntimeError("GEMINI_API_KEY is not configured")

    client = genai.Client(
        api_key=settings.gemini_api_key.get_secret_value()
    )

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )

    if response.text is None:
        raise RuntimeError("Gemini returned no text response")

    return response.text
