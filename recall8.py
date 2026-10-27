def is_palindrome(text):
    text = text.lower()

    return text == text[::-1]


print(is_palindrome("level"))    # True
print(is_palindrome("Level"))    # True
print(is_palindrome("hello"))    # False