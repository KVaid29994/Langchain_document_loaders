from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template= "Write a summaru for following text {text}", input_variables=["text"])


# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

loader = TextLoader(r"C:\Users\kanha\Desktop\GenAI\Langchain_document_loaders\cricket.txt", encoding= "utf-8")
docs = loader.load()

print (docs[0].page_content)
print (docs[0].metadata)
print (type(docs[0]))
print (len(docs))

chain = prompt | model | parser

print (chain.invoke({"text":docs[0].page_content}))