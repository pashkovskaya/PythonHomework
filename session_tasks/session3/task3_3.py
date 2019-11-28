def count_letters(s: str) -> dict:
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


print(count_letters(""))
