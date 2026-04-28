from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

def word_counter(text: str) -> int:
    return len(text.split())

runnableWordCounter = RunnableLambda(word_counter)


model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

# 1. Create a joke prompt

jokePrompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# chain for joke generation
jokeGenChain = RunnableSequence(jokePrompt , model, parser)

# Parallel chain
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": runnableWordCounter
})

# Final chain
finalChain = RunnableSequence(jokeGenChain, parallel_chain)
result = finalChain.invoke({"topic": "Narendra Modi"})
print(result)




