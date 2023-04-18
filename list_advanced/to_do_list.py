def to_do_notes (the_command):
    result = []
    while the_command != "End":
        text = the_command.split("-")
        number = int(text[0])
        current_string = text[1]
        result.append([number,current_string])
        the_command = input()

    sorted_result = [result[1] for result in sorted(result)]
    return sorted_result

command = input()
print(to_do_notes(command))

