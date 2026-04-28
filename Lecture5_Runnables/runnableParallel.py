from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

tweetPrompt = PromptTemplate(
    template="Write a Engaging tweet about {topic}",
    input_variables=["topic"]
)

linkedInPrompt = PromptTemplate(
    template="Write a professional LinkedIn post about {topic}",
    input_variables=["topic"]
)

# Chain with the help of RunnableParallel
parallel_chian = RunnableParallel({
    "tweet" : RunnableSequence(tweetPrompt, model, parser),
    "linkedin" : RunnableSequence(linkedInPrompt, model, parser)
})
result = parallel_chian.invoke({"topic": "Narendra Modi is a coward."})

print("*"*50)
print("Tweet: ", result["tweet"])
print("*"*50)
print("LinkedIn Post: ", result["linkedin"])
