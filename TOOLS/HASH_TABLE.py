"HASH TABLES"   #

"""
Нелинейна структура данни, без индекс, която съхранява двойки ключ-стойност.
Позицията на всеки един елемент се определя на база резултата от хешираща
 функция. Подадените ключове биват хеширани. Хешът се трансформира в 
 индекс в рамките на масива.

За вмъкване и достъпване, хеш-функцията се прилага към ключа, за да 
определи индекса, на който да сложи/намери този ключ. 

Хеш функцията трансформира всякакъв тип ключове най-често в числа.
Тя трябва да бъде:
    - стабилна - при подадена една и съща стойност трябва да се генерира 
      един и същи кеш;
    - да бъде сигурна - в някой случай е важно да не може от хеша по 
      обратен път да се разбере каква е стойността, от която е получен.
      При съхранение на пароли в БД. Тогава се използват криптографски хериращи функции

В масива се съхраняват ключовете, които са референция към стойностите, 
които са разположени на различни места в паметта на компютъра.

Употреба.
    - когато искаме бързо да потърсим някакъв елемент ключ. Константна сложност
    - в Питон - Set, Dictionary

Ако имат добър алгоритъм хеш таблиците имат константна средна времева сложност O(1). Ако има много колизии, в най-лошия случай може да достигне до линейна сложност О(n)
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

