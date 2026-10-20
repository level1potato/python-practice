def count_vowels(text):
    counter = 0

    for char in text:
        if char.lower() in "aeiou":
            counter += 1
    return(counter)

print(count_vowels("Apple"))
print(count_vowels("EDUCATION"))