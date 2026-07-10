from google import genai
from getpass import getpass
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

while True :
    prompt = input("Enter the Prompt ")
    if(prompt.strip().lower()=='exit'):
        print("Bye....")
        break

    response = client.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt,
    )

    print(response.text)