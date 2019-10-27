from typing import List
from functools import reduce

def foo(lst: List[int]) -> List[int]:
    result = []
    for item in lst:
        index = lst.index(item)
        prod = lambda a,b: a * b
        result.append(reduce(prod, lst[:index], 1) * reduce(prod, lst[index + 1:], 1))
    return result

print(foo([1, 2, 3, 4, 5, 3]))
print(foo([3, 2, 1]))
print(foo([]))
