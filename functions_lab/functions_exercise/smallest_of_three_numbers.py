def result(first_received_number, second_received_number, three_received_number):
    all_number = lambda first, second , three: (first, second , three)
    result = all_number(first_received_number,second_received_number,three_received_number)
    return min(result)




first_number = int(input())
second_number = int(input())
three_number = int(input())
print(result(first_number,second_number,three_number))



