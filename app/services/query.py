from services.embedder import embed_user_query
from services.vectordb import search_in_pinecone
from services.llm import chat_response
from services.prompts import LLM_PROMPT

def process_user_query(query: str, role: str):
    embed = embed_user_query(query)
    query_search = search_in_pinecone(embed, role)
    generated_response = chat_response(query= query, system_prompt= LLM_PROMPT,context=query_search)
    return generated_response


