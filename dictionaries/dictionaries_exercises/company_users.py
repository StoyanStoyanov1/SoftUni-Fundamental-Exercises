command = input()

the_companies = {}

while command != "End":
    company, employees = command.split(" -> ")
    if company not in the_companies.keys():
        the_companies[company] = []
    if employees not in the_companies[company]:
        the_companies[company].append(employees)
    command = input()

for company, employees in the_companies.items():
    print(company)
    for employ in employees:
        print(f'-- {employ}')