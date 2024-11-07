from pathlib import Path
import os
from datetime import datetime
from get_current_dir import get_current_dir
from zipfile import ZipFile

ZIP_FILE: str = 'croco-blitz-source.zip'


def get_zip_creation_date(zip_path: Path) -> str:
    """
    Получает дату создания zip-файла.

    Args:
    zip_path (str): Путь к zip-файлу.

    Return:
    str: Дата создания zip-файла в формате ISO.
    """
    # Получаем статистику zip-файла
    stats = os.stat(zip_path)
    # Преобразуем временную метку в объект datetime
    dt = datetime.fromtimestamp(stats.st_ctime).date()
    # Возвращаем дату в формате ISO
    return dt.isoformat()


if __name__ == "__main__":
    zip_creation_date = get_zip_creation_date(Path(get_current_dir()) / 'src' / ZIP_FILE)
    print(f"Дата создания архива: {zip_creation_date}")