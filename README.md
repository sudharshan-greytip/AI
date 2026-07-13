# AI Learning Progression 🚀

This repository documents my step-by-step learning journey from **Python
fundamentals** to **Large Language Models (LLMs), LangChain, Embeddings,
and Retrieval-Augmented Generation (RAG)**.

The main purpose of this repository is to learn AI concepts by building
small programs, experimenting with APIs, and understanding how modern
Generative AI applications work internally.

------------------------------------------------------------------------

## 📚 Learning Progress

### 1. Python Core Fundamentals

I started by strengthening the Python fundamentals required for AI and
Generative AI development.

#### Topics Learned

-   Variables and data types
-   User input using `input()`
-   Type conversion using `int()` and `float()`
-   Printing and formatted strings (f-strings)
-   String operations
-   String searching with `find()`
-   String replacement with `replace()`
-   `strip()`, `title()`, `lower()`, and `upper()`
-   Conditional statements
-   Arithmetic operators
-   Comparison operators
-   Logical operators
-   Modulus and floor division
-   Exponentiation
-   Python `math` module

#### Practice Programs

-   User information formatter
-   Product delivery message
-   String manipulation exercises
-   Arithmetic calculator
-   Age classification
-   Discount calculation
-   Leap year checker
-   Temperature classification
-   Loyal customer discount checker

------------------------------------------------------------------------

### 2. Python Lists and Functions

I learned how to organize reusable logic using functions and work with
collections of data.

#### Topics Learned

-   Defining functions using `def`
-   Function parameters
-   Returning values
-   Lists
-   Iterating through lists
-   Adding elements using `append()`
-   List comprehension concepts
-   Conditional expressions / ternary expressions
-   Splitting strings into words

#### Practice Programs

-   Calculator function
-   Odd or even checker
-   Word counter
-   Leap year checker
-   Generate the first 10 cubes
-   Extract odd numbers from a list
-   Convert names to lowercase

------------------------------------------------------------------------

### 3. Loops, Dictionaries, and Tuples

I practiced iteration and problem-solving using loops.

#### Topics Learned

-   `for` loops
-   `while` loops
-   `range()`
-   Nested loops
-   String iteration
-   Modulo-based filtering
-   String case conversion
-   Character filtering

#### Practice Programs

-   Print even numbers from 1 to 50
-   Print odd numbers within a range
-   Multiplication table using nested loops
-   Count characters in a string
-   Swap uppercase and lowercase characters
-   Remove vowels from a string

I am also progressing through Python collection concepts such as
**dictionaries and tuples**.

------------------------------------------------------------------------

### 4. Lambda Functions and Python Modules

I started learning concise functions and built-in Python modules.

#### Topics Learned

-   Lambda expressions
-   Importing modules
-   Python `math` module
-   `math.pi`
-   Exponentiation
-   Mathematical formulas in Python

#### Practice Programs

-   Calculate the area of a circle using lambda
-   Compound interest calculation using lambda

------------------------------------------------------------------------

## 🤖 Introduction to Large Language Models

After learning Python fundamentals, I started exploring **Large Language
Models (LLMs)** and Generative AI.

### Concepts Learned

-   What is Artificial Intelligence?
-   Machine Learning
-   Deep Learning
-   Natural Language Processing
-   Large Language Models
-   Tokens and text processing
-   Prompt-based interaction
-   Model input and output
-   AI hallucination
-   Importance of context
-   API-based LLM integration

------------------------------------------------------------------------

## ✨ Google Gemini API

I learned how to interact with Gemini models using Python.

### Topics Learned

-   Installing the Google Gen AI SDK
-   Creating a Gemini client
-   API key management
-   Using `.env` files
-   Loading environment variables with `python-dotenv`
-   Reading secrets using `os.getenv()`
-   Calling `generate_content()`
-   Accessing model responses
-   Building command-line chatbots

### Basic Gemini Example

``` python
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What are the basic fundamentals of LLM?"
)

print(response.text)
```

------------------------------------------------------------------------

## 💬 Building Chatbots with Gemini

I built multiple chatbot experiments to understand how LLM conversations
work.

### Simple CLI Chatbot

