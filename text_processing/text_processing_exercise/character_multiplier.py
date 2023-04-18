first_text, second_text = input().split()

total_sum = 0

if len(first_text) >= len(second_text):
    for index in range(len(first_text)):
        if index + 1 > len(second_text):
            total_sum += ord(first_text[index])
        else:
            total_sum += ord(first_text[index]) * ord(second_text[index])
else:
    for index in range(len(second_text)):
        if index + 1 > len(first_text):
            total_sum += ord(second_text[index])
        else:
            total_sum += ord(first_text[index]) * ord(second_text[index])

print(total_sum)
