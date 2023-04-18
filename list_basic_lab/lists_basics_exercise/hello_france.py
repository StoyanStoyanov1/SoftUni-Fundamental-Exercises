MARKUP = 1.40
CLOTHES_MAX_PRICE = 50
SHOES_MAX_PRICE = 35
ACCESSORIES_MAX_PRICE= 20.5
TRAIN_TICKET = 150
receive = input().split("|")
budget = float(input())
items, price = [], []

BEGIN_BUDGET = budget
buy_items = []
for item in range(len(receive)):
    the_item = receive[item].split('->')
    items.append(the_item[0])
    price.append(float(the_item[1]))

for the_item in range(len(items)):

    buy = False
    if items[the_item] == "Clothes":
        if not price[the_item] > CLOTHES_MAX_PRICE and budget >= price[the_item]:
            budget -= price[the_item]
            buy = True
    elif items[the_item] == "Shoes":
        if not price[the_item] > SHOES_MAX_PRICE and budget >= price[the_item]:
            budget -= price[the_item]
            buy = True
    elif items[the_item] == "Accessories":
        if not price[the_item] > ACCESSORIES_MAX_PRICE and budget >= price[the_item]:
            budget -= price[the_item]
            buy = True
    if buy:
        buy_items.append(price[the_item] * 1.4)

for buy in buy_items:
    print(f'{buy:.2f}', end=" ")

if sum(buy_items) + budget >= TRAIN_TICKET:
    print(f'\nProfit: {sum(buy_items) + budget - BEGIN_BUDGET:.2f}\nHello, France!')
else:
    print(f'\nProfit: {sum(buy_items) + budget - BEGIN_BUDGET:.2f}\nNot enough money.')
