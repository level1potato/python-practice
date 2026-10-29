def most_common(sentence):
    words = sentence.split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    common = words[0]

    for word in counts:
        if counts[word] > counts[common]:
            common = word
    return common

print(most_common("the cat saw the dog"))     # the
print(most_common("a b b c c c"))             # c
