"ERROR HANDALING" #



"ВРЪЩА ДОПЪЛНИТЕЛНО СЪОБЩЕНИЕ"      # към съществуващ клас грешки
# b = 0
# if b == 0:
#     raise IndexError("Ни стаа! Грешка!")


"НОВ КЛАС ГРЕШКА"
# class No_enough_BEER():
#     pass
# b = 0
# if b == 0:
#     raise No_enough_BEER()



"ЗА НЯКОЛКО ВИДА ГРЕШКИ TRY EXEPT"      # влиза в except ако грешката се случи в кода м/у try и except

# try:
#     x = int(input("Pleace, enter a number 1: "))
#     y = int(input("Pleace, enter a number 2: "))
#     print(x/y)

# except ValueError:
#     print("Oops! That was no valid number.")

# # except ZeroDivisionError:
# #     print("Oops! Second number can not be zero.")

# finally:
#     print("Final clause")   

# # или за по-кратко
# # except (ValueError, ZeroDivisionError):
# #     print("Oops! Try again...")

# print("Good bye")



"ДОНАПИСАНА И ПОДРОБНА ИНФОРМАЦИЯ ЗА ГРЕШКАТА"
# try:
#     x = int(input("Въведете число: "))
#     print(10 / x)
    
# except ValueError as e:
#     # print("Грешка: Невалидно число.")
#     print("Съобщение за грешката:", e)


"ВДИГНАТАТА ГРЕШКА СЕ ИЗВЛАЧВА ОТ КЪДЕТО Е ВДИГНАТА ДО EXCEPT БЛОКА"
try:
    a = 5
    if a > 1:
        if a > 2:
            if a > 3:
                raise ValueError("Num is greater than 3")
            
except Exception as error:
    print(error.args[0])
    print(error.args)
