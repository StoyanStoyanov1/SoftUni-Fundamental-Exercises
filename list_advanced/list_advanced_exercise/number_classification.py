def positive (numbers):
    return list(filter(lambda num: int(num) >= 0, numbers))
def negative (numbers):
    return list(filter(lambda num: int(num) < 0, numbers))
def even (numbers):
    return list(filter(lambda num: int(num) % 2 == 0, numbers))
def odd (numbers):
    return list(filter(lambda num: int(num) % 2 != 0, numbers))

number = input().split(', ')
print(f'Positive: {", ".join(positive(number))}\n'
      f'Negative: {", ".join(negative(number))}\n'
      f'Even: {", ".join(even(number))}\n'
      f'Odd: {", ".join(odd(number))}')
