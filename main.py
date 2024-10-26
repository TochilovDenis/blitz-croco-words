import os  # Импорт модуля os для работы с операционной системой


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


def main() -> None:
    # Выводим путь к текущему каталогу
    print(f"Путь: {current_dir()}")


if __name__ == "__main__":
    main()
