number_in_string = input().split()
the_opposite_number = []

for index in range(len(number_in_string)):
    opposite_number = -int(number_in_string[index])
    the_opposite_number.append(opposite_number)

print(the_opposite_number)
