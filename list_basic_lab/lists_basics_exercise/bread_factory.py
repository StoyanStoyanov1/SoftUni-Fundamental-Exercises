working_day = input().split('|')

word = []
number = []

energy = 100
coins = 100

completed = True
gained_energy = True

for day in working_day:
    day = day.split('-')

    word.append(day[0])
    number.append(int(day[1]))

for the_day in range(len(word)):
    energy_for_day = 0
    if word[the_day] == 'rest':
        for num in range(number[the_day]):
            if energy >= 100:
                print(f'You gained {num} energy.')
                gained_energy = False
                break
            else:
                gained_energy = True
            energy += 1
        if gained_energy:
            print(f'You gained {number[the_day]} energy.')
        print(f'Current energy: {energy}.')
    elif word[the_day] == "order":
        if energy < 30:
            print('You had to rest!')
            energy += 50
            continue
        else:
            energy -= 30
            coins += number[the_day]
            print(f'You earned {number[the_day]} coins.')
    else:
        coins -= number[the_day]
        if coins < 0 :
            print(f'Closed! Cannot afford {word[the_day]}.')
            completed = False
            break
        else:
            print(f'You bought {word[the_day]}.')

if completed:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
