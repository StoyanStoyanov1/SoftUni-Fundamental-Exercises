command = input().split(":")
students = {}

while len(command) > 1:
    name_student, id_number, course = command
    if course not in students:
        students[course] = []
    students[course].append(f"{name_student} - {id_number}")

    command = input().split(":")

searched_course = command[0].replace("_", " ")

for student in students[searched_course]:
    print(student)