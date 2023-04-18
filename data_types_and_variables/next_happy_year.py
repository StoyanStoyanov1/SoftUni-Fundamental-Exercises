year = int(input())

is_true = False


while not is_true:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    is_true = len(set_year) == len(str(year))

print(year)

