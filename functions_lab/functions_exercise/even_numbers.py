def the_even_numbers(received_numbers):
    even_numbers = []
    for number in received_numbers:
        if int(number) % 2 == 0:
            even_numbers.append(int(number))

    return even_numbers

numbers = input().split()
print(the_even_numbers(numbers))