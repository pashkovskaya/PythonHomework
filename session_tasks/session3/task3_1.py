from typing import List
import string

def test_1_1(*strings) -> set:
    if not strings:
        result = set()
    isFirst = True
    for string in strings:
        if isFirst:
            result = set(list(string.lower()))
            isFirst = False
        result = result.intersection(set(list(string.lower())))
    return result

def test_1_2(*strings) -> set:
    result = set()
    for string in strings:
        result = result.union(set(list(string.lower())))
    return result

def test_1_3(*strings) -> set:
    result = set()
    chars = test_1_2(*strings)
    for char in chars:
        counter = 0
        for string in strings:
            if char in string:
                counter += 1
            if counter == 2:
                result.add(char)
                break
    return result

def test_1_4(*strings) -> set:
    alphabet = set(list(string.ascii_lowercase))
    return alphabet.difference(test_1_2(*strings))


strings = ["hello", "world", "python"]
print(test_1_1(*strings))
print(test_1_2(*strings))
print(test_1_3(*strings))
print(test_1_4(*strings))
