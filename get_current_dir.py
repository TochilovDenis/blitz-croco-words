import os


def get_current_dir() -> str:
    """
    Получает путь к текущей директории.
    Returns:
    str: Путь к текущей директории.
    """
    # Получаем текущий каталог, в котором находится скрипт
    current_dir: str = os.path.dirname(os.path.realpath(__file__))
    return current_dir


