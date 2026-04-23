from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")

# Schema 
# SImple dict
class Review(TypedDict):
    key_themes: Annotated[list[str],"A list of the main themes or topics discussed in the review, such as performance, camera quality, battery life, design, etc."]
    summary: Annotated[str, "A concise summary of the review, highlighting the main points and overall impression."]
    sentiment: Annotated[Literal["positive", "negative"], "The overall sentiment of the review, categorized as 'positive', 'negative'"]
    pros: Annotated[Optional[list[str]], "A list of the positive aspects mentioned in the review, if any. If there are no positive aspects, this can be an empty list or None." ]
    cons: Annotated[Optional[list[str]], "A list of the negative aspects mentioned in the review, if any. If there are no negative aspects, this can be an empty list or None." ]   
    name: Annotated[Optional[str], "The name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)

# print(result['summary'])
# print("******************************")
# print(result['sentiment'])


