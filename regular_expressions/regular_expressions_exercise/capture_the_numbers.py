import re

text = input()
pattern = r"\d+"
while text:
    result = re.findall(pattern, text)
    if result:
        print(*result, sep=" ", end=" ")
    text = input()