from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

prompt = '''
summarize the below following paragraph into 5 lines bullet points
Artificial Intelligence, commonly known as AI, is one of the most important technologies in the modern world.
AI refers to the ability of machines to perform tasks that normally require human intelligence.
It allows computers to learn, reason, understand information, and make decisions.
The main goal of AI is to create intelligent systems that can solve complex problems.
AI has become an important part of our daily lives.
Smartphones use AI to provide better user experiences.
Voice assistants can understand human speech using AI.
Search engines use AI to provide relevant search results.
Social media platforms use AI to recommend content to users.
Online shopping websites use AI to suggest products.
Artificial Intelligence is a broad field of computer science.
Machine Learning is an important subset of AI.
Machine Learning allows computers to learn from data.
Instead of writing every rule manually, developers train models using data.
The model identifies patterns in the provided data.
It then uses those patterns to make predictions.
Deep Learning is a subset of Machine Learning.
Deep Learning uses artificial neural networks.
Neural networks are inspired by the human brain.
They contain interconnected layers of artificial neurons.
These networks can learn complex patterns from large datasets.
Deep Learning is widely used in image recognition.
It is also used in speech recognition.
Natural Language Processing is another important area of AI.
Natural Language Processing is commonly called NLP.
NLP helps computers understand human language.
Chatbots use NLP to communicate with users.
Translation systems use NLP to translate languages.
AI assistants can answer questions using language models.
Large Language Models are advanced AI models.
They are commonly called LLMs.
LLMs are trained using large amounts of text data.
They learn patterns and relationships between words.
LLMs can generate human-like text.
They can answer questions and explain complex concepts.
They can also generate computer programs.
Developers use AI to improve software development.
AI coding assistants can suggest code.
They can help developers identify bugs.
They can explain unfamiliar code.
AI can also generate test cases.
However, developers must verify AI-generated code.
AI systems can sometimes produce incorrect information.
This problem is sometimes called AI hallucination.
AI models do not think exactly like humans.
They process patterns learned from training data.
Data plays an important role in Artificial Intelligence.
The quality of data affects the quality of an AI model.
Incorrect data can produce incorrect predictions.
Biased data can create biased AI systems.
Therefore, data preparation is an important step in AI development.
Data cleaning removes unwanted or incorrect information.
Data preprocessing transforms data into a suitable format.
Large datasets are often divided into smaller chunks.
Chunking is especially useful in AI applications.
Embeddings convert information into numerical vectors.
These vectors represent the meaning of the information.
Similar information usually has similar vector representations.
Vector databases store and search embeddings.
They are widely used in modern AI applications.
Retrieval-Augmented Generation is commonly called RAG.
RAG combines information retrieval with generative AI.
A RAG system searches for relevant information.
The retrieved information is given to a language model.
The model uses the context to generate an answer.
RAG can reduce incorrect AI responses.
It is commonly used in document-based chatbots.
Companies use RAG to build internal AI assistants.
AI agents are another important concept.
An AI agent can observe information and perform actions.
Agents can use tools to complete tasks.
For example, an agent can search a database.
It can call an API.
It can execute a workflow.
It can analyze the result and decide the next action.
Agentic AI focuses on AI systems that can work toward goals.
These systems can perform multiple steps automatically.
A single-agent system uses one agent to complete tasks.
A multi-agent system uses multiple specialized agents.
Each agent can have a specific responsibility.
One agent may perform research.
Another agent may analyze information.
Another agent may review the final result.
The agents can collaborate to solve complex problems.
AI is also transforming the healthcare industry.
It can help analyze medical images.
AI is used in finance to detect suspicious transactions.
Manufacturing companies use AI for automation.
Transportation systems use AI for route optimization.
Education platforms use AI for personalized learning.
Businesses use AI to analyze customer behavior.
AI can improve productivity and reduce repetitive work.
However, AI also creates ethical challenges.
Privacy is an important concern in AI systems.
Security is another major consideration.
AI systems must be designed responsibly.
Human supervision is important for critical decisions.
Developers should understand the limitations of AI.
AI should be used as a tool to support humans.
It should not be blindly trusted for every decision.
The future of Artificial Intelligence is rapidly evolving.
New AI models and technologies are continuously being developed.
Learning AI can create many career opportunities.
Developers who understand AI can build intelligent applications.
Understanding Python, Machine Learning, LLMs, RAG, and AI agents is valuable.
Artificial Intelligence is changing how people interact with technology.
AI will continue to influence industries around the world.
Therefore, learning Artificial Intelligence is an important step toward understanding the future of technology.
'''

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    api_key= os.getenv("GEMINI_API_KEY"),
)

response = llm.invoke(prompt)
print(response.content)