text = input()

result = ""

for letter in text:
    new_letter = ord(letter) + 3
    result += chr(new_letter)

print(result)