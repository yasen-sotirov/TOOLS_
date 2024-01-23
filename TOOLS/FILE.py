"FILE HANDLING"     # РАБОТА С ПАПКИ И ФАЙЛОВЕ
                    # https://pynative.com/python-list-files-in-a-directory/

'''
FILE АТРИБУТИ
    - име
    - съдържание
    - размер
    - тип: подразбира се от разширението .exe .txt .png '''
    

import os

" === ПЪТ ПЪТЕКА === "
# disc / folders / file_name.py

"АБСОЛЮТЕН ПЪТ"
# абсолютният започва от началото
# path_abs = "D:\Telerik\Telerik_course_python"
# print(os.path.isabs(path_abs))


'''РЕЛАТИВЕН ПЪТ
    при релативният път кой файл ще бъде достъпен се изменя на база на това
    от къде сме стартирали програмата която достъпва файла.
        
    source                  source                  source
        data                    file.txt                data
            file.txt            main.py                     main.py
        main.py                                     file.txt
        
    "data/file.txt"         "file.txt"              "../../file.txt
        
'''




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

''' OPEN - работи с релативни пътища, освен когато трябва да се
    върнем директория назад. Тогава трябва да изчислим абсолютен път
        x - създава файл, ако го има вдига грешка
        a - допълва към текста, създава файл ако го няма
        w - пренаписва текста, създава файл ако го няма
        r - encoding="utf-8" чете кирилица  
        
    CLOSE - затваря файла. Ползва се когато програмата работи 
    дълго време, файлът не се използва и може да се наложи 
    файлът да бъде достъпен от друго място което може   '''


"ОТВАРЯ И ЧЕТЕ ПРИ РЕЛАТИВЕН ПЪТ"
# path = 'ERROR.py'                                   # релативен път
# file_1 = open(path, mode='r', encoding="utf-8")     # отваря файла и чете
# content = file_1.read()
# print(content)
# file_1.close()



"ОТВАРЯ И ЧЕТЕ ПРИ АБСОЛЮТЕН ПЪТ"
# from os import path
# cwd = path.dirname(__file__)        # cwd - current working directory
# file_path = path.join(cwd, '../TOOLS/Classes_Objects/1_CLASS/CLASS.py')
#
# print(__file__)     # името на файла, от където стартираме кода
# print(cwd)          # пътя на файла, от където стартираме кода
# print(file_path)    # сголбеният абсолютен път
#
# file = open(file_path, mode='r', encoding='utf-8')
# content = file.read()
# print(content)
# file.close()


"WITH блок"     # след края на блока затваря файла
# path = "ERROR.py"
# with open(path, mode='r', encoding='utf-8') as file_to_read:
#     content = file_to_read.read()
#     print(content)


''' ЧЕТЕ НА ФАИЛ
    
    STREAM - когато отворим един файл е добре да четем ред по ред от него,
        а не да го зареждаме целя. Така пестим от рам паметта. 
        Stream-а чете ред по ред от файл, без да го зарежда целия. 
        Изтощава се след прочитане. '''

# with open("demo_folder/test/test_2/test_file.txt", "r", encoding="utf-8") as file_2:
#     print(file_2.read())            # връща string на целия текст от файла
#     print(file_2.readline())        # връща само първия ред
#     print(file_2.readiness())       # връща list като всеки ред е отделен лист

# долните принтове действа заедно
# file_2 = open("demo_folder/test/test_2/test_file.txt", "r", encoding="utf-8")
# print(file_2.read(3))  # връща string с първите „n“ bytes
# print(file_2.read(4))  # връща следващите „n“ bytes
# print(file_2.read())    # връща „n“ bytes до края на текста



"ЧЕТЕНЕ И ЗАПАЗВАНЕ НА ИНФОТО ОТ ФАЙЛ"
settings = {}
file_path = '../'
with open(file_path, 'r') as settings_file:
    for line in settings_file:
        key, value = line.split()
        settings[key] = value


"ПРЕЗАПИСВАНЕ НА ФАЙЛ"
new_volume = input('new volume level = ')
settings['volume'] = new_volume

with open(file_path, mode='w') as settings_file:
    for key, value in settings.items():
        settings_file.write(f'{key} {value}\n')



"ПИШЕ ВЪВ ФАЙЛ"
# my_file.write()     записва стринг
# my_file.writelines()     записва много  елементи

# file_1 = open("demo_folder/test/test_2/demo_file.txt", "x", encoding="utf-8")
# file_1.writelines('I just REWRITE my first file!\n')
# file_1.close()        # трябва да се затвори

# друг синтаксис
# file_path = "demo_folder/test/test_2/demo_file.txt"
# text = "text proba \n"
# file_1 = open(file_path, mode="a")
# file_1.write(text)
# file_1.close()


"СЪЗДАВА ФАЙЛ"      #  създава файл, ако го има вдига грешка
# open(file_path, 'x')


"ТРИЕ ФАЙЛ"
# from os import remove
# remove(file_path)



"МЕСТИ КУРСОРА НА ПОЗИЦИЯ"
# file.seek(2)



"ТРИЕ СЛЕД КУРСОРА"
# file.truncate(15)



"ERROR ПРИ СЪЩЕСТВУВАЩА ПАПКА"
# try:
#     os.mkdir("demo_folder")
# except OSError as err:
#     print(err)