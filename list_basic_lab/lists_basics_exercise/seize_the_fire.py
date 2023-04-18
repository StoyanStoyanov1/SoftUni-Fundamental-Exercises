LOW, MEDIUM, HIGH = range(1, 51), range(51, 81), range(81, 126)

type_of_fire = input().split('#')
water = int(input())
effort = 0
total = 0

print('Cells:')
for fire in range(len(type_of_fire)):
    the_fire = type_of_fire[fire].split(' = ')
    type_fire = the_fire[0]
    the_water = int(the_fire[1])

    if water < the_water:
        continue
    if type_fire == 'Low' and the_water in LOW:
        water -= the_water
        effort += the_water * 0.25
    elif type_fire == 'Medium' and the_water in MEDIUM:
        water -= the_water
        effort += the_water * 0.25
    elif type_fire == 'High' and the_water in HIGH:
        water -= the_water
        effort += the_water * 0.25
    else:
        continue
    total += the_water

    print(f' - {the_water}')

print(f'Effort: {effort:.2f}\nTotal Fire: {total}')
