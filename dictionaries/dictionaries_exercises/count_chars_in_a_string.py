text = input().replace(" ", "")

result = {}

for letter in text:
    if letter not in result.keys():
        result[letter] = 0
    result[letter] += 1

for letter, value in result.items():
    print(f"{letter} -> {value}")
