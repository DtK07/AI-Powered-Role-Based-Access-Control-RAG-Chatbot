from typing import List
def chunk_text(text_lst: List[str], chunk_size: int = 900, chunk_overlap: int = 150) -> List[str]:
    chunk_list =[]
    text = "".join(text_lst)
    text_length = len(text)
    start = 0
    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]
        chunk_list.append(chunk)       
        if end >= text_length:
            break
        start = end - chunk_overlap
    return chunk_list