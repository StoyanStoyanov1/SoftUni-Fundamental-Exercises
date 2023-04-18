import re

text = input()
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
total_money = 0
furniture_names = []

while text != "Purchase":
    result = re.search(pattern, text)

    if result:
        furniture_name, price, quantity = result.groups()
        furniture_names.append(furniture_name)
        total_money += float(price) * int(quantity)

    text = input()

print('Bought furniture:')

for name in furniture_names:
    print(name)

print(f'Total money spend: {total_money:.2f}')
