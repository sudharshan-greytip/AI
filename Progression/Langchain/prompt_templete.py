from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

name = input("Enter your name ")
height = int(input("Enter your height "))
weight = int(input("Enter your weight "))
llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key= os.getenv("GEMINI_API_KEY"),
)

templete = PromptTemplate(
    template = '''
    Calculate the BMI for the provided inputs {name},{height},{weight} and explain what is BMI number means
    ''',
    input_variables = [
        "name","height","weight"
    ],
)

prompt = templete.format(name=name,height=height, weight=weight)
response = llm.invoke(prompt)
print(response.content)


# llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash",
#     api_key = os.getenv("GEMINI_API_KEY"),
# )
# destination = "Bangalore"
# templete = PromptTemplate.from_template("List some of the temples in {destination}")
# prompt = templete.format(destination = destination)
# response = llm.invoke(prompt)
# print(response.content)

