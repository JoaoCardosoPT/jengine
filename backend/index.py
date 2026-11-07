# we are building an inverted index for the documents
def build_index(documents):
    inverted_index = {}
    documents_by_id = {}

    for doc in documents:
        doc_id = doc['id']
        documents_by_id[doc_id] = doc

        for token in doc['tokens']:
            if token not in inverted_index:
                inverted_index[token] = set()
            inverted_index[token].add(doc_id)

    return inverted_index, documents_by_id
