from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import  RunnableSequence, RunnableBranch, RunnablePassthrough
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")
parser = StrOutputParser()

# Prompt1 - Given a Topic, Generate a detailed report on it.
reportPrompt = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# Chain1 - For report generation
reportChain = RunnableSequence(reportPrompt, model, parser)


# Prompt 2 - Given a detailed report, Generate a summary of it.
summaryPrompt = PromptTemplate(
    template="Summarize the following report: {report}",
    input_variables=["report"]
)

# Chain 2 - For summary generation
summaryChain = RunnableSequence(summaryPrompt, model, parser)

# Branching chain - If the report is more than 500 words, then generate a summary, otherwise skip it.

branchChain = RunnableBranch(
    (lambda x: len(x.split()) > 300, summaryChain),
    RunnablePassthrough()
)

finalChain = RunnableSequence(reportChain, branchChain)
result = finalChain.invoke({"topic": "Iran vs USA war"})
print(result)