from services.llm import chat_response
from services.prompts import ROUTER_PROMPT

def router(query: str, prompt: str = ROUTER_PROMPT):
    query_type = chat_response(query=query, system_prompt=prompt)
    return query_type