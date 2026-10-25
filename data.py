from files import content
from typing import Any, Dict, List

def process_documents(raw_files: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "id": doc.get("id", ""),
            "name": str(doc.get("name", "")).strip(),
            "content": " ".join(str(doc.get("content", "")).split())
        }
        for doc in raw_files
    ]
