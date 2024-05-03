from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

print(os.getenv("OPENAI_API_KEY"))

load_dotenv("../.env.py")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

#os.environ["OPENAI_API_KEY"] = "sk-proj-sDfBYiD0PHkbELY1n7OTT3BlbkFJjZdHRcNQXF3sz6JF8Qld"
#os.environ["LANGCHAIN_TRACING_V2"] = "true"
#os.environ["LANGCHAIN_API_KEY"] = "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"
#os.environ["LANGCHAIN_PROJECT"] = "Tutorial1"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helper online assistant. Respond to the queries of customer in a proffessional and polite way."),
        ("user", "Question:{question}")
    ]
)


st.title("Langchain OpenAI")
input_text = st.text_input("Enter topic which you would like to search for")

#CAll OpenAI LLM

llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    #st.write(chain.invoke('question':{input_text}))
    st.write(chain.invoke({'question':input_text}))





