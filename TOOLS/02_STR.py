"""STRING"""    #
# низ от символи, които могат да бъдат обходени
# immutable = не се променя
import re
# МЕТОДИТЕ които работят върху стринга създават нова инстанция, а не променят стринга

txt = "I like bananas!!"
txt_2 = 'Very_much'
txt_3 = "123456"
txt_4 = "1 2 3 4 5 6"
txt_5 = "123abc"
txt_6 = "123 abc"



"ПРЕВРЪЩА STR В ЛИСТ ОТ ЧИСЛА"
# nums = [int(el) for el in input().split(', ')]


"РАЗДРОБЯВА СТРИНГ НА ЕЛЕМЕНТИ"     # връща лист
# print(txt.split())                # разделя по празно място
# print(txt.split(" ", 1))          # разделя на първото съвпадение


"ОТ STR ПРАВИ ЛИСТ ОТ ЧИСЛА"
# list_of_ints = [int(x) for x in txt_3]
# print(list_of_ints)

# list_of_strings = txt_4.split(' ')
# print(list(map(int, list_of_strings)))        # мап-ване


"ЗАМЕНЯ ЕЛЕМЕНТ"    # връща копие на стринга, самия стринг не се променя
# edited = txt.replace("bananas", "apples apples apples")
# print(edited)
# print(edited.replace("apples", "", 1))     # премахва всичките или брой съвпадения

# def concatenate(*args, **kwargs):
#     main_string = ''.join(args)
#     for key, value in kwargs.items():
#         if key in main_string:
#             main_string = main_string.replace(key, value)
#     return main_string
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))


"ПРЕМАХВА ЕЛЕМЕНТ ОТ НАЧАЛОТО И/ИЛИ КРАЯ НА ТЕКСТА"
# print(("   I like bananas   ").strip())
# print(("----I like bananas!!").strip("-!"))
# print(("----I like bananas!!").lstrip("-"))
# print(("----I like bananas!!").rstrip("!"))
    # ще премахне празен ред


"ДОБАВЯ ЕЛЕМЕНТ ОТ НАЧАЛОТО И КРАЯ НА ТЕКСТА"
# print(txt.join('!@'))


"БРОЙ ЕЛЕМЕНТИ В СТРИНГА"
# print(txt.count('n'))


"ASCII ТАБЛИЦА"
# print(f'Кодът на буквата е: {ord("A")}')
# print(f'Буквата е: {chr(100)}')


"СЛАЙСИНГ"                # работи и за лист
# print(txt[2])           # показва кой символ е на индекс
# print(txt[1:9:2])       # показва символи от индекс до индекс със стъпка

# print(txt_3[::-1])
# print(''.join(reversed(txt_3)))


"ГЛАВНИ и МАЛКИ БУКВИ"
print(txt.lower())          # прави всички букви малки
print(txt.upper())          # прави всички букви главни
#
# print(txt_6.islower())      # проверява, ако има букви дали са малки
# print(txt.isupper())        # проверява, ако има букви дали са главни


"БУКВИ ЛИ СА ИЛИ ЧИСЛА"
# print(txt_5.isalnum())        # връща True ако има числа и/или букви в стринга: alpha_numerical
# print(txt_4.isdigit())        # връща True ако всички са числа в стринга
# print(txt_6.isnumeric())      #


"ПОСТАВЯ СЕПАРАТОР МЕЖДУ СТРИНГОВЕТЕ"
# print(txt, txt_2, sep='. . .')


"ВСЯКА БУКВА НА НОВ РЕД"
# for letter in txt:
#     print(letter)


"ПРОВЕРЯВА ДАЛИ СА ЕДНАКВИ"
# print(isinstance('123', str))
# print(isinstance(123, int))
# print(isinstance("123", int))


"ДОБАВЯ ЕЛЕМЕНТИ ПРЕДИ И/ИИЛИ СЛЕД ТЕКСТА"      # прави общо 20 символа
# text = "EPIC"
# print(f'{text:#<20}')
# print(f'{text:_>20}')
# print(f'{text:.^20}')


"ЕВАЛЮИРА СТРИНГА ДО ЧИСЛА"
# print(eval(f"2, 4, 5"))

# from functools import reduce
# def operate(sign, *args):
#     return reduce(lambda x, y: eval(f"{x} {sign} {y}"), args)
# print(operate("+", 1, 2, 3))


"БРОЙ ЗНАЦИТЕ"
# from string import punctuation
# print(len([el for el in txt if el in punctuation]))


"ПОПЪЛВАНЕ НА ТЕМПЛЕИТ"     # стар подход
# template = 'Country": {}, Capital: {} '
# print(template.format('Bulgaria', 'Sofia'))
# print(template.format('UK', 'London'))


"ПАРСВАНЕ НА СТРИНГ"    # превръщане на стринга в число
# str_1 = "12"
# str_2 = "5.6"
# parsed_str_1 = int(str_1)
# parsed_str_2 = float(str_2)
# print(parsed_str_1 + parsed_str_2)

# print(float('12'))
# print(float('1.2'))


"КОНКАТЕНАЦИЯ"
# print("1" + "2" + " " + "Жоро")


"SLICEING - ЧЕТЕ ПО ИНДЕКС СЪС СТЪПКА"  # работи с LIST също

# mix_list = "123456789"
# print(mix_list[2:5:2])      # 35
# print(mix_list[-2])         # 8
# print(mix_list[::-1])       # 987654321
# print(mix_list[-1:])        # 9


"РАЗОПАКОВА СТРИНГА"
# commands = "bg:sofia:varna:burgas"
# commands, *data = commands.split(":")
# print(commands)
# print(data)

