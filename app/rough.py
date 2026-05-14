from embedder import embed_user_query
from vectordb import search_in_pinecone
from llm import chat_response
from prompts import LLM_PROMPT
query = "What is the marketing team goal"
embed = embed_user_query(query)
query_search = search_in_pinecone(embed, role = "marketing")
#print(query_search)
generated_response = chat_response(query = query, system_prompt = LLM_PROMPT, context=query_search)
print(generated_response)