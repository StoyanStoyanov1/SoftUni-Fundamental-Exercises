name_of_gift = input().split()
command = input()

while command != "No Money":
    command = command.split()
    if "OutOfStock" in command:
        for word in range(len(name_of_gift)):
            if command[1] in name_of_gift[word]:
                name_of_gift[word] = "None"

    elif "Required" in command:
        for index in range(len(name_of_gift)):
            if index == int(command[2]):
                name_of_gift[index] = command[1]
    elif 'JustInCase' in command:
        name_of_gift [-1] = command[1]

    command = input()

while "None" in name_of_gift:
    name_of_gift.remove("None")

for word in name_of_gift:
    print(word, end= " ")






