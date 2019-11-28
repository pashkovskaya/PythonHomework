def get_longest_word(s: str) -> str or None:
    words = s.split()
    if not words:
        return None
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


my_str = "Python is simple end effective!"
print(get_longest_word(my_str))
my_str = " "
print(get_longest_word(my_str))
