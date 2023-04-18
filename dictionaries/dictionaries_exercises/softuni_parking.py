counter = int(input())

parking = {}

for _ in range(counter):
    command = input().split()
    reg = command[0]
    name = command[1]

    if reg == "register":
        number = command[2]
        if name not in parking.keys():
             parking[name] = number
             print(f'{name} registered {number} successfully')
        else:
            print(f'ERROR: already registered with plate number {number}')
    else:
        if name in parking.keys():
            print(f'{name} unregistered successfully')
            del parking[name]
        else:
            print(f'ERROR: user {name} not found')

for name, number in parking.items():
    print(f'{name} => {number}')
