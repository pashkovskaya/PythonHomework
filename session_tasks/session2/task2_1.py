def reverse_quotes(s: str) -> str:
    s = s.translate(str.maketrans({"'" : '"', '"' : "'"}))
    return s


str = "Hello 'World'!"
print(str)
new_str = reverse_quotes(str)
print(new_str)
