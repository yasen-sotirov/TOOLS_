# values and functions starting with _ usually mean "don't import or use this"
_courses = [
    'Fundamentals',
    'Core Programming'
    'Object-Oriented Programming',
    'Data Structures and Algorithms'
]

def check_for_course(course_name):
    return course_name in _courses