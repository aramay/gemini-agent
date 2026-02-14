import os 
from google import genai
from google.genai import types
from dotenv import load_dotenv
import argparse

def main():
    print("Hello from gemini-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if (not api_key):
        raise RuntimeError("API_KEY not for gemini")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # print ("message ", messages)
    # print("args ", args)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )

    if not response.usage_metadata:
        raise RuntimeError("API request failed, not sage meta data found")
    # If the --verbose flag is included, the console output should include:
    if (args.verbose):

        print("User prompt: ", args.user_prompt)

        print("Prompt tokens: ", response.usage_metadata.total_token_count)

        if response.usage_metadata.candidates_token_count:
            print("Response tokens: ", response.usage_metadata.candidates_token_count)
        
        # response.usage_metadata.candidates_token_count
    # print(response)
    print("Response:\n")
    print(response.text)
    
if __name__ == "__main__":
    main()
