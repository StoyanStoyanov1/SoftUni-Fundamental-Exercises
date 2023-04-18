words = input().split()
words_dict = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in words_dict:
        words_dict[lower_word] = 0
    words_dict[lower_word] += 1

for word, value in words_dict.items():
    if not value % 2 == 0:
        print(word, end=" ")
