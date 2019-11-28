from typing import List
from functools import reduce
from operator import mul


def foo(lst: List[int]) -> List[int]:
    result = []
    for item in lst:
        index = lst.index(item)
        result.append(reduce(mul, lst[:index], 1) * reduce(mul, lst[index + 1:], 1))
    return result


print(foo([1, 2, 3, 4, 5, 3]))
print(foo([3, 2, 1]))
print(foo([]))
