def min_max_sum(the_numbers):
    return f"The minimum number is {min(the_numbers)}\n" \
             f"The maximum number is {max(the_numbers)}\n" \
             f"The sum number is: {sum(the_numbers)}"

numbers = list(map(int, input().split()))
print(min_max_sum(numbers))
    