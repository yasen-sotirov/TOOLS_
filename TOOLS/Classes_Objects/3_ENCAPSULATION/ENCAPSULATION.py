"ENCAPSULATION"     # Групиране на атрибути и методи в един клас.
# Това не позволява на външните класове да имат достъп и
# да променят атрибути и методи на клас.
# Това също помага за постигане на скриване на данни (information hiding)
# Getter & Setter дават допълнителна логика и валидация.
# Property - декоратор. променя методите или атрибутите на класа по такъв начин,
# че потребителят да не е необходимо да прави промени в своя код
# първо getter, после setter
# getter без setter може, но обратното не.

"СМИСЛЕНОТО ОБЯСНЕНИЕ"
# https://youtu.be/7DR2P81tAOU?list=PLRQcrKKiAthBcAV9pZYbxTHItwxGuT2cA&t=3890

'''
SETTER - валидира нови инстанции и промени
    когато има създадени getter и setter, при инициализиране на инстанция, 
    Питон минава през тях и прескача конструктора
    '''

class Employee:
    company = "DSK"
    def __init__(self, name: str, family: str, password, salary: int):
        self.name = name
        self.family = family            # public instance attribute
        self.__password = password      # protected instance attribute, няма setter и getter
        self.salary = salary            # property, защото има setter и няма подчертавка
                                        # при инициализиране подава на setter-a, който валидира

    @property
    def salary(self):                   # property-то трябва да е със същото име както атрибута
        return self._salary             # добавя се _ за да не изпадне в рекурсия

    @salary.setter                      # при създаване на инстанция Питон от конструктора
    def salary(self, value):            # ще дойде тук, за да валидира
        if value <= 0:
            raise ValueError("The salary must be positive number!")
        self._salary = value


    "READ-ONLY"     # няма си setter
    @property
    def full_name(self):                # зад property не е задължително за има атрибут
        return f'{self.name} {self.family}'


    "PROTECTED METHOD"
    def __is_password_correct(self, current_password):
        return current_password == self.__password

    def change_password(self, current_password, new_password):
        if self.__is_password_correct(current_password):
            self.__password = new_password



"СЪЗДАВАНЕ НА ИНСТАНЦИЯ"
employee_1 = Employee("Ivan", "Petrov", "pass123", 1500)
# # employee_1 = Employee("Ivan", "Petrov", "pass123", - 1500)
# print(employee_1.salary)



"ПРОМЯНА НА АТРИБУТИ SETTER"
# employee_1.salary = employee_1.salary + 300
# print(employee_1.salary)
#
# employee_1.salary = 0                 # промяната не минава заради валидациите ни
# print(employee_1.salary)



"ПРЕСКАЧАНЕ НА SETTER"                  # директно достъпва _salary, като прескача валидацията
# employee_1._salary = 0
# print(employee_1.salary)


"ДОСТЪПВАНЕ НА PRIVATE-и"               # мрънка, но дава достъп!
# print(employee_1._Employee__is_password_correct("pass"))
# print(employee_1._Employee__password)



"READ-ONLY АТРИБУТИ"                    # само през getter и не може да се променя след инициализация
# print("employee_1 name", employee_1.full_name)
# employee_1.full_name = 'Todor'  # AttributeError: property 'name' of 'Employee' object has no setter



"ИЗКЛЮЧЕНИЕ"        # това записване всъщност създава нов атрибут (чужд на класа)
# employee_1.password = "123pass"
# print(employee_1.password)


