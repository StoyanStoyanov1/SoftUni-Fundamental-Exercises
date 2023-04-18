the_cards = input().split()
faro_shuffles = int(input())

half_deck = len(the_cards) // 2

for shuffles in range(faro_shuffles):
    the_shuffles_deck = []
    for card in range(half_deck):
        left_deck = the_cards[0:half_deck]
        right_deck = the_cards[half_deck::]
        the_shuffles_deck.append(left_deck[card])
        the_shuffles_deck.append(right_deck[card])
    the_cards = the_shuffles_deck

print(the_cards)




