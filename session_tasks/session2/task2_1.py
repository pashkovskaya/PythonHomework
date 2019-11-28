def reverse_quotes(s: str) -> str:
    s = s.translate(str.maketrans({"'": '"', '"': "'"}))
    return s


my_str = "Hello 'World'!"
print(my_str)
new_str = reverse_quotes(my_str)
print(new_str)
