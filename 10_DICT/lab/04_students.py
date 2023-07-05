""""
You will be receiving names of students, their ID, and a course of programming they
have taken in the format "{name}:{ID}:{course}". On the last line, you will receive
a name of a course in snake case lowercase letters. You should print only the information
of the students who have taken the corresponding course in the format: "{name} - {ID}"
on separate lines.
"""


info = input()
programs = {}

while ':' in info:
    name, points, course = info.split(":")
    if course not in programs.keys():
        programs[course] = {}

    # ако го няма го създава, ако го има го подминава и добавя
    if name not in programs[course]:
        programs[course][name] = 0
    programs[course][name] += int(points)
    info = input()

for key, value in programs[info].items():
    print(f"{key} - {value}")
