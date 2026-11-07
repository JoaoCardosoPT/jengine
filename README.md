# JEngine

A small search engine project built around an in-memory inverted index in Python, with a React interface

> **Status:** Work in progress, im still developing its a interesting project that makes me have a solid foundation in search engines

## How it works

```text
Sample documents
      │
      ▼
Normalize document fields
      │
      ▼
Combine document name and content
      │
      ▼
Lowercase and tokenize
      │
      ▼
Build inverted index + document lookup
```

### Document preprocessing

Each document contains an `id`, a `name`, and `content`. The preprocessing pipeline:

1. Trims whitespace around document names.
2. Collapses repeated whitespace in document content.
3. Combines the name and content so both contribute searchable terms.
4. Converts text to lowercase and extracts tokens using `\w+(?:\+\+|#)?`.

The tokenizer preserves suffixes such as `++` and `#`, allowing terms like `C++` and `C#` to remain single tokens.

```python
pre_processing("How to build a game in C++")
# ['how', 'to', 'build', 'a', 'game', 'in', 'c++']
```

### Inverted index

An inverted index maps each token to a set of document IDs. For the included sample data, part of the index looks like this:

```python
{
    "basics": {1, 2, 3},
    "c++": {1},
    "c": {2, 3},
    "pointers": {3},
}
```

Sets prevent repeated occurrences of a word from adding the same document ID more than once. A separate `documents_by_id` dictionary maps IDs back to complete documents.

This structure makes it possible to retrieve candidate document IDs without scanning every document for each query. It also provides a basis for multi-term queries: intersection for AND matching, or union for OR matching. Those query semantics are not yet implemented.

Index construction visits every token once. With average constant-time dictionary and set operations, its expected time complexity is **O(T)**, where **T** is the total number of token occurrences. The postings store one entry per unique token–document pair; the complete documents and their token lists are also retained in memory.


## Run locally

### Backend

The current Python code uses only the standard library and requires Python 3.9 or later.

From the repository root, run the index checks:

```sh
PYTHONPATH=backend python3 backend/tests/test_index.py
```

The checks cover token-to-document mappings, document lookup, empty input, and duplicate tokens within a document. A successful run prints:

```text
All the tests passed successfully
```

To inspect the index interactively:

```sh
cd backend
python3
```

```python
from cfg import documents
from index import build_index

inverted_index, documents_by_id = build_index(documents)

inverted_index["pointers"]
# {3}

documents_by_id[3]["name"]
# 'Pointers in C'
```

### Frontend

With Node.js and npm installed, use a Node.js version supported by the Vite dependency declared in `frontend/package.json`:

```sh
cd frontend
npm install
npm run dev
```
