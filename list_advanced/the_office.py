def employees_are_happy(score, factor):
    employees_score = list(map(lambda the_score:the_score * factor, score))
    the_filtered = list(filter(lambda the_score: the_score >= sum(employees_score) / len(employees_score), employees_score))
    if len(the_filtered) >= len(employees_score) / 2:
        return f'Score: {len(the_filtered)}/{len(employees_score)}. Employees are happy!'
    else:
        return f'Score: {len(the_filtered)}/{len(employees_score)}. Employees are not happy!'

score_of_employees = list(map(int, input().split()))
the_factor = int(input())
print(employees_are_happy(score_of_employees, the_factor))