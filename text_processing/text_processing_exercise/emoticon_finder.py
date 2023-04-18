text = input()

for index in range(len(text)):
    if text[index] == ":":
        print(f"{text[index]}{text[index + 1]}")