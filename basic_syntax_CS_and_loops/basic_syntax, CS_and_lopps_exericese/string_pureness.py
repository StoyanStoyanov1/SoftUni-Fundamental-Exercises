n = int(input())
pure = True
for a in range(n):
    string = input()
    pure = True

    for i in string:
        if i == '.' or i == ',' or i == "_":
            pure = False

    if not pure:
        print(f'{string} is not pure!')
    else:
        print(f'{string} is pure.')
