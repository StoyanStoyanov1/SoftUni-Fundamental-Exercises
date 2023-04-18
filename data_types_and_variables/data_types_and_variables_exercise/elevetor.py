n, p = int(input()), int(input())

courses_counter = 0

while n > 0:
    courses_counter += 1
    n -= p

print(courses_counter)

