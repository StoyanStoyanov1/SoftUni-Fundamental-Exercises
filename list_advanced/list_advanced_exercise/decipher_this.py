def secret_message (secret_text):
    result = []

    for secret in secret_text:
        numbers = ""
        letters = []
        for text in secret:
            if text.isnumeric():
                numbers += text
            else:
                letters.append(text)
        letters[0], letters[-1] = letters[-1], letters[0]
        result.append(f"{chr(int(numbers))}{''.join(letters)}")
    return result

text_input = input().split()
print(' '.join(secret_message(text_input)))