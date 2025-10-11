import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
prompt = "".join(sys.argv[1:])
if len(prompt) < 1:
    print("error")
    sys.exit(1)
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)
if sys.argv[-1] == "--verbose":
    print(f"User prompt: {response.text}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")