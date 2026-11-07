from cfg import pre_processing
from index import build_index

inverted_index, documents_by_id = build_index(documents)

def search(query, inverted_index, documents_by_id):
    processed_query = pre_processing(query)
    
    if not processed_query:
        return []

    # Search token ids in the database
    for token in processed_query:
        if token not in inverted_index:
            return []
        ids = inverted_index[token]
        results = [documents_by_id[doc_id] for doc_id in ids]
