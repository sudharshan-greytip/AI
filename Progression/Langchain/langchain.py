from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

response = llm.invoke("What is the difference between AI Agents and Agentic AI")
print(response.content)