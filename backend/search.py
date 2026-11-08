from cfg import pre_processing, documents
from index import build_index

inverted_index, documents_by_id = build_index(documents)

def search(query, inverted_index, documents_by_id, mode='AND'):
    if mode not in ['AND', 'OR']:
        raise ValueError("Invalid mode. Use 'AND' or 'OR'.")

    processed_query = pre_processing(query)
    
    if not processed_query: 
        return []

    # How to handle the search based on the mode (AND/OR)
    if mode == 'OR':
        ids = set()

        for token in processed_query:
            if token in inverted_index:
                ids |= inverted_index[token]
        results = [documents_by_id[doc_id] for doc_id in ids]
        return results

    first_token = processed_query[0]

    if first_token not in inverted_index:
        return []

    ids = inverted_index[first_token].copy()

    # Search token ids in the database
    for token in processed_query[1:]:
        if token not in inverted_index:
            return []
        
        ids = ids & inverted_index[token]

        if not ids:
            return []
        
    results = [documents_by_id[doc_id] for doc_id in ids]
    return results
