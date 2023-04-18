def grade_in_word (the_grade):
    if 2 <= the_grade < 3:
        return "Fail"
    elif 3 <= the_grade < 3.5:
        return  "Poor"
    elif 3.5 <= the_grade < 4.5:
        return  "Good"
    elif 4.5 <= the_grade < 5.5:
        return "Very Good"
    elif 5.5 <= the_grade <= 6:
        return "Excellent"

grade = float(input())
print(grade_in_word(grade))