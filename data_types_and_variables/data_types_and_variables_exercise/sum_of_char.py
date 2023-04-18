n = int(input())

the_sum = 0

for counter in range(1, n + 1):
    latter = input()
    the_sum += ord(latter)

print(f'The sum equals: {the_sum}')
