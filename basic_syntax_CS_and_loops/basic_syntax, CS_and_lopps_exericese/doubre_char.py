string = input()
the_string = ""
while string != "End":
    if string == "SoftUni":
        string = input()
        continue
    the_string = ""
    for letter in string:
        the_string += letter * 2

    print(the_string)
    string = input()

