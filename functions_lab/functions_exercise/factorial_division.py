def factorial(first_receiving_number, second_receiving_number):
    first_factorial = 1
    second_factorial = 1

    for num in range(2, first_receiving_number + 1):
        first_factorial *= num
    for num in range(2, second_receiving_number + 1):
        second_factorial *= num

    return f'{first_factorial / second_factorial:.2f}'

first_number = int(input())
second_number = int(input())
print(factorial(first_number, second_number))