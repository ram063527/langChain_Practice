from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence


load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")

jokePrompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

parser = StrOutputParser()

explainPrompt  = PromptTemplate(
    template = "Explain the joke: {joke}",
    input_variables=["joke"]
)

# Chain with the help of RunnableSequence

chain = RunnableSequence(jokePrompt , model, parser, explainPrompt, model, parser)
result = chain.invoke({"topic": "Narendra Modi"})
print(result)
