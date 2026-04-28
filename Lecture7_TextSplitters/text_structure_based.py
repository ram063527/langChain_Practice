from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a powerful framework for building applications with language models. It provides a simple and intuitive interface for working with language models, allowing developers to easily integrate them into their applications.
With LangChain, you can create chatbots, virtual assistants, and other applications that leverage the capabilities of language models. The framework supports a wide range of language models, including those from OpenAI, Hugging Face, and more."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=250,
    chunk_overlap=0,
)



result = splitter.split_text(text)

print(len(result))
print(result)