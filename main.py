import os


def cur():
    current_file = os.path.realpath(__file__)           # текущий файл
    current_directory = os.path.dirname(current_file)   # текущая папка
    return current_directory


if __name__ == "__main__":
    print(cur())
