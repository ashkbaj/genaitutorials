import requests
import streamlit as st

def getpoem(input_text):
    payload = {"input": {"topic": input_text},"config": {},"kwargs": {}}
    response = requests.post('http://localhost:9999/poem/invoke', json=payload)
    #print(response.json()['output'])
    return response.json()['output']

def getessay(input_text):
    payload = {"input": {"topic": input_text},"config": {},"kwargs": {}}
    response = requests.post('http://localhost:9999/essay/invoke', json=payload)
    #print(response.json()['output'])
    return response.json()['output']['content']



st.title = "Create Essay or Poem on topic of your Choice"
inputext = st.text_input('Please enter your topic for generating Poem')
inputext2 = st.text_input('Please enter your topic for generating Essay')
#output_essay = st.form_submit_button('Generate Essay')
#output_poem = st.form_submit_button('Generate Poem')

if inputext2 :
    st.write(getessay(inputext))
else:
    st.write(getpoem(inputext))

#st.info(getopenaiResponse('The Beatles'))


#print(getopenaiResponse('The Beatles'))