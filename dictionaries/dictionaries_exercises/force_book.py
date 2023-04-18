command = input()


force_book = {}

while command != "Lumpawaroo":
    if "|" in command:
        is_enjoy = False

        force_side, force_user = command.split(" | ")

        for force in force_book.values():
            if force_user in force:
                is_enjoy = True
                break
        if not is_enjoy:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(" -> ")

        for the_side, the_user in force_book.items():
            if force_user in the_user:
                force_book[the_side].pop(the_user.index(force_user))
                break

        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")
    command = input()

for force_side, force_user in force_book.items():
    if len(force_user) > 0:
        print(f'Side: {force_side}, Members: {len(force_user)}')
        for user in force_user:
            print(f'! {user}')
