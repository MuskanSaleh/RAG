from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question - \n {question} from the following text {text}',
    input_variables=['question','text']
)


parser = StrOutputParser()
loader = WebBaseLoader('https://python.langchain.com/docs/introduction/')

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'what is langchain?','text':docs[0].page_content}))

