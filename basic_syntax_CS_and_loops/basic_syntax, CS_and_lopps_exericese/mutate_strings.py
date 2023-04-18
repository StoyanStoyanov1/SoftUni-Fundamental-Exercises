first_string = input()
second_string = input()

last_print = first_string

for index in range(len(first_string) + 1):
    left_string = second_string[:index + 1]
    right_string = first_string[index + 1:]

    if left_string + right_string == last_print:
        continue

    last_print = left_string + right_string
    print(last_print)
