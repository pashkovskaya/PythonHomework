from typing import List


def split(s: str, sep: str = " ") -> List[str]:
    if not sep:
        raise ValueError("empty separator")
    result_list = []
    end_index = s.find(sep)
    while end_index != -1:
        result_list.append(s[: end_index])
        s = s[end_index + len(sep):]
        end_index = s.find(sep)
    result_list.append(s)
    return result_list


my_str = "Hello world"
sep = "l"
substr_list = my_str.split(sep)
print(substr_list)

substr_list = split(my_str, sep=sep)
print(substr_list)
