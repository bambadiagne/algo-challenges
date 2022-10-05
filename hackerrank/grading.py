def gradingStudents(grades):
    round_grades = []
    for grade in grades:
        next_mult = ((grade//5)+1)*5
        if (grade < 38):
            round_grades.append(grade)
        elif (next_mult-grade < 3):
            round_grades.append(next_mult)
        else:
            round_grades.append(grade)
    return round_grades
