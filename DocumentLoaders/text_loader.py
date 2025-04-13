from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)


parser = StrOutputParser()

loader = TextLoader('cricket_poem.txt',encoding='utf-8')

#in list format
docs = loader.load()

print(type(docs))
#document object it has two things:page_content & metadata
print(docs[0])

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))
