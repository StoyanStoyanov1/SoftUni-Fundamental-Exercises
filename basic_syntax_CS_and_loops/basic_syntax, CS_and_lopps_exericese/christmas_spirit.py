quantity_of_decorations = int(input())
left_days = int(input())

budget = 0
points = 0

for day in range(1, left_days + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += 2 * quantity_of_decorations
        points += 5
    if day % 3 == 0:
        budget += 8 * quantity_of_decorations
        points += 13
    if day % 5 == 0:
        budget += 15 * quantity_of_decorations
        points += 17
    if day % 10 == 0:
        budget += 23
        points -= 20
        if day == left_days:
            points -= 30

    if day % 15 == 0:
        points += 30




print(f'Total cost: {budget}\nTotal spirit: {points}')






