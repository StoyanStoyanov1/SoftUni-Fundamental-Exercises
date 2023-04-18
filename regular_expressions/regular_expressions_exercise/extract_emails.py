import re

text = input()
pattern = r"\s(([a-z]+[a-z\_\.\-]*)@[a-z\-]+(\.[a-z]+)+)\b"
result = re.findall(pattern, text)

for res in result:
    print(res[0])