def loading(battery):
    if not battery == 100:
        return f'{battery}% [{"%" * (battery // 10) + "." * (10 - battery // 10)}]\nStill loading...'
    else:
        return f'{battery}% Complete!\n[{"%" * 10}]'

the_battery = int(input())
print(loading(the_battery))