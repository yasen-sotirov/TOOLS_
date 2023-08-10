import os


"FILE HANDLING"

# ===== РАБОТА С ПАПКИ И ФАЙЛОВЕ =====
# ====================================


"СЪЗДАВА ПАПКА"
# directory = "demo_folder"
# parent_dir = "D:\Telerik\TOOLS"
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# os.mkdir("demo_folder/test/test_2")

# в горната папка
# os.mkdir("../test_folder")


"ERROR ПРИ СЪЩЕСТВУВАЩА ПАПКА"
# try:
#     os.mkdir("demo_folder")
# except OSError as err:
#     print(err)


"ПОКАЗВА ТЕКУЩАТА РАБОТНА ДИРЕКТОРИЯ"
# print(os.getcwdu())


"ПОКАЗВА ЕЛЕМЕНТИТЕ В ТЕКУЩАТА ПАПКА"
# връща списък
# print(os.listdir("demo_folder/test"))


"ТРИЕ ПАПКА / ФАЙЛ"
# # премахва папката и файловете в нея
# os.rmdir("demo_folder")

# премахва само пътя на файл??
# os.remove("demo_folder/test/test_2/demo_file.txt")


"ПРОВЕРЯВА ДАЛИ ИМА ФАЙЛ/ПАПКА В ДИРЕКТОРИЯ"
# print(os.path.isdir("demo_folder/test/test_2"))
# print(os.path.isfile("demo_folder/test/demo_file.txt"))




# ===== РЕДАКТИРАНЕ НА .TXT =====
# ===============================

"ЗАТВАРЯНЕ НА ФАЙЛ СЛЕД РЕДАКЦИЯ"
# блок, който затваря автоматично след края на кода
# with open("text.txt") as file_2:
#     print(file_2.read())

# команда за затваряне в края на кода
# file_1.close()



"ПИШЕ ВЪВ ФАЙЛ"
# "x" - създава файл, ако го има вдига грешка
# "a" - допълва към текста, създава файл ако го няма
# "w" - пренаписва текста, създава файл ако го няма
# "r", encoding="utf-8" чете кирилица

# file_1 = open("demo_folder/test/test_2/demo_file.txt", "x", encoding="utf-8")
# file_1.writelines('I just REWRITE my first file!\n')
# file_1.close()

# друг синтаксис
# file_path = "demo_folder/test/test_2/demo_file.txt"
# text = "text proba \n"
# file_1 = open(file_path, mode="a")
# file_1.write(text)
# file_1.close()



"ЧЕТЕ НА ФАИЛ"
# with open("demo_folder/test/test_2/test_file.txt", "r", encoding="utf-8") as file_2:
#     print(file_2.read())            # връща string на целия текст от файла
#     print(file_2.readline())        # връща само първия ред
#     print(file_2.readiness())       # връща list като всеки ред е отделен лист

# долните принтове действа заедно
# file_2 = open("demo_folder/test/test_2/test_file.txt", "r", encoding="utf-8")
# print(file_2.read(3))  # връща string с първите „n“ bytes
# print(file_2.read(4))  # връща следващите „n“ bytes
# print(file_2.read())    # връща „n“ bytes до края на текста



"МЕСТИ КУРСОРА НА ПОЗИЦИЯ"
# file.seek(2)



"ТРИЕ СЛЕД КУРСОРА"
# file.truncate(15)







