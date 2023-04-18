from math import ceil

def sequence_of_numbers (all_numbers):
    group_long = ceil(max(all_numbers) / 10)
    result = []
    counter = 1


    for group in range(1, group_long + 1):
        for_group = []
        for number in all_numbers:
            if number in range(counter, group * 10 + 1):
                for_group.append(number)

        result.append(f"Group of {group * 10}'s: {for_group}")

        counter += 10
    return "\n".join(result)

numbers = list(map(int, input().split(", ")))
print(sequence_of_numbers(numbers))