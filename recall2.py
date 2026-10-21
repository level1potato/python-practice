def count_vowels(text):
    count = 0

    for char in text:
        if char.lower() in "aeiou":
            count += 1
    return(count)

print(count_vowels("hello"))       # 2
print(count_vowels("sky"))         # 0
print(count_vowels("EDUCATION"))   # 5