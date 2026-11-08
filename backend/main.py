from search import search, inverted_index, documents_by_id 
from cfg import pre_processing

def main():
    while True:
        query = input("Enter your search: ")
        if query == "":
            continue

        if query.lower() == "exit":
            break
        mode = input("Enter search mode (AND/OR): ").strip().upper()

        if mode != 'AND' and mode != 'OR':
            print("Invalid mode. Please enter 'AND' or 'OR'.")
            continue

        results = search(query, inverted_index, documents_by_id, mode)
        
        if not results:
            print("No results found.")
        else:
            query_tokens = set(pre_processing(query))
            scored_results = []

            for doc in results:
                doc_tokens = set(doc['tokens'])
                score = len(query_tokens & doc_tokens)
                scored_results.append((doc, score))

            scored_results.sort(key=lambda item: (-item[1], item[0]['id']))
            print('Search results:')
            for doc, score in scored_results:
                print(f"Document ID: {doc['id']}, Name: {doc['name']}, Score: {score}")
                print(f"Content: {doc['content']}\n")

if __name__ == "__main__":
    main()