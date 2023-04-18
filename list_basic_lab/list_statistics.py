count_number = int(input())

count_of_positives = []
sum_of_negatives = []

for digit in range(count_number):
    the_number = int(input())
    if the_number >= 0:
        count_of_positives.append(the_number)
    else:
        sum_of_negatives.append(the_number)


print(f'{count_of_positives}\n{sum_of_negatives}')
print(f'Count of positives: {len(count_of_positives)}\nSum of negatives: {sum(sum_of_negatives)}')