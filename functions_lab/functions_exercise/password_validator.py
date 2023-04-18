def password_validator(received_password):
    result = []
    password_is_valid = True
    digit_counter = 0
    for character in received_password:
        if character.isdigit():
            digit_counter += 1

    if not 6 <= len(received_password) <= 10:
        result.append('Password must be between 6 and 10 characters')
        password_is_valid = False
    if not received_password.isalnum():
        result.append('Password must consist only of letters and digits')
        password_is_valid = False
    if not digit_counter >= 2:
        result.append('Password must have at least 2 digits')
        password_is_valid = False


    if password_is_valid:
        return 'Password is valid'
    else:
        return '\n'.join(result)

password = input()
print(password_validator(password))
