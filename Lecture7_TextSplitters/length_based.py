from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

texLoader = TextLoader('cricket.txt', encoding='utf-8')
pyPdfLoader = PyPDFLoader('UpdatedCAS.pdf')


textDocument = texLoader.load()
pdfDocument = pyPdfLoader.load()

print(len(pdfDocument))

textContent = textDocument[0].page_content

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=10,
    separator=''
)

textResult = splitter.split_text(textContent)

result = []


for doc in pdfDocument:
    # Split each of the document
    docResult = splitter.split_text(doc.page_content)
    # Append the result to the final result list
    result.extend(docResult)


# print(result)


# for chunk in textResult:
#     print(f'Chunk: "{chunk}"\n')




# for chunk in result:
#     print(f'Chunk: "{chunk}"\n')



### ------  MENTOS ZINDAGI ------ ###

# Use split_document instead of split_text if you want to split a list of documents and also want to preserve the metadata of the documents.
# Each split will be a document object with page_content as the chunk and metadata as the metadata of the original document.

document_split_result = splitter.split_documents(pdfDocument)

for i in document_split_result:
    print(f'Chunk: "{i.page_content}"\n')
    print(f'Metadata: {i.metadata}\n')
    print("******************************"*10)