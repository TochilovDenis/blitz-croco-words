from get_current_dir import get_current_dir
from zipfile import ZipFile
from pathlib import Path
from level_2 import get_words_form_file, save_words_to_file


ZIP_FILE: str = 'croco-blitz-source.zip'


def read_archive_file():
    words: set[str] = set()

    with ZipFile(Path(get_current_dir()) / 'src' / ZIP_FILE) as zFile:
        for file in zFile.namelist():
            words.update(get_words_form_file(zFile.open(file)))

    save_words_to_file(words, 'words_2.txt')


if __name__ == "__main__":
    read_archive_file()
