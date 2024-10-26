import os  # Импорт модуля os для работы с операционной системой
from zipfile import ZipFile  # Импорт класса ZipFile из модуля zipfile для работы с zip-файлами
from pathlib import Path # Импорт класса Path из модуля pathlib для удобной работы с путями

# Константы
SRC = 'src'  # Папка с исходным кодом
FILENAME_ZIP = 'croco-blitz-source.zip'  # Имя файла архива


def current_dir() -> str:
    """
    Получает путь к текущей директории.
    Returns:
    str: Путь к текущей директории.
    """

    # Получаем текущий каталог, в котором находится скрипт
    current_folder: str = os.path.dirname(__file__)

    # Возвращаем путь к текущему каталогу
    return current_folder


def list_archive_files() -> list[str]:
    """
    Список всех файлов в zip-архиве.
    Returns:
    list[str]: Список имен файлов в архиве.
    """
    # Открываем zip-файл в текущей директории, в папке src, с именем FILENAME_ZIP
    with ZipFile(Path(current_dir()) / SRC / FILENAME_ZIP, 'r') as zFile:
        # Возвращаем список всех файлов в архиве
         return zFile.namelist()


def main() -> None:
    # Выводим путь к текущему каталогу
    print(f"Путь: {current_dir()}")

    # Выводим список файлов в архиве
    print("Список файлов в архиве: ")
    file_list: list[str] = list_archive_files()
    for file in file_list:
        print(file)


if __name__ == "__main__":
    main()
