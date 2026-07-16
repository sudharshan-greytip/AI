from langchain_core.runnables import RunnableLambda , RunnableParallel

str = "Gen AI impact in india"

def get_str_len(str):
    return len(str.strip().split())

def get_word_len(word):
    return len(word)

words = RunnableLambda(get_str_len)
char = RunnableLambda(get_word_len)

res = RunnableParallel({
    "words" : words,
    "char" : char
    }
)

print(res.invoke(str))