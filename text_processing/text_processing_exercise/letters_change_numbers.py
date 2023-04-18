text = input().split()

total_sum = 0

for word in text:
    current_number = int(word[1:len(word) - 1])
    first_letter = word[0]
    second_letter = word[-1]

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += current_number / first_letter_position
    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += current_number * first_letter_position

    if second_letter.isupper():
        second_letter_position = ord(second_letter) - 64
        total_sum -= second_letter_position
    elif second_letter.islower():
        second_letter_position = ord(second_letter) - 96
        total_sum +=  second_letter_position

print(f'{total_sum:.2f}')