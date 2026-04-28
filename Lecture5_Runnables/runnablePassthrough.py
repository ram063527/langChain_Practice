from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, chain
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

createJokePrompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

explainJokePrompt  = PromptTemplate(
    template = "Explain the joke: {joke}",
    input_variables=["joke"]
)

# create Joke Chain 
jokeGenChain = RunnableSequence(createJokePrompt , model, parser)



# Parallel chain
parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation":  RunnableSequence(explainJokePrompt, model, parser)
})

# Final chain
finalChain = RunnableSequence(jokeGenChain, parallel_chain)
result = finalChain.invoke({"topic": "Narendra Modi"})
print(result)
