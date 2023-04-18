def without_vowels (current_string):
    vowels = ["a", "o", 'u', "e","i"]
    result = [letter for letter in current_string if letter.lower() not in vowels]
    return "".join(result)

string = input()
print(without_vowels(string))