The chatbot:

1.  Accepts a user prompt.
2.  Sends the prompt to Gemini.
3.  Receives the model response.
4.  Prints the response.

### Dynamic Prompt Chatbot

I created a continuous chatbot using a `while` loop.

``` text
User Prompt
    ↓
Gemini Model
    ↓
AI Response
    ↓
Wait for Next Prompt
```

The chatbot exits when the user enters `exit`.

### Chatbot with Memory

I experimented with storing previous messages in a `chat_history` list.

``` text
User Message
      ↓
Chat History
      ↓
Gemini Model
      ↓
AI Response
      ↓
Updated Chat History
```

This helped me understand an important LLM concept:

> LLMs do not automatically remember previous application messages.
> Conversation history or state must be managed and supplied by the
> application when required.

------------------------------------------------------------------------

## 🌐 Streamlit Chatbot

I built a simple chatbot user interface using Streamlit.

### Topics Learned

-   Importing Streamlit
-   Creating a page title
-   Text input
-   Buttons
-   Displaying AI responses
-   Connecting a frontend-like Python UI with Gemini

### Application Flow

``` text
Streamlit UI
     ↓
User enters a prompt
     ↓
Gemini API
     ↓
Generated response
     ↓
Display response in UI
```

------------------------------------------------------------------------

## 🔗 LangChain

I started learning LangChain to understand how LLM applications can be
structured using reusable abstractions.

### Topics Learned

-   What is LangChain?
-   LLM and chat model integration
-   `ChatGoogleGenerativeAI`
-   Model configuration
-   Calling models using `invoke()`
-   Accessing `response.content`
-   Prompt-based summarization
-   Gemini integration with LangChain

### Example

``` python
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

response = llm.invoke(
    "What is the difference between AI Agents and Agentic AI?"
)

print(response.content)
```

------------------------------------------------------------------------

## 🧠 Embeddings

I started learning one of the most important concepts behind semantic
search and RAG: **embeddings**.

### What I Learned

An embedding converts text into a numerical vector.

``` text
Text
 ↓
Embedding Model
 ↓
Numerical Vector
```

Conceptually:

``` text
"Python programming"
        ↓
[0.12, -0.45, 0.87, ...]
```

The vector represents semantic information about the input.

### Important Concepts

-   Text embeddings
-   Numerical vectors
-   Vector dimensions
-   Semantic meaning
-   Similar text can have similar vector representations
-   Query embeddings
-   Gemini embedding models
-   LangChain embedding integration

### Gemini Embedding Experiment

I used `embed_content()` to convert user input into an embedding vector
and inspected the vector values and dimensions.

### LangChain Embedding Experiment

I also experimented with `GoogleGenerativeAIEmbeddings` and
`embed_query()`.

------------------------------------------------------------------------

## 📦 Chunking

While learning embeddings and RAG, I studied **chunking**.

### What is Chunking?

Chunking means splitting large data into smaller pieces.

``` text
Large Document
      ↓
Chunk 1
Chunk 2
Chunk 3
Chunk 4
```

### Why Chunk Data?

-   Models have context limitations.
-   Smaller text units are easier to retrieve.
-   Embeddings can represent focused information.
-   Retrieval becomes more relevant.
-   It reduces unnecessary context sent to an LLM.

I also learned that **chunking is generally handled by the
application/developer or a text-splitting pipeline before embedding**.
The embedding model converts the provided input into vectors; it does
not automatically design the application's chunking strategy.

------------------------------------------------------------------------

## 🔍 Retrieval-Augmented Generation (RAG)

I started implementing RAG using plain Python before relying on
frameworks.

### What is RAG?

RAG combines:

``` text
Retrieval + Generative AI
```

Instead of asking an LLM to answer only from its learned knowledge, the
application retrieves relevant information and provides it as context.

### RAG Flow

``` text
User Question
      ↓
Search / Retrieval
      ↓
Relevant Context
      ↓
Prompt + Context
      ↓
LLM
      ↓
Context-Based Answer
```

### Plain Python RAG Experiment

I created sample employee leave-policy data containing:

-   Casual leave
-   Sick leave
-   Earned leave
-   Maternity leave
-   Paternity leave
-   Bereavement leave

