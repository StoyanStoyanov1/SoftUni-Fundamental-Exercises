command = input()
products = {}

while command != "statistics":
    key, value = command.split(': ')

    if key not in products:
        products[key] = 0
    products[key] += int(value)

    command = input()

print('Products in stock:')
for product, quantity in products.items():
    print(f'- {product}: {quantity}')

print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")
