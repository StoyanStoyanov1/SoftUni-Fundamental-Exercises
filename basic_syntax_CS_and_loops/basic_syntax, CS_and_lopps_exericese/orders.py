n = int(input())
total_price = 0

for i in range(n):
    price_coffee = 0
    price_capsule = float(input())
    days = int(input())
    capsules_day = int(input())
    if price_capsule < 0.01 or price_coffee > 100.00 \
            or days < 1 or days > 31 \
            or capsules_day < 1 or capsules_day > 2000:
        continue

    price_coffee += capsules_day * days * price_capsule
    total_price += price_coffee

    print(f'The price for the coffee is: ${price_coffee:.2f}')

print(f'Total: ${total_price:.2f}')
