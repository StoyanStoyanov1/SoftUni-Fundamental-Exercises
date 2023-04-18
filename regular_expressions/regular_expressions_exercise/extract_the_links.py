import re

text = input()
pattern = r"www.[A-Za-z0-9\-]+\.[a-z]+(\.[a-z]*)*"
while text:

    result = re.search(pattern, text)
    if result:
        print(result.group())

    text = input()
