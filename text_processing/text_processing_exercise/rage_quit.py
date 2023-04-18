text = input().upper()
unique_symbols = ""
current_text = ""
finish_text = ""

for letter in text:

    if not letter.isdigit() and letter not in unique_symbols:
        unique_symbols += letter

    if not letter.isdigit():
        current_text += letter
    else:
        finish_text += current_text * int(letter)
        current_text = ""

print(f"Unique symbols used: {len(unique_symbols)}")
print(finish_text)