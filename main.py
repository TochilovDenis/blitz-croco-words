from random import randint
from pathlib import Path
from archive_processor import get_list_archive_files, get_extract_pptx_from_zip, get_extract_pptx_text
from file_stream import write_txt
from get_current_dir import get_current_dir
from path_to_archive import SRC, FILENAME_ZIP, EXTRACTION_DIR, PPTX, WORDS_TXT_0, WORDS_TXT_1
from pptx_processor import get_open_pptx_with_pptx_library, get_extract_words_from_pptx


def main() -> None:
    # Выводим путь к текущему каталогу
    print(f"Путь: {get_current_dir()}")

    # Выводим список файлов в архиве
    print("Список файлов в архиве: ")
    get_list_archive_files(SRC, FILENAME_ZIP)
    # Извлекаем файл презентации
    get_extract_pptx_from_zip(SRC, FILENAME_ZIP, EXTRACTION_DIR)
    # Открываем и выводим содержимое выбранной презентации
    open_file_pptx: int = randint(1, 9)
    get_open_pptx_with_pptx_library(EXTRACTION_DIR, PPTX, open_file_pptx)

    # Извлекаем слова из презентации
    extracted_words: list[str] = get_extract_words_from_pptx(EXTRACTION_DIR, PPTX, open_file_pptx)
    # Записываем слова в файл
    write_txt(WORDS_TXT_0, extracted_words)
    print(f"\nОбработка завершена. Слова сохранены в {WORDS_TXT_0}")

    # Извлекаем презентации слова
    zip_file_path: Path = Path(SRC) / FILENAME_ZIP
    words: list[str] = get_extract_pptx_text(zip_file_path)
    # Записываем слова в файл
    write_txt(WORDS_TXT_1, words)
    print(f"\nОбработка завершена. Слова сохранены в {WORDS_TXT_1}")


if __name__ == "__main__":
    main()
