n = int(input())

for i in range(n):
    the_input = int(input())
    if the_input == 88:
        print('Hello')
    elif the_input == 86:
        print('How are you?')
    elif the_input < 88:
        print('GREAT!')
    else:
        print('Bye.')