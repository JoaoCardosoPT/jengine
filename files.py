# these will be replaced with an actual database
from typing import Any, Dict, List

# return a list of dictionaries
def content() -> list[dict[str,  Any]]:
    return [
        {
            "id": 1,
            "name": "How to build a game in c++",
            "content": "learn the basics to build a game"
        },
        {
            "id": 2,
            "name": "Basics of C",
            "content": "learn the basics of C"
        },
        {
            "id": 3,
            "name": "Pointers in C",
            "content": "Learn the basics of pointers in C"
        }, 
    ]
