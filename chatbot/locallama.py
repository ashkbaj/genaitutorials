from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = "sk-proj-sDfBYiD0PHkbELY1n7OTT3BlbkFJjZdHRcNQXF3sz6JF8Qld"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"
os.environ["LANGCHAIN_PROJECT"] = "Tutorial1"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are helper online assistant. Respond to the queries of customer in a proffessional and polite way."),
        ("user", "Question:{question}")
    ]
)


st.title("Langchain with Ollama base llama3 model deployed locally:")
input_text = st.text_input("Enter topic which you would like to search for")

#CAll OpenAI LLM

llm = Ollama(model="llama3")
output_parser = StrOutputParser()

chain = prompt|llm|output_parser

if input_text:
    #st.write(chain.invoke('question':{input_text}))
    st.write(chain.invoke({'question':input_text}))

