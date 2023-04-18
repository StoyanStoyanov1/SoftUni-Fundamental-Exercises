def price (the_product, the_count):
    coffee = 1.5
    water = 1
    coke = 1.4
    snacks = 2
    if the_product == "coffee":
        return f'{coffee * the_count:.2f}'
    elif the_product == "water":
        return f'{water * the_count:.2f}'
    elif the_product == "coke":
        return f'{coke * the_count:.2f}'
    elif the_product == "snacks":
        return f'{snacks * the_count:.2f}'

product, count = input(), int(input())
print(price(product,count))
