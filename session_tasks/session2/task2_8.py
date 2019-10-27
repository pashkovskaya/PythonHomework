from typing import List, Any

def get_pairs(lst: List[Any]) -> List[tuple]:
    return list(zip(lst[:-1], lst[1:])) or None


lst = [1, 2, 3, 4, 5]
print(get_pairs(lst))
lst = [8]
print(get_pairs(lst))
