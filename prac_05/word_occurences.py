"""
Word Occurrences
Estimate: 20 minutes
Actual: 19 minutes
"""

text = input("Text: ").split(" ")
word_to_word_count = {}
for word in text:
    word_count = text.count(word)
    word_to_word_count[word] = word_count

word_to_word_count = dict(sorted(word_to_word_count.items()))
longest_word_length = len(max(word_to_word_count, key=len))
for word, word_count in word_to_word_count.items():
    print(f"{word:{longest_word_length}} : {word_count}")
