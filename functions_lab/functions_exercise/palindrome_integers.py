def palindrome(the_numbers):
    result = []
    for number in the_numbers:
        if number[0] == number[-1]:
            result.append("True")
        else:
            result.append("False")
    return "\n".join(result)

numbers = list(map(str, input().split(", ")))
print(palindrome(numbers))