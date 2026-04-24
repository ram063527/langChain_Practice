# [feedback] -> Analyze [positive / negative ] -> if [positive] -> [give positive feedback] -> else [give constructive feedback]
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
from typing import Literal


load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template= "Classify the sentiment of the following feedback as positive or negative: {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template="Write a appropriate response to this positive feedback: {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="Write a appropriate response to this negative feedback: {feedback}",
    input_variables=["feedback"]
)



classifier_chain = prompt1 | model | parser2

branch_chain = RunnableBranch(

    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment of the feedback")
)


chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "The Product is terrible!"})
print(result)
chain.get_graph().print_ascii()


