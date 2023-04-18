def word_even_long_filter(the_text):
    result = []
    for word in the_text:
        if len(word) % 2 == 0:
            result.append(word)

    return "\n".join(result)

text = input().split()
print(word_even_long_filter(text))