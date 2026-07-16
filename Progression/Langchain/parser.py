from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import json

load_dotenv()
parser = StrOutputParser()
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY")
)

user_query = input("Enter the topic ")

report = PromptTemplate(
    template = '''Generate the detailed report on a given {topic}''',
    input_variables = ["topic"]
)

points = PromptTemplate(
    template = '''Convert the {report} into 5-point summary ''',
    input_variables = ["report"],
)

quote = PromptTemplate(
    template = '''Use the {summary} to generate a motivational quote''',
    input_variables = ["summary"],
)

chain = report | llm | parser | points | llm | parser | quote | llm | parser

result = chain.invoke({
    "topic" :user_query
    })

print(json.dumps(result))

