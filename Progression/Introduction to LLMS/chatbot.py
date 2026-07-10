# from google import genai
# from getpass import getpass

# api_key = getpass("Enter the API key")

# print(api_key)

# client = genai.Client(api_key=api_key)

# # for mod in client.models.list():
# #     print(mod);
# # response = client.models.generate_content(
# #     model = "gemini-1.5-flash",
# #     contents = "What are basic fundamentals of LLM ?",
# # )

# response= client.models.generate_content(
#     model = "gemini-2.5-flash",
#     contents = "What are the basic fundamentals of LLM?"
# )

# print(response.text)





from google import genai
from getpass import getpass

api_key = getpass("Enter the API-KEY ")

client = genai.Client(api_key=api_key)

# for mod in client.models.list():
#     print(mod);

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "What is n8n?",
)
print(response.text)