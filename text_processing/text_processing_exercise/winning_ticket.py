tickets = [ticket.strip() for ticket in input().split(",")]

winning_symbols = ['@' ,'#' ,'$' ,'^']

for ticket in tickets:

    the_ticket_is_winning = False

    if len(ticket) != 20:
        print("invalid ticket")
        continue

    left_part = ticket[:10]
    right_part = ticket[10:]

    for symbol in winning_symbols:
        if the_ticket_is_winning:
            break

        for length_symbol in range(10, 5, -1):

            win_symbols = symbol * length_symbol

            if win_symbols in left_part and win_symbols in right_part:
                if len(win_symbols) == 10:
                    print(f'ticket "{ticket}" - {length_symbol}{symbol} Jackpot!')
                    the_ticket_is_winning = True
                    break
                else:
                    print(f'ticket "{ticket}" - {length_symbol}{symbol}')
                    the_ticket_is_winning = True
                    break
    if not the_ticket_is_winning:
        print(f'ticket "{ticket}" - no match')




