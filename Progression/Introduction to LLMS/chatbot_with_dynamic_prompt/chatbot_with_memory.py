from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat_history = []

while True:
    prompt = input("Enter the prompt ")
    if(prompt.strip().lower()=='exit'):
        print("Bye..")
        break

    chat_history.append(f"you: {prompt}")

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = chat_history,
    )

    chat_history.append(response.text)
    print(chat_history)