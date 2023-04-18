def all_characters(first_received_character, second_received_character):
    result = []
    for character in range(ord(first_received_character) + 1, ord(second_received_character)):
        result.append(chr(character))

    return " ".join(result)

first_character = input()
second_character = input()
print(all_characters(first_character, second_character))
