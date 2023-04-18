def calculator (first_received_number, second_received_number, the_operator):
    if the_operator == "multiply":
        return first_received_number * second_received_number
    elif the_operator == "divide":
        return  first_received_number // second_received_number
    elif the_operator == "add":
        return first_received_number + second_received_number
    elif the_operator == "subtract":
        return first_received_number - second_received_number

operator = input()
first_number = int(input())
second_number = int(input())

print(calculator(first_number,second_number,operator))
