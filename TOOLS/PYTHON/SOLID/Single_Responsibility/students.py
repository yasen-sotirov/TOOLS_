"SINGLE RESPONSIBILITY"     # част от SOLID

# Един клас (и неговите методи) трябва да са отговорни само за едно нещо
# https://www.youtube.com/watch?v=pmjr2QcdbBo&t=1202s&ab_channel=SoftwareUniversity%28SoftUni%29


"СТУДЕНТСКА ЧАСТ"
class Student:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if len(value) >= 3:
            self._name = value
        else:
            raise ValueError('The name must be at least 3 characters.')



"АДМИНИСТРАТИВНА ЧАСТ"
class StudentRecord:
    @staticmethod
    def get_student(id):
        with open('student.txt', 'r') as file:
            for line in file.readline():
                if str(id) == line.split()[0]:
                    return line


    @staticmethod
    def register(student):
        with open('student.txt', 'a') as file:
            file.write(f'id: {student.id}, name: {student.name} \n')



s_record = StudentRecord()

for num in range(1, 21):
    student = Student(num, f'Test_{num}')
    s_record.register(student)


