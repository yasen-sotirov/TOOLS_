"""
Students order

Alpha students love learning new stuff. They are also aware that switching
seats in the classroom helps them learn new material more effectively.
You are given the names of N students and K seat changes.
Your task is to implement an algorithm that shows the students' final
seating order after all seat changes have been made.

Input
    Read from the standard input.
    On the first line, you'll find the numbers N and K separated by a white space.
        N - the number of students.
        K - the number of seat changes.
    On the next line there will be N student names separated by a white space.
    The next K lines are pairs of student names. Each pair represents a change of seats where the first student sits on the left of the second student.
        The names are separated by a white space.

Output
    Print on the standard output.
    On a single line, print the final order of the student names.

Constraints
    1 <= N <= 2000
    1 <= K <= 100 000
    Each name contains only alphanumeric characters.
    All names are unique.

Sample tests
====== Input
5 3
Gosho Tosho Penka Miro Stanka
Miro Gosho
Gosho Stanka
Stanka Miro

Output
Stanka Miro Tosho Penka Gosho
Explanation

    Miro takes a seat next to Gosho. The order becomes Miro Gosho Tosho Penka Stanka
    Gosho takes a seat next to Stanka. The order becomes Miro Tosho Penka Gosho Stanka
    Stanka takes a seat next to Miro. The order becomes Stanka Miro Tosho Penka Gosho

====== Input
7 4
Emo Misho Ivanka Ginka Vancho Stancho Sashka
Emo Misho
Misho Emo
Misho Sashka
Sashka Stancho

Output
Emo Ivanka Ginka Vancho Sashka Stancho Misho
"""


class Student:
    def __init__(self, name):
        self.name = name
        self.next: Student = None
        self.prev: Student = None


class Order:
    def __init__(self):
        self.head: Student = None
        self.tail: Student = None


    def add_after(self, student: Student):
        prev_student = Student
        if self.head is None:
            self.head = student
            self.tail = student
            prev_student = student
        else:
            prev_student = self.tail
            self.tail = student
            student.prev = prev_student
            prev_student.next = student


    def add_before(self, add_student: Student, before_st: str):
        before_st = first_order[before_st]
        if before_st == self.head:
            add_student.next = before_st
            before_st.prev = add_student
            self.head = add_student
        else:
            old_fellow = before_st.prev
            old_fellow.next = add_student
            add_student.prev = old_fellow
            add_student.next = before_st
            before_st.prev = add_student


    def get_student(self, student_to_get):
        node = first_order[student_to_get]
        if node == self.head:
            next_node = node.next
            next_node.prev = None
            self.head = next_node
        elif node == self.tail:
            prev_node = node.prev
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            next_node.prev = prev_node
        node.next = None
        node.prev = None
        return node


all_students, desk = [int(el) for el in input().split()]
start_list = input().split()
sequence = Order()
first_order = {}

for current_name in start_list:
    student = Student(current_name)
    sequence.add_after(student)
    first_order[current_name] = student

for pair in range(desk):
    student_to_add, add_before = input().split()

    move_student = sequence.get_student(student_to_add)
    sequence.add_before(move_student, add_before)

temp = sequence.head
while temp:
    print(temp.name, end=" ")
    temp = temp.next





