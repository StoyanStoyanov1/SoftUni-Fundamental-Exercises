n = int(input())

capacity = 255
receive_water = 0

for tank in range(1 , n + 1):
    receive = int(input())
    if receive_water + receive > 255:
        print('Insufficient capacity!')
        continue
    receive_water += receive

print(receive_water)

