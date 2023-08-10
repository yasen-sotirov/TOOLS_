from unittest import TestCase


"""
UNIT TEST           лекция Инес:   https://softuni.bg/trainings/resources/video/70483/video-25-march-2022-ines-kenova-python-oop-february-2022/3591

    Arrange - приготвя данните
    Act     - действие
    Assert  - проверява дали нещата са се случили

"""



class Worker: 
    def __init__(self, name:str, salary: int, energy: int): 
        self.name = name 
        self.salary = salary 
        self.energy = energy 
        self.money = 0 
        
    def work(self): 
        if self.energy <= 0: 
            raise Exception('Not enough energy.') 
        self.money += self.salary 
        self.energy -= 1 
        
    def rest(self): 
        self.energy += 1 
        
    def get_info(self):
        return f'{self.name} has saved {self.money} money.' 



# ==== TESTS =====

class WorkerTest(TestCase):
    def test_worker_is_initialized_correctly(self):
        # Arrange - приготвя данните
        # Act - действие
        worker_1 = Worker("Test", 1500, 10)

        #Assert - проверява дали нещата са се случили
        self.assertEqual("Test", worker_1.name)



"setUp()"
# казва какво да се случи преди всеки тест

"tearDown"
# казва какдо да се случи след всеки тест

"assertEqual()"
# ДАЛИ РЕЗУЛТАТИТЕ СЪВПАДА

"assertNotEqual()"
# ДАЛИ РЕЗУЛТАТИТЕ НЕ СЪВПАДАТ

"assertTrue()"
# свежда ли се до True / False

"assertIn()"
# дали е в масив - set, list, tuple

"assertRaise()"
# хвърля ли грешка