
from google import genai

from config import GEMINI_API_KEY, GEMINI_MODEL, validate_config


def main():
    validate_config()

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents="Reply with exactly: Gemini connection successful."
    )

    print("Gemini response:")
    print(response.text)


if __name__ == "__main__":
    main()
