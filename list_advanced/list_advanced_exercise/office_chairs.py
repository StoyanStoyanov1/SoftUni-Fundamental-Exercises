def office_space (count_rooms):
    result = []
    free_chairs = 0
    on_game = True
    for room in range(1, count_rooms + 1):
        command = input().split()
        chairs = len(command[0])
        visitors = int(command[1])
        if chairs < visitors:
            on_game = False
            result.append(f'{visitors - chairs} more chairs needed in room {room}')
        free_chairs += visitors - chairs
    if on_game:
        result.append(f'Game On, {abs(free_chairs)} free chairs left')

    return result

rooms = int(input())
print('\n'.join(office_space(rooms)))
