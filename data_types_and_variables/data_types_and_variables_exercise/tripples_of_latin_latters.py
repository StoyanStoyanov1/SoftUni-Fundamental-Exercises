n = int(input())

for first_latter in range(ord("a"), ord("a") + n ):
    for second_latter in range(ord("a"), ord("a") + n ):
        for three_latter in range(ord("a"), ord("a") + n ):
            print(f'{chr(first_latter)}{chr(second_latter)}{chr(three_latter)}')
