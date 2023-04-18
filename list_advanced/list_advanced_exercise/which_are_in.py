def which_are_in(first_sequences, second_sequences):
    result = []
    for first_word in first_sequences:
        for second_word in second_sequences:
            if first_word in second_word:
                result.append(first_word)
                break
    return result

first_string = input().split(", ")
second_string = input().split(", ")
print(which_are_in(first_string, second_string))
