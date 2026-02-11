import os 
from google import genai
from dotenv import load_dotenv

def main():
    print("Hello from gemini-agent!")

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if (not api_key):
        raise RuntimeError("API_KEY not for gemini")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print("Response:\n")
    print(response.text)
    
if __name__ == "__main__":
    main()
