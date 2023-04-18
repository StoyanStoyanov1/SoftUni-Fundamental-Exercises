command = input()

results = {}
banned = []
languages = {}

while command != "exam finished":
    command = command.split("-")
    name = command[0]
    language = command[1]

    if len(command) > 2:
        points = command[2]
        if language not in languages:
            languages[language] = 0
        languages[language] += 1

        if language not in results.keys():
            results[language] = []
            results[language].append(name), results[language].append(points)
        else:
            if name in results[language]:
                for index in range(0, len(results[language]), 2):
                    if name == results[language][index] and points > results[language][index + 1]:
                        results[language][index + 1] = points
            else:
                results[language].append(name), results[language].append(points)

    else:
            banned.append(name)

    command = input()

print("Results:")

for key, value in results.items():
    for index in range(0, len(value), 2):
        if value[index] not in banned:
            print(f"{value[index]} | {value[index + 1]}")

print("Submissions:")

for language, count in languages.items():
    print(f'{language} - {count}')
