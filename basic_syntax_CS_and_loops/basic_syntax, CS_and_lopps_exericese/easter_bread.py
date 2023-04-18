budget = float(input())
price_kg_flour = float(input())

price_eggs = price_kg_flour * 0.75
price_milk = price_kg_flour * 1.25

total = price_kg_flour + price_eggs + price_milk * 0.25
colored_eggs = 0
counter = 0

while budget >= total:
    budget -= total
    counter += 1
    colored_eggs += 3
    if counter % 3 == 0:
        colored_eggs -= (counter - 2)

print(f'You made {counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
