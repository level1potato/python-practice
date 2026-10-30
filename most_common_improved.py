def most_common(sentence):
    sentence = sentence.lower()
    words = sentence.split()

    if not words:
        return ""

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

print(most_common("The the cat"))      # the
print(most_common("a B b c C c"))      # c
print(repr(most_common("")))           # ''

