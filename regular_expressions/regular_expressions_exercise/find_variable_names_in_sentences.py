import re

text = input()
pattern = r"\b_([A-Za-z-0-9]+)\b"
result = re.findall(pattern, text)

print(",".join(result))