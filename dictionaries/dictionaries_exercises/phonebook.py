name = input().split("-")
phone_book = {}
while len(name) > 1:
    phone_book[name[0]] = name[1]
    name = input().split("-")

counter = int(name[0])

for count in range(counter):
    the_name = input()
    if the_name in phone_book:
        print(f"{the_name} -> {phone_book[the_name]}")
    else:
        print(f"Contact {the_name} does not exist.")


