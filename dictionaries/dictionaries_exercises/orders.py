command = input()

products = {}

while command != "buy":
    name, price, quantity = command.split()
    if name not in products.keys():
        products[name] = [0, 0]
    products[name][0], products[name][1] = float(price), products[name][1] + int(quantity)
    command = input()


for product_name, total_price in products.items():
    print(f"{product_name} -> {total_price[0] * total_price[1]:.2f}")
