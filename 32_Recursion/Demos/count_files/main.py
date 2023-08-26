import os

path = os.path.join(os.path.dirname(__file__), 'demo_folder')


def count_files(root_path):
    count = 0
    for child in os.listdir(root_path):
        sub_path = os.path.join(root_path, child)
        if os.path.isdir(sub_path):
            count += count_files(sub_path)
        elif child.endswith('.txt'):
            count += 1

    return count


print(count_files(path))
