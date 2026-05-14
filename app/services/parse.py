from typing import List
import pandas as pd

def parse_md(file_path) -> List[str]:
    with open (file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return [text]
def parse_csv(file_path) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    return df
