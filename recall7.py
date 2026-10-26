def reverse_text(text):

    result = ""

    for char in text:
        result = char + result
    return result

print(reverse_text("hello"))   # olleh
print(reverse_text("a"))       # a
print(reverse_text(""))        # (empty line)
