from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
import os
from dotenv import load_dotenv

load_dotenv()



chat_history = [SystemMessage("You are a expert AI Assisant .Answer the question cleverly with precise.")]

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    api_key = os.getenv("GEMINI_API_KEY"),
)

while True:
    prompt = input("Enter your query ")
    if(prompt.strip().lower()=='exit'):
        print("Thank You see you soon")
        break
    
    chat_history.append(HumanMessage(prompt))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(response.content))
    print(response.content)

print(chat_history)
