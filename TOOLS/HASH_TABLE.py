"HASH TABLES"   #

"""
Списък с ключове показващ къде в паметта се намира валюто на този ключ

Хеш таблицата може да се разглежда като структура от данни, 
която използва хеширане, за да асоциира ключове със съответните им стойности 
в паметта. 

Хеширане: Когато се добави ключ и стойност в хеш таблицата, 
системата използва хеш функция, за да генерира уникален хеш код, 
представляващ ключа. Този хеш код се използва като индекс или адрес 
във вътрешната памет на хеш таблицата.

Индексиране в паметта: Стойността (например, данните или обектът), 
свързана с този ключ, се съхранява на конкретния индекс във вътрешната 
памет на хеш таблицата. Този индекс се определя чрез резултата от хеш 
функцията.

Бърз достъп: Когато искате да получите стойността, свързана с даден ключ, 
хеш таблицата използва отново хеш функцията, за да определи индекса в 
паметта, където тази стойност се намира. Това позволява бързо и ефективно 
извличане на стойностите, тъй като времето за търсене е константно O(1)
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def _hash_code(self, key):
        value = 0
        for char in key:
            value = (value + ord(char)) % self.size
            return value

    def set_into_bucket(self, key, value):
        index = self._hash_code(key)
        #  ако клетката в масива е празна
        if not self.data[index]:
            self.data[index] = []
        self.data[index].append((key, value))

    def get_value(self, key):
        index = self._hash_code(key)
        if self.data[index]:
            return self.data[index][0][1]
        return None

    def view(self):
        print([el for el in self.data])


hash_table = HashTable(5)
hash_table.set_into_bucket("Име", "Иван")
hash_table.set_into_bucket("Име", "Данчо")
hash_table.set_into_bucket("Възраст", 30)
hash_table.set_into_bucket("Държава", "България")

print(hash_table.view())

print(hash_table.get_value("Име"))
print(hash_table.get_value("Възраст"))
print(hash_table.get_value("Град"))

