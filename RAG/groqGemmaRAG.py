import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFDirectoryLoader
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv("../.env.py")

#Load API Keys from env file

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.title = "Gemma model chatbot with GROQ inferencing"
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question on provided context only.
    Please provide the most accurate response based on question.
    <context>
    {context}
    </context>
    Questions: {input}
    """
)

def vectorEmbeddings():
    if "vectors" not in st.session_state:
    #if st.session_state.vectors is None:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("censusdata")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        #return st.session_state.final_documents

        #Use vector store and store all embedding
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)


prompt1=st.text_input("Ask your question from the documents here:")

if st.button("Create Embeddings"):
    vectorEmbeddings()
    st.write("embeddings created")

import time

if prompt1:
    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    retriever = st.session_state.vectors.as_retreiver()
    retreieval_chain = create_retrieval_chain(document_chain, retriever)
    start = time.process_time()
    response = retreieval_chain.invoke({"input": prompt1})
    st.write(response['answer'])



    #Use Streamlit expander to process and do a similarity search and process context




