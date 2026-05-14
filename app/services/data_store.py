from pathlib import Path
from parse import parse_md
from parse import parse_csv
from chunk import chunk_text
from embedder import embed_chunks
from vectordb import store_in_pinecone

root_dir = "C:/Users/DINESH/Downloads/Codebasics_Project/resources/data"
ROLE_MAP = {
    "finance": ["finance", "executive"],
    "marketing": ["marketing", "executive"],
    "hr": ["hr", "executive"],
    "engineering": ["engineering", "executive"],
    "general": ["employee", "finance", "marketing", "hr", "engineering", "executive"]
}
filepath = []
root = Path(root_dir)
for dept_folder in root.iterdir():
    if dept_folder.is_dir():
        for file_path in dept_folder.iterdir():
            if file_path.is_file():
                filepath.append(file_path)
for f_path in filepath:
    department_name = f_path.parent.name
    file_name = f_path.name
    file_extension = f_path.suffix.lower()
    allowed_roles = ROLE_MAP[department_name]
    file_stem = Path(file_name).stem
    if file_extension == ".md":
        parsed_text = parse_md(f_path)
        chunk = chunk_text(parsed_text)
        embedding = embed_chunks(chunk)
        db_upsert = store_in_pinecone(chunk_list= chunk, embedded_chunks= embedding, 
                                      department_name=department_name, file_name=file_name,file_stem=file_stem,
                                       allowed_roles=allowed_roles, namespace="" )
        print(f"{file_name} upserted in the Vector DB")
    elif file_extension == ".csv":
        parsed_csv = parse_csv(f_path)
        print(f"{file_name} stored in the dataframe")

