import os                    # модуль для работы с операционной системой
from pathlib import Path     # модуль для удобного обхода путей в файловой системе
from zipfile import ZipFile  # класс для работы с ZIP-архивами

# Константа имени файла
FILENAME_ZIP: str = "croco-blitz-source.zip"


def read_zip_file():
    """
    Функция чтения ZIP-файла.
    Просматривает содержимое ZIP-файла и выводит список всех файлов внутри архива.
    """

    # Чтение содержимого ZIP-файла и вывод списка всех файлов внутри архива.
    # Использует текущую директорию файла скрипта как путь к ZIP-файлу.
    current_folder = os.path.dirname(os.path.realpath(__file__))

    # Открывает ZIP-файл в текущей директории и читает его содержимое
    with ZipFile(Path(current_folder) / 'src' / FILENAME_ZIP) as archive:
        # Выводит список всех файлов в архиве
        for file_name_zip in archive.namelist():
            print(file_name_zip)


if __name__ == "__main__":
    read_zip_file()
