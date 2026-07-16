from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI
import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

tra =  TavilySearch(
        max_results = 4,
        topic = "general"
    )

def web_search(query):
    res = tra.invoke(query)
    # print(res)
    return "\n\n".join(
      i["content"]  for i in res["results"]
    )


llm = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash',
    api_key = os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    template = "You are expert content summary so summary the {research} in 5 line bullet points",
    input_variables = ["research"]
)
user_query = input("Enter your topic ")

chain = prompt | llm | parser

response = chain.invoke({
    "research" : web_search(user_query)
})

print(response)