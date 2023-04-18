count_student = int(input())

all_students = {}
for _ in range(count_student):
    name = input()
    grade = float(input())

    if name not in all_students.keys():
        all_students[name] = []
    all_students[name].append(grade)

for student, grades in all_students.items():
    if sum(grades) / len(grades) >= 4.5:
        print(f'{student} -> {sum(grades) / len(grades):.2f}')
