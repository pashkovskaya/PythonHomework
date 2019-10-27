from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    start_index = 0
    for index in indexes:
        sub_str = s[start_index : index]
        if sub_str:
            result.append(sub_str)
        start_index = index
    sub_str = s[start_index:]
    if sub_str:
        result.append(sub_str)
    return result

str = "pythoniscool,isn'tit?"
print(split_by_index(str, [6, 8, 12, 13, 18]))

str = "no luck"
print(split_by_index(str, [42, 80]))
