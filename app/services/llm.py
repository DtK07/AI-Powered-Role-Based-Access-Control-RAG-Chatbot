from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY)
def chat_response(query: str, system_prompt: str | None = None, context: str | None = None):
    response = client.chat.completions.create(
        model = "gpt-5.4",
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Query {query} \n Context {context}"}],
        temperature = 0.3
    )
    return response.choices[0].message.content