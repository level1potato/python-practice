def count_words(sentence):
    words = sentence.split()
    counter = 0

    for word in words:
        counter += 1
    return counter

print(count_words("I love python"))
print(count_words("hello"))
print(count_words(""))
