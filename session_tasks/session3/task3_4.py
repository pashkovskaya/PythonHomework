def combine_dicts(*dicts: dict) -> dict:
    result = {}
    for d in dicts:
        for key in d:
            if key in result:
                result[key] += d[key]
            else:
                result[key] = d[key]
    return result

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2, dict_3))
