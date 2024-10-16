from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

def get_embedding_function():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small",api_key=api_key)
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
