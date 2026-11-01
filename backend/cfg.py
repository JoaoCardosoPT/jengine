from data import process_documents 
import string

raw_files = []
doc = process_documents(raw_files)

def pre_processing(tokens):
    tokens = doc.lower()
    tokens = str.maketrans('', '', string.punctuation)
    
