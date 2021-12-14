grades=[23,56,69,78]

def gradingStudents(grades):
    # Write your code here
    ar =[]
    for grade in grades:
        if grade <35:
            ar.append(grade)
            continue
        num = 5 - grade%5
        rounded = num + grade
        if num >= 3:
            ar.append(grade)
            continue
        grade = rounded
        ar.append(grade)
    return ar


