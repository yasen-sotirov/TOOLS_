"КОМПОЗИЦИЯ"    # на принципа HAS - A

# https://translate.google.com/?sl=en&tl=bg&text=Composition%20is%20an%20object%20oriented%20design%20concept%20that%20models%20a%20has%20a%20relationship.%20In%20composition%2C%20a%20class%20known%20as%20composite%20contains%20an%20object%20of%20another%20class%20known%20to%20as%20component.%20In%20other%20words%2C%20a%20composite%20class%20has%20a%20component%20of%20another%20class.%0A%0AComposition%20allows%20composite%20classes%20to%20reuse%20the%20implementation%20of%20the%20components%20it%20contains.%20The%20composite%20class%20doesn%E2%80%99t%20inherit%20the%20component%20class%20interface%2C%20but%20it%20can%20leverage%20its%20implementation.%0A%0AThe%20composition%20relation%20between%20two%20classes%20is%20considered%20loosely%20coupled.%20That%20means%20that%20changes%20to%20the%20component%20class%20rarely%20affect%20the%20composite%20class%2C%20and%20changes%20to%20the%20composite%20class%20never%20affect%20the%20component%20class.%0A%0AThis%20provides%20better%20adaptability%20to%20change%20and%20allows%20applications%20to%20introduce%20new%20requirements%20without%20affecting%20existing%20code.%0A%0AWhen%20looking%20at%20two%20competing%20software%20designs%2C%20one%20based%20on%20inheritance%20and%20another%20based%20on%20composition%2C%20the%20composition%20solution%20usually%20is%20the%20most%20flexible.%20You%20can%20now%20look%20at%20how%20composition%20works.%0A%0AYou%E2%80%99ve%20already%20used%20composition%20in%20our%20examples.%20If%20you%20look%20at%20the%20Employee%20class%2C%20you%E2%80%99ll%20see%20that%20it%20contains%20two%20attributes%3A&op=translate

from typing import Optional


class Engine:
    def __init__(self, power):
        self.power = power
        self.turbo = Optional

    def start(self):
        try:
            line = input("дай газ: ")
            if line == "газ":
                return line

        except ValueError:
            print("Грешка")


class Wheel:
    def __init__(self, car_engine: Engine):
        self.engine = car_engine

    def rotate(self):
        print("Rotate")


class Car:
    def __init__(self, wheels: Wheel):
        self.wheels = wheels

    def drive(self):
        print("Car is driving")


engine = Engine(100)
wheels = Wheel(engine)
car_obj = Car(wheels)

# print(car_obj.wheels.engine.power)      # 100
# print(car_obj.wheels.rotate())          # rotate,  None
# print(car_obj.drive())
# Car is driving,  None

car_obj.wheels.engine.start()

















"ВЛАГАНЕ НА КЛАСОВЕТЕ КАТО АТРИБУТИ"

# class Engine:
#     # няма конструктор, защото ползваме само методите
#     def engine_start(self):
#         print("drive")
#         return "дава газ"
#
# class Wheels:
#     # няма конструктор, защото ползваме само методите
#     def rotate(self):
#         print("rotate")
#         return "търкалят се"
#
# class Car:
#     # няма нужда да се описват след self, директно вземат от класа
#     def __init__(self):             # (self, wheels: Wheels, engine: Engine):
#         self.wheels = Wheels()      # композиция на class Engine():
#         self.engine = Engine()      # композиция на class Wheels():
#
#     def drive(self):
#         self.engine.engine_start()
#         self.wheels.rotate()
#
#
# car_obj_1 = Car()
# car_obj_1.drive()
# car_obj_1.wheels.rotate()








