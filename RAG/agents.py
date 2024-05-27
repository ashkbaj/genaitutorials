# %%
#Part - 3

#multisearch agent rag LLM application

#We will learn about Tools, Toolkit, Agents

!pip install arxiv
!pip install wikipedia
from langchain.tools import google_search

#output = google_search("Tools for multisearch agent rag LLM application")
#print(output)

# %%


from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

apiwraper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200, lang='en')

#print(apiwraper.query_and_summarize("Deep learning"))
tool_wikipedia = WikipediaQueryRun(api_wrapper=apiwraper)
tool_wikipedia.name

# %%
import os
from dotenv import load_dotenv

load_dotenv('../.env.py')
print(os.getenv('OPENAI_API_KEY'))
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings

loader = WebBaseLoader('https://docs.smith.langchain.com/')
docs = loader.load()

documents = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100).split_documents(docs)
vectordb = FAISS.from_documents(documents, OpenAIEmbeddings())
retriever1 = vectordb.as_retriever()

retriever1


# %%
from langchain.tools.retriever import create_retriever_tool

documentprompt = ""
retriever_tool = create_retriever_tool(retriever1, "langsmith_search", "Search about langsmith as a framework, for any questions about langsmith capabilities or how to use langsmith")
retriever_tool.name


# %%
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

arxivwrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
tool_arxiv = ArxivQueryRun(api_wrapper=arxivwrapper)
tool_arxiv.name

# %%
tools = [retriever_tool, tool_arxiv, tool_wikipedia]
tools


# %%
%pip install langchain_openai

from langchain.chat_models import ChatOpenAI
llm = ChatOpenAI(model='gpt-3.5-davinci', temperature=0.6)

# %%
#%pip install langchainhub
#Function Agents from hub for prompts

from langchain import hub
prompt = hub.pull("hwchase17/openai-functions-agent")
prompt.messages

# %%
#Agents

from langchain.agents import create_openai_tools_agent
agent = create_openai_tools_agent(llm, tools, prompt)


