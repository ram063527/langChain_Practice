from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
                            task="text-generation")

model = ChatHuggingFace(llm=llm)

# 1st prompt -> Write a detailed report 
template1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> Summarize the report in 5 points 
template2 = PromptTemplate(
    template="Summarize the following report in 5 lines: {report}",
    input_variables=["report"]
)

# 
parser = StrOutputParser()

# Form a chain 

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'Black Holes'})
print(result)

