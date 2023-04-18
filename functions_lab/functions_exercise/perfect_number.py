def perfect_number(the_number):
    the_sum = []

    for digit in range(1, the_number // 2 + 1):
        if the_number % digit == 0:
            the_sum.append(digit)
    if sum(the_sum) == the_number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_number(number))