import os 
from google import genai
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
    args = parser.parse_args()

    print("args ", args)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=args.user_prompt
    )

    if not response.usage_metadata:
        raise RuntimeError("API request failed, not sage meta data found")
    
    print("Prompt tokens: ", response.usage_metadata.total_token_count)

    if response.usage_metadata.candidates_token_count:
        print("Response tokens: ", response.usage_metadata.candidates_token_count)
        
        # response.usage_metadata.candidates_token_count
    # print(response)
    print("Response:\n")
    print(response.text)
    
if __name__ == "__main__":
    main()
