from pinecone import Pinecone
import os
from dotenv import load_dotenv
from typing import List
load_dotenv()
API_KEY = os.getenv("PINECONE_API_KEY")
INDEX = os.getenv("PINECONE_INDEX")
pinecone_client = Pinecone(api_key=API_KEY)
index = pinecone_client.Index(INDEX)
def store_in_pinecone(chunk_list: List[str], embedded_chunks: List[List[str]], department_name: str,
                       file_name: str, file_stem: str,allowed_roles : List[str], namespace: str =""):
    upsert_vectors = []
    for i, (chunk,embedding) in enumerate(zip(chunk_list,embedded_chunks)):
        vector_data ={
            "id": f"{department_name}_{file_stem}_{i}",
            "values": embedding,
            "metadata":{
                "text": chunk,
                "chunk_index": i,
                "department": department_name,
                "source": file_name,
                "allowed_roles": allowed_roles
            }
        }
        upsert_vectors.append(vector_data)
    batch_size = 100
    for i in range(0, len(upsert_vectors), batch_size):
        batch = upsert_vectors[i: i + batch_size]
        index.upsert(vectors = batch, namespace=namespace)

def search_in_pinecone(query_vector: List[float], role: str,  top_k: int = 10, namespace: str = ""):
    results = index.query(
        vector = query_vector,
        top_k= top_k,
        include_metadata= True,
        namespace=namespace
        #filter = {
        #    "allowed_roles" : {"$in" : [role]}
        #}
    )
    return results
