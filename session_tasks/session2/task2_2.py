def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]


my_str = "Hello"
print(my_str, is_palindrome(my_str))
my_str = "Lol"
print(my_str, is_palindrome(my_str))
my_str = "Keeeek"
print(my_str, is_palindrome(my_str))
