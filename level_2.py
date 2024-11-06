from typing import IO, TextIO
from pptx import Presentation
from datetime import datetime

def is_not_valid(text: str) -> bool:
    return ' ' in text or '-' in text or ':' in text or 'СУПЕРКРОКО' in text


def get_words_form_file(file: IO[bytes] | TextIO) -> list[str]:
    print(f"Получение слов из файла {file.name}")

    prs = Presentation(file)

    result: list[str] = []

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if is_not_valid(shape.text):
                continue
            result.append(shape.text.strip())

    print(f"Получение слов выполнено. получено {len(result)} слов")

    return result


def save_words_to_file(words: list[str] or set[str], filename: str) -> None:
    print(f"Сохранение {len(words)} слов в {filename} файл")

    with open(file=filename, mode='w', encoding='utf-8') as file:
        current_data = datetime.now().date()
        file.writelines(f"{word} : {current_data}\n" for word in words)

    print(f"Готово")