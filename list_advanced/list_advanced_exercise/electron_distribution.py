def electron_distribution (number_of_electrons):
    shell = 0
    result = []
    while True:
        shell += 1
        position = 2 * shell ** 2
        if sum(result) + position <= number_of_electrons:
            result.append(position)
        else:
            result.append(number_of_electrons - sum(result))
            break
    return result

number = int(input())

print(electron_distribution(number))



