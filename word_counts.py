def word_counts(sentence):
    sentence = sentence.split()
    counts = {}

    for word in sentence:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_counts("the cat saw the dog"))    # {'the': 2, 'cat': 1, 'saw': 1, 'dog': 1}
print(word_counts("hello"))                  # {'hello': 1}
print(word_counts(""))                       # {}