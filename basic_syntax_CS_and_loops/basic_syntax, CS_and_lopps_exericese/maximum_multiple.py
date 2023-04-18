first_number = int(input())
second_number = int(input())

sum = 0

while True:
    if sum + first_number <= second_number:
        sum += first_number
        continue
    elif sum + first_number > second_number:
        print(sum)
        break