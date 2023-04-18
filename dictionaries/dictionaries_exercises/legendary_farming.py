result = {'shards': 0, "fragments": 0, "motes": 0}

farming = True

while farming:
    farming = input().split()
    for index in range(0, len(farming) , 2):
        value = int(farming[index])
        element = farming[index + 1].lower()

        if element not in result.keys():
            result[element] = 0

        result[element] += value

        if result['shards'] >= 250:
            print('Shadowmourne obtained!')
            result['shards'] -= 250
            farming = False
            break


        elif result['fragments'] >= 250:
            print('Valanyr obtained!')
            result['fragments'] -= 250
            farming = False
            break

        elif result["motes"] >= 250:
            print('Dragonwrath obtained!')
            result["motes"] -= 250
            farming = False
            break

for element, value in result.items():
    print(f"{element}: {value}")
