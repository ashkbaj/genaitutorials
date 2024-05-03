#OPENAI_API_KEY="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"
OPENAI_API_KEY='sk-proj-sDfBYiD0PHkbELY1n7OTT3BlbkFJjZdHRcNQXF3sz6JF8Qld'
NAME='langchain'
HUGGINGFACE_API_TOKEN = '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'

from langchain_community.llms import OpenAI
#from langchain.llms import OpenAI
#from langchain import HuggingFaceHub
import streamlit as st


#llm_huggingface_flan = HuggingFaceHub(repo_id = "google/flan-t5-xl", huggingfacehub_api_token = HUGGINGFACE_API_TOKEN)
#prompt2 = print(llm_huggingface_flan("What is the name of most popular person in india"))


#llm_openai_text_ada = OpenAI(model_name="text-ada-001", openai_api_key=OPENAI_API_KEY)
#prompt = print(llm_openai_text_ada("What is the name of most popular person in india"))


#Streamlit App

st.title('🦜🔗 Quickstart App')

openai_key=st.sidebar.text_input('Enter your Open API Key')

def generateresponse(input_text):
    llm_openai = OpenAI(temperature=0.8, openai_api_key=openai_key)
    st.info(llm_openai(input_text))

with st.form('input_form'):
    text = st.text_area('Enter Text :', 'Who is the most famous sportsman in india')
    submittedtext = st.form_submit_button('Submit')
    if not openai_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    #if submittedtext and openai_key.startswith('sk-'):
        #generateresponse(text)

##Using Huggingface



