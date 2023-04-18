command = input()

all_courses = {}

while command != "end":
     course, student = command.split(" : ")

     if course not in all_courses.keys():
         all_courses[course] = []
     all_courses[course].append(student)

     command = input()

for course, students in all_courses.items():
    print(f'{course}: {len(students)}')
    for student in students:
        print(f"-- {student}")
