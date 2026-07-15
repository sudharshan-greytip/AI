from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

user_query = input("Enter the topic ")

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)
prompt = PromptTemplate(
    template = '''Give me the detail report on the given {topic}''',
    input_variables = ["topic"]
)

chain = prompt | llm 

response = chain.invoke({
    "topic" : user_query
})

print(response.content)
