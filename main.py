import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model_name = "gemini-2.0-flash-001"

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    app_name = sys.argv[0]

    if not args:
        print(f"Usage: python {app_name} <input prompt> [--verbose]")
        sys.exit(1)

    user_prompt = " ".join(args)
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )

    if verbose:
        print(f"User prompt: {user_prompt}\n")
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
