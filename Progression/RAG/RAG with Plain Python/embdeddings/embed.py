from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client()

prompt = input("Enter the text/word for embeddings ")

response = client.models.embed_content(
    model = 'gemini-embedding-2',
    contents = prompt,
)

print(response.embeddings[0].values,response)
print(len(response.embeddings[0].values))