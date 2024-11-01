def write_txt(filename:str, extracted_words: list[str] or str):
    """
    Записывает извлеченные слова в текстовый файл.

    Args:
    filename (str): Имя файла для сохранения
    extracted_words (list[str]): Список извлеченных слов

    Returns:
    None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        for word in extracted_words:
            f.write(f"{word}\n")
    print(f'Слова сохранены в {filename}')