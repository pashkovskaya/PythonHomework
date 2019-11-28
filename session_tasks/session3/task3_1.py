import string


def test_1_1(*strs) -> set:
    if not strings:
        result = set()
    is_first = True
    for s in strs:
        if is_first:
            result = set(list(s.lower()))
            is_first = False
        result = result.intersection(set(list(s.lower())))
    return result


def test_1_2(*strs) -> set:
    result = set()
    for s in strs:
        result = result.union(set(list(s.lower())))
    return result


def test_1_3(*strs) -> set:
    result = set()
    chars = test_1_2(*strs)
    for char in chars:
        counter = 0
        for s in strs:
            if char in s:
                counter += 1
            if counter == 2:
                result.add(char)
                break
    return result


def test_1_4(*strs) -> set:
    alphabet = set(list(string.ascii_lowercase))
    return alphabet.difference(test_1_2(*strs))


strings = ["hello", "world", "python"]
print(test_1_1(*strings))
print(test_1_2(*strings))
print(test_1_3(*strings))
print(test_1_4(*strings))
