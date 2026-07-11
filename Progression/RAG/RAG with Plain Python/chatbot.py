import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

raw_data = """

Types of Leaves

- Casual: 8 days/year. Can be used for personal matters. Must be applied at least 1 day

in advance.

- Sick: 10 days/year. Can be availed with a medical certificate if more than 2 days.

- Earned: 15 days/year. Must be pre-approved by your manager.

- Maternity: 26 weeks for female employees, as per government norms.

- Paternity: 7 days for new fathers, to be taken within 2 months of childbirth.

- Bereavement: 3 days, in case of immediate family loss.

"""

chunked_data = raw_data.split('\n')

prompt = input("Enter the prompt ")

## search function
def search(chunked_data,user_query):
    data = user_query.split()
    result = []
    for a in chunked_data:
        temp = ""
        for b in data:
            if(b.strip().lower() in a.strip().lower()):
                temp = a
                result.append(a)
                break
    return result

context = (search(chunked_data,prompt))

prompt1 =f'''
You are an expert assistant. You will answer the User's QUESTION strictly using only the provided CONTEXT.

Context: 
<context>
{context}
</context>

Constraints:
- If the answer cannot be found in the provided CONTEXT, say exactly: "I cannot find the answer to that question in the provided context."
- Do not use your pre-trained knowledge to answer the question. 
- Do not make up or hallucinate information.
- Cite the sources or documents used to formulate your answer if applicable.

User Question:
{prompt}

'''

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model = 'gemini-2.5-flash',
    contents = prompt1
)

print(response.text)





