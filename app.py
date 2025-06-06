from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

loader = PyPDFLoader("data/company_policy.pdf")

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)
print(split_docs[1])


# print("Result: ", len(split_docs))
# print("Result: ", split_docs[0].page_content)
# print(docs[0].metadata)
# print(len(docs))

