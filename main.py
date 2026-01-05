import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import available_functions
from functions.get_files_info import call_function


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
model_name = "gemini-2.5-flash"
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Hello"
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)])
]
verbose = "--verbose" in sys.argv
count = 0
while count < 20:
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt) 
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if response.function_calls:
        function_call = response.function_calls[0]
        function_call_result = call_function(function_call, verbose=verbose)
        function_responses = types.Content(role="user", parts=function_call_result.parts)
        
        messages.append(function_responses)
        if not function_call_result.parts or not hasattr(function_call_result.parts[0], "function_response"):
            raise Exception("FATAL")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
    if response.text:
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        if verbose:
            print(f"User prompt: {response.text}")
        sys.exit()
    count += 1