"ERROR HANDLING"    # https://softuni.bg/trainings/resources/video/79553/video-30-january-2023-diyan-kalaydzhiev-python-advanced-january-2023/3963
# Exception hierarchy   https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
SYNTAX ERROR
    проблем с начина на структориране на кода.
    Python първо прави code parsing и ако открие грешка не изпълнява кода

RUNTIME ERROR
    кодът работи, но има логически проблем. Известни като Exceptions
    програмата crash-ва когато достигне до логическата грешка и ако не бъде handled спира да работи

    UNRECOVERABLE
        грешката може да бъде handled, но е по-добре да оправим кода отколкото да catching
        my_list = [1, 2, 3]
        print(my_list[4])
        
    RECOVERABLE
        handle грешката и казваме на потребителя какво не е наред
        maybe_number = input()
        val = int(maybe_number)'''



''' 
TRY-EXCEPT БЛОК"
    когато в една програма изникнат непредвидени събития има механизъм
    с който програмата може да се справи с тях
    този блок ни помага да очакваме определени exceptions и 
    да заложим код, който да реагира на тях 
    
    TRY
        в него e кодът, който може да доведе до грешка
    EXCEPT
        в него пишем какъв вид грешка очакваме 
        може да опишем множество грешки като започваме от специфичните към общите 
    ELSE
        изпълнява се, ако не влезнем в грешката        
    FINALLY
        изпълнява се винаги, ако не крашне програмата '''

# try:
#     x = int(input("First number: "))
#     y = int(input("Second number: "))
#     print(y / y)
#
# except ValueError:
#     print("This is not a real number :(")
# except ZeroDivisionError:
#     print("Second number can't be zero")
#
# except (ValueError, ZeroDivisionError): # обработване на множество грешки с един except блок
#     print("Invalid input :(")




"ПРЕДИЗВИКВАНЕ НА ГРЕШКИ"   # вдигаме грешка, когато не знаем какво да правим при дадено събитие
# beer = int(input('Колко литри бира има? '))
#
# if beer == 0:
#     raise Exception("Нямаш бира!")
# elif beer < 2:
#     raise Exception("Много е малко")
# else:
#     print("Всичко е наред")




"СОБСТВЕНИ ГРЕШКИ"
# class NoBeer(Exception):
#     '''No beer exception'''
#
# class TooLow(Exception):
#     def __init__(self, amount):
#         super(). __init__(f'{amount} л е твърде малко!')
#
#
# beer_quantity = int(input('Колко литри бира има? '))
# if beer_quantity == 0:
#     raise NoBeer("Няма бира!")
#
# elif beer_quantity < 2:
#     raise TooLow(beer_quantity)
#
# else:
#     print("Всичко е наред!")




"ВРЪЩА ТЕКСТ КАКВО Е ГРЕШНО"    # ще изпише точната грешка
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     print(f"a / b = {a / b}")
# except ValueError as err:
#     print(err)
#     print(err.args)
#     print(err.args[0])



"ПРЕНАПИСВАНЕ НА ГРЕШКАТА"
# try:
#     a = int(input("a = "))
#     b = int(input("b = "))
#     print(f"a / b = {a / b}")
# except Exception as err:
#     print("делене на 0 не става")
#     print("Could not divide on 0. Reason:", err)



"RAISE & HANDLE НА ГРЕШКА"
# def deposit(amount):
#     if amount <= 0:
#         raise ValueError('Error')   # вдигане на грешка
#     print(f'Deposited {amount}.')
#
#
# amounts = [200, 0, 50]
# for amount in amounts:
#     try:
#         deposit(amount)
#     except ValueError as err:       # handle грешка
#         print(err)





class NoInternetConnection(Exception):
    """Exception raised when there is no internet"""

raise NoInternetConnection

