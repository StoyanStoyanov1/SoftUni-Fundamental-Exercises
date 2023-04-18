text = input()
result = ""
for index, letter in enumerate(text):
    if not index + 1 == len(text):
        if letter == text[index + 1]:
            continue
    result += letter

print(result)