The application:

1.  Stores raw text data.
2.  Splits the text into chunks.
3.  Accepts a user question.
4.  Searches chunks using keyword matching.
5.  Collects matching context.
6.  Builds a controlled prompt.
7.  Sends the context and question to Gemini.
8.  Generates an answer using the retrieved context.

### Prompt Constraints

The RAG prompt instructs the model to:

-   Answer only using the provided context.
-   Avoid using unrelated pretrained knowledge.
-   Avoid making up information.
-   Return a fallback response when the answer is unavailable.

This experiment helped me understand the basic RAG architecture before
moving to vector search.

------------------------------------------------------------------------

## 🔎 Keyword Search vs Semantic Search

### Current Plain Python RAG

My current RAG experiment uses keyword matching.

``` text
Question
   ↓
Split words
   ↓
Search chunks for matching words
   ↓
Return matching chunks
```

### Limitation

Keyword search depends heavily on exact or similar words.

For example:

``` text
Document: "Casual leave can be used for personal matters."

Question: "Can I take time off for private work?"
```

The meaning is related, but exact keywords may not match.

### Next Step: Semantic Search

Embeddings can help search based on meaning.

``` text
Documents
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Storage

User Question
    ↓
Query Embedding
    ↓
Similarity Search
    ↓
Relevant Chunks
    ↓
LLM
```

This is the next stage of my RAG learning journey.

------------------------------------------------------------------------

## 🧩 AI Agents and Agentic AI

I started exploring AI agents and agentic systems.

### AI Agent

An AI agent can:

-   Observe information
-   Reason about a task
-   Use tools
-   Perform an action
-   Analyze results

Example:

``` text
User Goal
   ↓
Agent
   ↓
Select Tool
   ↓
Execute Action
   ↓
Observe Result
   ↓
Generate Response
```

### Agentic AI

Agentic AI focuses on systems capable of working toward a goal through
multiple steps and decisions.

I am learning the differences between:

-   LLM applications
-   AI agents
-   Agentic AI
-   Single-agent systems
-   Multi-agent systems

------------------------------------------------------------------------

## 👥 Multi-Agent Pattern

I recently started learning the **multi-agent pattern**.

A multi-agent system uses multiple specialized agents instead of asking
one agent to perform every responsibility.

Example:

``` text
User Task
    ↓
Coordinator Agent
    ↓
┌──────────────┬──────────────┬──────────────┐
│ Research     │ Analysis     │ Review       │
│ Agent        │ Agent        │ Agent        │
└──────────────┴──────────────┴──────────────┘
    ↓
Combined Final Result
```

### Why Multi-Agent Systems?

-   Separation of responsibilities
-   Specialized prompts and tools
-   Easier decomposition of complex tasks
-   Independent review and validation
-   Better workflow organization for suitable problems

I am currently learning **when multi-agent architecture is useful and
when a single agent is enough**.

------------------------------------------------------------------------

## 📁 Repository Structure

``` text
AI/
│
├── Progression/
│   │
│   ├── Python Fundamentals/
│   │   ├── Python_Core_Fundamentals/
│   │   ├── Operators_ConditionalStatements_Lists/
│   │   ├── Dictionaries_Tuples_Loops/
│   │   ├── List_Functions/
│   │   └── lamda_modules/
│   │
│   ├── Introduction to LLMS/
│   │   ├── chatbot.py
│   │   ├── streamlit/
│   │   └── chatbot_with_dynamic_prompt/
│   │
│   ├── Langchain/
│   │   ├── langchain.py
│   │   ├── langchain_learn.py
│   │   └── langchain_embeddings.py
│   │
│   └── RAG/
│       └── RAG with Plain Python/
│           ├── chatbot.py
│           └── embdeddings/
│               └── embed.py
│
└── README.md
```

------------------------------------------------------------------------

## 🛠️ Technologies and Libraries Used

-   Python
-   Google Gemini
-   Google Gen AI SDK
-   LangChain
-   LangChain Google GenAI integration
-   Streamlit
-   python-dotenv

------------------------------------------------------------------------

## 🔐 Environment Variables

