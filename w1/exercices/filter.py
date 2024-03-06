students = {
    'Aaron': {
        'Physics': 95,
        'Chemistry': 80,
        'Math': 92,
    },
    'David': {
        'Physics': 99,
        'Chemistry': 85,
        'Math': 92,
    },
    'John': {
        'Physics': 92,
        'Chemistry': 84,
        'Math': 89,
    },
    'Danny': {
        'Physics': 93,
        'Chemistry': 82,
        'Math': 91,
    },
    'Zach': {
        'Physics': 97,
        'Chemistry': 86,
        'Math': 93,
    },
}


def check_if_student_qualifies(student_details):
    name, scores = student_details
    condition0 = scores['Physics'] > 95
    condition1 = scores['Chemistry'] > 83
    condition2 = scores['Math'] > 90

    return all([condition0, condition1, condition2])


students_tuple = [(name, scores) for name, scores in students.items()]
qualified_students = dict(filter(check_if_student_qualifies, students_tuple))


print(students_tuple)
print(qualified_students)
