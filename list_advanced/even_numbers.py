def index_of_even_numbers (the_numbers):
    found_even_numbers = map(
        lambda number: number if the_numbers[number] % 2 == 0 else "False", range(len(the_numbers))
    )
    result = list(filter(lambda number: number != "False", found_even_numbers))
    return result

list_number = list(map(int, input().split(", ")))
print(index_of_even_numbers(list_number))