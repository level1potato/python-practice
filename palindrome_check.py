def is_palindrome(text):
    
    text = text.lower()
  
    return text == text[::-1]

# def is_palindrome(text):
#     text = text.lower()
    
#     reverse = text[::-1]

#     if reverse == text:
#         return True
#     else:
#         return False

print(is_palindrome("Level"))
print(is_palindrome("level"))     # True
print(is_palindrome("hello"))    # False
print(is_palindrome("a"))        # True  (one letter reads the same both ways)