"""word occurrences
asks for a input and counts the numbers of words"""

word_count = {}
words = input("please, tell me something interesting: ")
words = words.split()

for word in words:
    try:
        word_count[word] += 1
    except KeyError:
        word_count[word] = 1
print(word_count)

words_sorted = list(word_count.keys())
words_sorted.sort()
print(words_sorted)

max_word_length = max(len(word) for word in words_sorted)

for word in words_sorted:
    print("{:{}} : {}".format(word, max_word_length, word_count[word]))
