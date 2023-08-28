"FILE HANDLING"    # РАБОТА С ПАПКИ И ФАЙЛОВЕ
# https://pynative.com/python-list-files-in-a-directory/
import os

" === ПЪТЕКА === "

"АБСОЛЮТЕН и РЕЛАТИВЕН ПЪТ"
# абсолютният започва от началото
# path_abs = "D:\Telerik\Telerik_course_python"
# print(os.path.isabs(path_abs))

# релативният
# path_rel = "TOOLS\Classes_Objects"


"ОТ РЕЛАТИВЕН В АБСОЛЮТЕН"






"ОТ АБСОЛЮТЕН В РЕЛАТИВЕН"
# path_absolut = "D:\Telerik\Telerik_course_python\TOOLS\Classes_Objects"
# print(os.path.relpath(path_rel, "Telerik_course_python"))


"СЪЗДАВАНЕ НА ПЪТЕКА"
# по принцип Windows ползва (\) за пътя "C:\windows\user\hello.txt"
# в python (\) се използва за escape. Mоже да избегнем този проблем кат:
#   изписвам пътя с (\) - path = "C:/windows/user/hello.txt"
#   използвам row string - path = r"C:\windows\user\hello.txt"


"ДОБАВЯ КЪМ ПЪТЕКАТА"
# path_1 = "D:\Telerik\Telerik_course_python"
# path_2 = "TOOLS\Classes_Objects"
# path = os.path.join(path_1, path_2)
# print(os.listdir(path))


"ПРОВЕРЯВА ДАЛИ ПЪТЕКАТА СЪЩЕСТВУВА"
# path_pro = "D:\Telerik\Telerik_course_python"
# print(os.path.exists(path_pro))


"ОТ ПЪТЕКА В ЛИСТ"
# path = os.getcwd()
# print(os.path.exists(path))
# print(os.path.split(path))


"ПОКАЗВА ФАЙЛОВЕ В ПОДДИРЕКТОРИИ"
# rec_dir = os.getcwd()
# print(list(os.walk(rec_dir, "")))




" === ДИРЕКТОРИЯ === "

"ПРОВЕРЯВА ДАЛИ ИМА ФАЙЛ/ПАПКА В ДИРЕКТОРИЯ"
# print(os.path.isdir("demo_folder/test/test_2"))
# print(os.path.isfile("demo_folder/test/demo_file.txt"))



"СЪЗДАВА ПАПКА"
# directory = "demo_folder"
# parent_dir = "D:\Telerik\TOOLS"   # създава пътека
# path = os.path.join(parent_dir, directory)
# os.mkdir(path)
# # или за по на кратко
# os.mkdir("demo_folder/test/test_2")
#
# # в горната папка
# os.mkdir("../test_folder")



"ТЕКУЩАТА РАБОТНА ДИРЕКТОРИЯ"
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())



"ПОКАЗВА ЕЛЕМЕНТИТЕ В ТЕКУЩАТА ПАПКА"
# връща списък
# print(os.listdir("demo_folder/test"))



"ТРИЕ ПАПКА / ФАЙЛ"
# # премахва папката и файловете в нея
# os.rmdir("demo_folder")

# премахва само пътя на файл??
# os.remove("demo_folder/test/test_2/demo_file.txt")







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



"ERROR ПРИ СЪЩЕСТВУВАЩА ПАПКА"
# try:
#     os.mkdir("demo_folder")
# except OSError as err:
#     print(err)