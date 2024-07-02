"SCOPE"     # парчето код оформено от идентацията (tab-a навътре)
'''
LEGB

Local       Променливите, дефинирани във функция

Enclosing   При вложени функции. 

Global      Променливите, дефинирани извън която и да е функция или клас. 
            Достъпни са в цялата програма.

Build-in    Вградените функции и модули, които са налични в Python.
'''



"GLOBAL"    # с  statement Global правим променлива от local или
            # enclosing scope достъпна в Global scope.
            # а ако вече е дефинирана се пренаписва
a = 100
print("the variable before global: ", a)
def sum_nums():
    global a
    a = 50
    b = 10
    return a + b

print("function result: ", sum_nums())
print("the variable after global: ", a)

var: str = "a"

"NONLOCAL"  # с  statement nonlocal правим променлива от enclosing scope
            # достъпна в local scope. Aко вече е дефинирана, се пренаписва

def local_scope():
    var = 200
    def enclosing():
        nonlocal var
        var = 300

    enclosing()
    print(var)

local_scope()
print(var)

