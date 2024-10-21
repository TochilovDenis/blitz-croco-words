import os
from zipfile import ZipFile


def cur():
    current_file = os.path.realpath(__file__)           # текущий файл
    current_directory = os.path.dirname(current_file)   # текущая папка
    return current_directory


PATH_FILE_ZIP = "F:/AcademyTop/blitz-croco-words/src/croco-blitz-source.zip"


def show_zip():
    with ZipFile(PATH_FILE_ZIP, mode="r") as archive:
        for file_name_zip in archive.namelist():
            print(file_name_zip)


if __name__ == "__main__":
    # print(cur())
    show_zip()
