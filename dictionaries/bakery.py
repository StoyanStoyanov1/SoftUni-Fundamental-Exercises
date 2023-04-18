elements = input().split()
bakery = {}

for index in range(0, len(elements), 2):
    key = elements[index]
    value = elements[index + 1]
    bakery[key] = int(value)

print(bakery)