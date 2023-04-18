budget = int(input())
product = input()

while product != "End":
    price_product = int(product)
    budget -= price_product
    if budget < 0:
        print('You went in overdraft!')
        break

    product = input()

else:
    print('You bought everything needed.')

