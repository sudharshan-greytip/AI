from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY"),
)
destination = "Bangalore"
templete = PromptTemplate.from_template("List some of the temples in {destination}")
prompt = templete.format(destination = destination)
response = llm.invoke(prompt)
print(response.content)