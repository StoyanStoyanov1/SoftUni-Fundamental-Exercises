import re

dates = input()
pattern = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.finditer(pattern, dates)

for date in result:
    print(f"Day: {date.group(1)}, Month: {date.group(3)}, Year: {date.group(4)}")