import streamlit as st
import base64
import openai
import pptx
from pptx.util import Pt, Inches
import os
import dotenv
import email_validator

#result = email_validator.validate_email("ashishasjjb@gmail.com", check_deliverability=False)
#print(result)


dotenv.load_dotenv('.env.py')

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#Font Sizes
Title_font_size = Pt(36)
content_font_size = Pt(16)

def generate_slide_titles(topic: str):
    '''prompt = f"Generate 5 presentation slides titles for the topic {topic}."
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt=prompt,
        max_tokens=200
    )
'''

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)


#generate_slide_titles('The Beatles - Band')

openai.api_key = os.environ['OPENAI_API_KEY']

# new
from openai import OpenAI

client = OpenAI(
    #model="gpt-3.5-turbo",
    api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)


# after
#from openai import OpenAI

#client = OpenAI()

#completion = client.completions.create(model='curie')
topic = "The Beatles - Band"
prompt = f"Generate 5 presentation slides titles for the topic '{topic}'."
#completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
        {
            "role": "user",
            "content": f"Generate 5 presentation slides titles for the topic '{topic}'.",
        },
    ],)
print(completion.choices[0])
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))
print(dict(completion).get('choices')[0])
#print(completion.choices[0].['message']['content'])