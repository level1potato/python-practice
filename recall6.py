def count_vowels(text):
    vowels = "aeiou"
    count = 0
    text = text.lower()
    
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello"))       # 2
print(count_vowels("sky"))         # 0
print(count_vowels("EDUCATION"))   # 5