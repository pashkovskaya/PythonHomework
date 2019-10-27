def is_palindrome(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]


str = "Hello"
print(str, is_palindrome(str))
str = "Lol"
print(str, is_palindrome(str))
str = "Keeeek"
print(str, is_palindrome(str))
