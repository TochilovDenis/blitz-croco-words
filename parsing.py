from pptx import Presentation
from zipfile import ZipFile
import os
from pathlib import Path


SRC = 'src'
ZIP_FILENAME = 'croco-blitz-source.zip'


def cur() -> str:
    return os.path.dirname(os.path.realpath(__file__))


def open_zip(src: str, file_name: str) -> list[str]:
    list_of_prs: list[str] = list()
    with ZipFile(Path(cur()) / src / file_name, 'r') as zFile:
        for info in zFile.infolist():
            list_of_prs.append(info.filename)
        return list_of_prs


if __name__ == "__main__":
    print("\n".join(open_zip(SRC, ZIP_FILENAME)))

    