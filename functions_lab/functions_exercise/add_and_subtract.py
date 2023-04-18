def sum_numbers(first_received_number, second_received_number):
    return first_received_number + second_received_number

def subtract(three_received_number):
    return sum_numbers(first_number,second_number) - three_received_number

first_number = int(input())
second_number = int(input())
three_number = int(input())

print(subtract(three_number))