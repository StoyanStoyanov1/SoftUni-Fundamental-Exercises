def sum_of_even_and_odd(the_number):
    even_sum = []
    odd_sum = []
    for digit in the_number:
        if int(digit) % 2 == 0:
            even_sum.append(int(digit))
        else:
            odd_sum.append(int(digit))

    result = f"Odd sum = {sum(odd_sum)}, Even sum = {sum(even_sum)}"
    return result

number = input()
print(sum_of_even_and_odd(number))