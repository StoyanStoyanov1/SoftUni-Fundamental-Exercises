number = int(input())
word = input()

all_words = []

for the_word in range(number):
    the_input = input()
    all_words.append(the_input)

print(all_words)

for the_word in range(len(all_words)):
    element = all_words[the_word]
    if word not in element:
        all_words.remove(element)

print(all_words)