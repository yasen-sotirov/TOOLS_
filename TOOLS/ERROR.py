"ERROR HANDLING"   # https://softuni.bg/trainings/resources/video/79553/video-30-january-2023-diyan-kalaydzhiev-python-advanced-january-2023/3963

# rais - създава грешка. ако грешката се хвърля сама, rais не ни трябва
# избягваме да ползваме if-else


"TRY-EXCEPT БЛОК"

# try:
#     raise IndexError  # вдига грешката
# за да влезем в except-a грешките трябва да са еднакви
# ако оставим except без грешка, ще хване всички грешки и няма да знаем какво точно се е слуучило
# except IndexError:    # хваща грешката
#     print("Error!")   # принтва грешката



# ако обработим с try-except, програмата не спира
# и понеже имаме цикъл, ще ни попита пак
# while True:      
#     try:
#         x = int(input("First number: "))
#         y = int(input("Second number: "))
#         print(y / y)
#         break
#     except ValueError:
#         print("This is not a real number :(")
#     except ZeroDivisionError:
#         print("Second number can't be zero")
    
# изпълнява се винаги, дори ако се вдигне грешка
#     finally:
#         print("Final clause")   
    


"MULTIPLE EXCEPTION"
# обработва множество грешки по един и същи начин
# while True:
#     try:
#         x = int(input("First number: "))
#         y = int(input("Second number: "))
#         print(y / y)
#         break
#     except (ValueError, ZeroDivisionError):
#         print("Invalid input :(")
        


"ПРОВЕРКА ЗА ПОВЕЧЕ ОТ ЕДНА ГРЕШКИ"
param = int(input())
try:
    if param == 0:
        raise ValueError("Параметърът не може да бъде 0.")
    elif param == -1:
        raise ValueError("Параметърът не може да бъде -1.")
    else:
        result = 10 / param
        print(result)
except ValueError as ve:
    print(f"Възникна грешка: {ve}")
except ZeroDivisionError:
    print("Деление на нула не е позволено.")

"""
def process_data(param):
    try:
        if param == 0:
            raise ValueError("Параметърът не може да бъде 0.")
        elif param == -1:
            raise ValueError("Параметърът не може да бъде -1.")
        else:
            result = 10 / param
            return result
    except ValueError as ve:
        print(f"Възникна грешка: {ve}")
    except ZeroDivisionError:
        print("Деление на нула не е позволено.")

# Тестване на функцията
try:
    value = int(input("Въведете параметър: "))
    result = process_data(value)
    print("Резултатът е:", result)
except ValueError:
    print("Невалиден вход.")
except Exception as e:
    print(f"Неочаквана грешка: {e}")
"""




"MULTIPLE EXCEPTION"
# class IntError(Exception):
#     pass
# class StrError(Exception):
#     pass
# class FloatError(Exception):
#     pass
#
# try:
#     x = input("x = ")
#     if isinstance(x, int):
#         raise IntError("Int")
#     if isinstance(x, str):
#         raise StrError("Str")
#     if isinstance(x, float):
#         raise FloatError("Float")
#
# except IntError:
#     print("===")
#



# class B(Exception):
#     pass
#
# class C(B):
#     pass
#
# class D(C):
#     pass
#
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")



"TRY - EXCEPT - ELSE"
# elsa се изпълнява ако не влезнем в грешката
# try:
#     print(int(input()))
# except ValueError as err:
#     print(err)
# else:
#     print("print without err")



"ПОДРОБНО РАЗПИСВАНЕ НА ГРЕШКАТА"
# try:
#     x = int("abc")
# except ValueError:
#     print("Invalid input.")
#     print()

# try:
#     x = int("abc")
# except ValueError as err:
#     print("Could not convert to integer. Reason:", err)




"СОБСТВЕН КЛАС ГРЕШКА"
# class No_enough_BEER(Exception): 
#     # ако сложим (exception) можем да добави и описание на грешката 
#     pass    # това е достатъчно
# b = 0
# if b == 0:
#     raise No_enough_BEER("Трябва да купиш още бира")




"ДОНАПИСАНА И ПОДРОБНА ИНФОРМАЦИЯ ЗА ГРЕШКАТА"
# try:
#     x = int(input("Въведете число: "))
#     print(10 / x)
    
# except ValueError as e:
#     # print("Грешка: Невалидно число.")
#     print("Съобщение за грешката:", e)


"ВДИГНАТАТА ГРЕШКА СЕ ИЗВЛАЧВА ОТ КЪДЕТО Е ВДИГНАТА ДО EXCEPT БЛОКА"
# try:
#     a = 5
#     if a > 1:
#         if a > 2:
#             if a > 3:
#                 raise ValueError("Num is greater than 3")
            
# except Exception as error:
#     print(error.args[0])
#     print(error.args)



"ВРЪЩА ДОПЪЛНИТЕЛНО СЪОБЩЕНИЕ"      
# към съществуващ клас грешки
# b = 0
# if b == 0:
#     raise IndexError("Ни стаа! Грешка!")



"try - except - else"
# ако try сработи логиката се продължава от else:
# while True:
#     try:
#         x = int(input("First number: "))
#         y = int(input("Second number: "))
#     except (ValueError, ZeroDivisionError):
#         print("Invalid input :(")
#     else:
#         print(y / y)
#         break


"ПРОВЕРКА КАКЪВ ВИД ГРЕШКА МИ ХРЪРЛЯ КОДА"
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     print(f"a / b = {a / b}")
# except Exception as err:    # ще изпише точната грешка
#     print(err)

