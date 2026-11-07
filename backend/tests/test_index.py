from cfg import documents
from index import build_index

index, documents_by_id = build_index(documents)

assert index["basics"] == {1, 2, 3}
assert index["c++"] == {1}
assert index["c"] == {2, 3}
assert index["pointers"] == {3}

assert documents_by_id[3]["name"] == "Pointers in C"
assert build_index([]) == ({}, {})

# When we have a repeated word it shouldnt duplicate the id
repeated = [{"id": 9, "tokens": ["game", "game"]}]
assert build_index(repeated)[0] == {"game": {9}}

print("All the tests passed successfully")
