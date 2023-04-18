number = input().split()
count_remove = int(input())
number_in_int = []

for index in number:
    number_in_int.append(int(index))

sorted_list = sorted(number_in_int)
small_numbers = []

for counter in range(count_remove):
    small_numbers.append(sorted_list[counter])

for index in range(len(small_numbers)):
    number.remove(str(small_numbers[index]))

the_result = ', '.join(number)
print(the_result)