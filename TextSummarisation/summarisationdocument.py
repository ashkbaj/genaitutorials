
import os

os.environ["OPENAI_API_KEY"] = "sk-proj-sDfBYiD0PHkbELY1n7OTT3BlbkFJjZdHRcNQXF3sz6JF8Qld"

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader('data/').load_data()
index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()
print(query_engine.query("Could you summarize the given context? Return your response which covers the key points of the text and does not miss anything important, please."))


import bs4

loader = WebBaseLoader("https://lilianweng.github.io/posts/2023-06-23-agent/")
text = loader.load()
print(text)
