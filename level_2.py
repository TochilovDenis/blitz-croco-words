from typing import IO, TextIO
from pptx import Presentation


def is_not_valid(text: str) -> bool:
    return ' ' in text or '-' in text or ':' in text or 'СУПЕРКРОКО' in text


def get_words_form_file(file: IO[bytes] | TextIO) -> list[str]:
    print(f"getting words from {file.name} file")

    prs = Presentation(file)

    result: list[str] = []

    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            if is_not_valid(shape.text):
                continue
            result.append(shape.text.strip())

    print(f"getting words done. got {len(result)} words")

    return result


def save_words_to_file(words: set[str], filename: str) -> None:
    print(f"saving {len(words)} words to {filename} file")

    with open(file=filename, mode='w', encoding='utf-8') as file:
        file.writelines([word + "\n" for word in words])

    print(f"saving words done")