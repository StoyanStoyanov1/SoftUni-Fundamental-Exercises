event = input()
counter = 0
while event != "END":
    if event == "dog" or event == "cat" or event == "coding" or event == 'movie':
        counter += 1
    elif event == "DOG" or event == "CAT" or event == "CODING" or event == 'MOVIE':
        counter += 2

    event = input()
if counter > 5:
    print('You need extra sleep')
else:
    print(counter)