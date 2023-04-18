counter = int(input())
the_dict = {}

for count in range(counter):
    key = input()
    value = input()
    if key not in the_dict.keys():
        the_dict[key] = []
    the_dict[key].append(value)

for key in the_dict:
    print(f'{key} - {", ".join(the_dict[key])}')

