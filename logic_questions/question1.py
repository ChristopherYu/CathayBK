test_data = [35, 46, 57, 91, 29, 8]


# include handle only one digit
def reverse(grades):
    str_grades = [str(grade).zfill(2) for grade in grades]
    reversed_grades = [grade[::-1] for grade in str_grades]
    return [int(grade) for grade in reversed_grades]


# ignore only one digit
def reverse_v2(grades):
    str_grades = [str(grade) for grade in grades]
    reversed_grades = [grade[::-1] for grade in str_grades]
    return [int(grade) for grade in reversed_grades]


print(reverse_v2(test_data))
