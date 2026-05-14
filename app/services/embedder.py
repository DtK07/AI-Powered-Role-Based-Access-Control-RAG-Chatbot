import os
from dotenv import load_dotenv
from openai import OpenAI
from typing import List

load_dotenv()

API_KEY= os.getenv("OPENAI_API_KEY")
client= OpenAI(api_key= API_KEY)

def embed_chunks(Chunk_list: List[str]):
    embedded_chunks = []
    for chunk in Chunk_list:
        response = client.embeddings.create(
            input = chunk,
            model= "text-embedding-3-small")
        embedded_chunks.append(response.data[0].embedding)
    return embedded_chunks

def embed_user_query(query: str):
    response = client.embeddings.create(
        input = query,
        model = "text-embedding-3-small"
    )
    return response.data[0].embedding