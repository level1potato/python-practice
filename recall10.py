def longest_word(sentence):
    words = sentence.split()
    longest = ""

    for word in words:
        if len(longest) < len(word):
            longest = word
    return longest

print(longest_word("I love programming"))     # programming
print(longest_word("a bbb cc"))               # bbb
print(longest_word(""))                       # (empty line)
