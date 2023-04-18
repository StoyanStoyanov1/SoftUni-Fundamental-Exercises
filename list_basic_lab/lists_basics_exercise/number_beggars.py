money_in_string = input().split(', ')
beggars = int(input())
money_in_int = []
counter_beggars = 0

the_result = []

for index in money_in_string:
    money_in_int.append(int(index))

while counter_beggars < beggars:
    sum_for_beggar = 0
    for money in range(counter_beggars, len(money_in_int), beggars):
        sum_for_beggar += money_in_int[money]
    the_result.append(sum_for_beggar)
    counter_beggars += 1

print(the_result)




