from get_current_dir import get_current_dir
from zipfile import ZipFile
from pathlib import Path
from level_2 import get_words_form_file, save_words_to_file
from check_speller import check_spelling

ZIP_FILE: str = 'croco-blitz-source.zip'


def read_archive_file():
    words: set[str] = set()

    with ZipFile(Path(get_current_dir()) / 'src' / ZIP_FILE) as zFile:
        for file in zFile.namelist():
            words.update(get_words_form_file(zFile.open(file)))
    checked_words_string: list[str] = check_spelling(words)
    save_words_to_file(checked_words_string, 'words_2.txt')


def main():
    spell_check: list[str] = ["Колакал", "малако"]
    print(*check_spelling(spell_check))


if __name__ == "__main__":
    main()
    print()
    read_archive_file()