API keys should not be hardcoded in Python files.

Create a `.env` file:

``` text
GEMINI_API_KEY=your_api_key_here
```

Load the environment variable:

``` python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
```

> **Security Note:** Never commit `.env` files or API keys to GitHub. If
> a key is accidentally committed, revoke or rotate it and remove the
> secret from Git history.

------------------------------------------------------------------------

## ⚙️ Setup

### 1. Clone the Repository

``` bash
git clone <your-repository-url>
cd AI
```

### 2. Create a Virtual Environment

``` bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment

#### macOS / Linux

``` bash
source .venv/bin/activate
```

#### Windows

``` bash
.venv\Scripts\activate
```

### 4. Install the Required Libraries

``` bash
pip install google-genai python-dotenv streamlit langchain langchain-google-genai
```

### 5. Configure the Gemini API Key

Create a `.env` file and add:

``` text
GEMINI_API_KEY=your_api_key_here
```

### 6. Run a Python Experiment

``` bash
python chatbot.py
```

### 7. Run the Streamlit Chatbot

``` bash
streamlit run chatbot.py
```

------------------------------------------------------------------------

## 🗺️ My AI Learning Roadmap

### Completed / Practiced

-   [x] Python core fundamentals
-   [x] Operators and conditional statements
-   [x] Loops
-   [x] Lists
-   [x] Functions
-   [x] String manipulation
-   [x] Lambda basics
-   [x] Python modules
-   [x] LLM fundamentals
-   [x] Gemini API integration
-   [x] Basic CLI chatbot
-   [x] Dynamic chatbot loop
-   [x] Basic conversation-history experiment
-   [x] Streamlit chatbot
-   [x] LangChain model integration
-   [x] Embedding fundamentals
-   [x] Gemini embedding experiment
-   [x] LangChain embedding experiment
-   [x] Chunking fundamentals
-   [x] Plain Python RAG using keyword retrieval
-   [x] AI agent fundamentals
-   [x] Introduction to multi-agent patterns

### Currently Learning

-   [ ] Semantic similarity
-   [ ] Vector search
-   [ ] Complete embedding-based RAG
-   [ ] LangChain text splitters
-   [ ] LangChain RAG pipelines
-   [ ] Vector databases
-   [ ] AI agents
-   [ ] Agentic AI workflows
-   [ ] Multi-agent architecture

### Planned Next Steps

-   [ ] Cosine similarity
-   [ ] Build semantic search using plain Python
-   [ ] Build RAG using embeddings
-   [ ] Learn FAISS or another vector store
-   [ ] Build RAG using LangChain
-   [ ] Learn tool calling
-   [ ] Build a single AI agent
-   [ ] Learn agent memory and state
-   [ ] Build a multi-agent workflow
-   [ ] Build an end-to-end Agentic AI project

------------------------------------------------------------------------

## 🎯 Learning Approach

My learning approach is:

``` text
Learn the Concept
      ↓
Understand Why It Is Needed
      ↓
Implement with Plain Python
      ↓
Identify the Limitations
      ↓
Learn the Framework
      ↓
Build a Real Project
```

I prefer understanding **what happens internally** before using
high-level AI frameworks.

For example:

``` text
Plain Python RAG
        ↓
Understand Retrieval
        ↓
Understand Chunking
        ↓
Understand Embeddings
        ↓
Understand Vector Search
        ↓
LangChain RAG
        ↓
Agentic AI
```

------------------------------------------------------------------------

## 🚀 Goal

My goal is to become an **AI / Agentic AI Developer** who can design and
build:

-   LLM-powered applications
-   Intelligent chatbots
-   RAG systems
-   Semantic search systems
-   AI agents
-   Tool-using agents
-   Agentic workflows
-   Multi-agent systems

This repository will continue to evolve as I progress through my AI
learning journey.

------------------------------------------------------------------------

## 📌 Note

This is a **learning and progression repository**. Some files contain
small experiments or in-progress exercises created to understand
individual concepts. The implementations will be improved as I learn
more advanced AI engineering patterns.

------------------------------------------------------------------------

⭐ **Learning AI step by step --- from Python fundamentals to Agentic
AI.**
