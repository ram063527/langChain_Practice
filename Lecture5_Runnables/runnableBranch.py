from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-3.1-flash-lite-preview")

strParser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback which is either positive or negative.")

pydanticParser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Given a user feedback : {feedback} \n\n Classify the sentiment of the feedback as either positive or negative. \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": pydanticParser.get_format_instructions()}
)

positiveResponsePrompt = PromptTemplate(
    template="Write a appropriate response to this positive feedback: {feedback}",
    input_variables=["feedback"]
)

negativeResponsePrompt = PromptTemplate(
    template="Write a appropriate response to this negative feedback: {feedback}",  
    input_variables=["feedback"]
)

classifierChain = RunnableSequence(prompt1, model, pydanticParser)

branchChain = RunnableBranch(
    (lambda x: x.sentiment == "positive", RunnableSequence(positiveResponsePrompt, model, strParser)),
    (lambda x: x.sentiment == "negative", RunnableSequence(negativeResponsePrompt, model, strParser)),
    RunnableLambda(lambda x: "Could not classify the sentiment of the feedback.")
)

finalChain = RunnableSequence(classifierChain, branchChain)
result = finalChain.invoke({"feedback": "Excellent product! Really loved it. Will keep coming back for more. Highly recommended! Best purchase I've made in a while."})
print(result)