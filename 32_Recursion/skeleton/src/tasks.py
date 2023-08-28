from tests import  demo_folder
import os

def traverse_directories(path: str):
    result_list = []
    # # показва всички файлове и папки
    # os.chdir("../")
    # items_in_folder = os.listdir(path)
    #
    # for el in items_in_folder:
    #     # създава пътя на всеки фаил и папка в текущата папка
    #     current_item_path = os.path.join(path, el)
    #
    #     # проверява дали елемента е папка
    #     if os.path.isdir(current_item_path):
    #         # ако е папка, я добавя в списъка
    #         result_list.append(el)
    #         # разширява списъка като извиква същ. функция,
    #         # за да провери какво има в таи папка
    #         result_list.extend(traverse_directories(current_item_path))
    #     else:
    #         # ако е файл, просто го добавя към списъка
    #         result_list.append(el)

    if os.path.isdir(path):
        result_list.append(os.path.basename(path))
        items_in_folder = os.listdir(path)
        for element in items_in_folder:
            sub_path = os.path.join(path, element)
            result_list.extend(traverse_directories(sub_path))

    elif os.path.isfile(path):
        result_list.append(os.path.basename(path))

    return result_list




def find_files(path: str, extension: str):
    result_list = []
    if os.path.isdir(path):
        items_in_folder = os.listdir(path)

        for element in items_in_folder:
            sub_path = os.path.join(path, element)

            if os.path.isfile(sub_path) and sub_path.endswith(extension):
                result_list.append(element)
            if os.path.isdir(sub_path):
                result_list.extend(find_files(sub_path, extension))
    return result_list



def file_exists(path: str, file_name: str):
    if os.path.isdir(path):
        items_in_folder = os.listdir(path)
        if file_name in items_in_folder:
            return True

        for element in items_in_folder:
            sub_path = os.path.join(path, element)
            if os.path.isdir(sub_path) and file_exists(sub_path, file_name):
                return True
    return False



def directory_stats(path: str):
    dictionary = {}

    if os.path.isdir(path):
        items_in_folder = os.listdir(path)

        for element in items_in_folder:
            sub_path = os.path.join(path, element)
            if os.path.isfile(sub_path):
                file_path, extension = os.path.splitext(element)
                if extension in dictionary:
                    dictionary[extension] += 1
                else:
                    dictionary[extension] = 1

            elif os.path.isdir(sub_path):
                sub_out = directory_stats(sub_path)
                for extension, count in sub_out.items():
                    if extension in dictionary:
                        dictionary[extension] += count
                    else:
                        dictionary[extension] = count

    return dictionary



