from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
                            task="text-generation")

model = ChatHuggingFace(llm=llm)

# Define Pydantic model for output parsing - Which will act like a scehma for the output we expect from the model

class Person(BaseModel):
    name: str = Field(description="Name of the Person")
    age: int = Field(gt=18, description="Age of the person, must be greater than 18")
    city: str = Field(description="The city where the person lives")

# Create a Pydantic output parser
parser = PydanticOutputParser(pydantic_object=Person)

# Define a prompt template

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person. \n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()} 
)


prompt = template.format(place="British")

# Get the response from the model

# result = model.invoke(prompt)
# # Parse the output using the Pydantic parser
# parsed_result = parser.parse(result.content)
# print(parsed_result)

# # USING CHAINS 
chain = template | model | parser 
result = chain.invoke({"place": "Dutch"})
print(result)