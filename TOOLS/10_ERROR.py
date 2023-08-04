"ERROR HANDALING"   #
# избягваме да ползваме if-else



"TRY-EXCEPT БЛОК"
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
    
#     # изпълнява се винаги
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
