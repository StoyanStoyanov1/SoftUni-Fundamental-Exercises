def palindrome_strings(the_words, the_palindromes):
    palindromes_words = []
    for word in the_words:
        if word == word[::-1]:
            palindromes_words.append(word)

    counter = palindromes_words.count(the_palindromes)
    return f'{palindromes_words}\nFound palindrome {counter} times'

words, palindrome = input().split(), input()
print(palindrome_strings(words,palindrome))
