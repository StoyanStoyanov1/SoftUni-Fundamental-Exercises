usernames = input().split(", ")

for name in usernames:
    flag = False
    if 3 <= len(name) <= 16:
        for letter in name:
            if not (letter.isalnum() or letter == "_" or letter == "-"):
                flag = True
                break
        if not flag:
            print(name)
