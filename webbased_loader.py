from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(template= "Answer the following question /n {question} fromt the {text}", input_variables=["text", "question"])


# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


url = "https://www.magicbricks.com/owner-property-for-sale-in-mumbai-pppfs"

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print (chain.invoke({"question":"what is the page about?", "text": docs[0].page_content}))