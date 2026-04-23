from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

# Get the report
prompt1 = template1.invoke({'topic': 'Black Holes'})

result = model.invoke(prompt1)

# Get the summary
prompt2 = template2.invoke({'report': result.content})

finalResult = model.invoke(prompt2)

print(finalResult.content)