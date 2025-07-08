import os
import sys

from dotenv import load_dotenv
from google import genai


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv
    if len(args) < 2:
        print(f"Usage: python {sys.argv[0]} <input prompt>")
        sys.exit(1)

    prompt = sys.argv[1]
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)

    print(response.text)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))


if __name__ == "__main__":
    main()
