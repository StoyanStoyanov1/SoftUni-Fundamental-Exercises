text = input()

remove_symbols = 0
result = ""

for index, symbol in enumerate(text):
    if symbol == ">":
        remove_symbols += int(text[index + 1])
        result += symbol
    elif remove_symbols > 0:
        remove_symbols -= 1
    else:
        result += symbol

print(result)
