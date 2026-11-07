import re

from files import content
from data import process_documents 

def pre_processing(text: str) -> list[str]:
    text = text.lower()
    tokens = re.findall(r"\w+(?:\+\+|#)?", text)
    return tokens

raw_files = content()
documents = process_documents(raw_files)

for doc in documents:
    text = f"{doc['name']} {doc['content']}"
    doc['tokens'] = pre_processing(text)