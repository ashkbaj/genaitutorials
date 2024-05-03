from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
#from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langserve import add_routes
import os
import uvicorn
from  langchain_community.llms import Ollama
from dotenv import load_dotenv


load_dotenv("../.env.py")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(title='Langchain Server', version='1.0', description='A langchain server from Youtube tutorial')

model = ChatOpenAI()
ollama = Ollama(model='llama3')


add_routes(
    app,
    model,
    path="/api"
)

#Prompts
prompt1 = ChatPromptTemplate.from_template("Write an Essay about: {topic} in 100 words")
prompt2 = ChatPromptTemplate.from_template("Write an poem about: {topic} in 100 words")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)



add_routes(
    app,
    prompt2|ollama,
    path="/poem"
)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=9999)