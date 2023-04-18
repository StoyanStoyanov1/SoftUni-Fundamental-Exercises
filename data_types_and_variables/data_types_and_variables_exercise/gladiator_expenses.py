lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_counter = 0
sword_counter = 0
shield_counter = 0
armor_counter = 0

for lost_fight in range(1, lost_fight_count + 1):
    if lost_fight % 2 == 0:
        helmet_counter += 1
    if lost_fight % 3 == 0:
        sword_counter += 1
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        shield_counter += 1
        if shield_counter % 2 == 0:
            armor_counter += 1

total_price = helmet_price * helmet_counter \
              + sword_price * sword_counter + \
              shield_price * shield_counter + \
              armor_price * armor_counter

print(f'Gladiator expenses: {total_price:.2f} aureus')