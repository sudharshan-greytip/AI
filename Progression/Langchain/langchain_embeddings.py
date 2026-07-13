from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAIEmbeddings(
    model='gemini-embedding-2',
    api_key = os.getenv("GEMINI_API_KEY"),
    output_deminsions = 12,
)
emdeddings = llm.embed_query(
    "Hello how are you"
)
# print(emdeddings)
print(len(emdeddings))

emdeddings1 = llm.embed_query(
    ['hi','how are you']
)
print(len(emdeddings1))