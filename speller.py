from pyaspeller import YandexSpeller, Word


def speller_text():
    """
    Функция использует библиотеку pyaspeller, которая интегрируется с API Яндекса для проверки орфографии.
    Проверка орфографии целых предложений или отдельных слов
    Предложение вариантов исправления опечаток
    :return: None
    """
    spell: YandexSpeller = YandexSpeller()  # создаем класс YandexSpeller
    letters: str = "в суббботу утромъ"      # определяем строка для проверки
    fixed: str = spell.spelled(letters)     # используем метод spelled() класса YandexSpeller для исправления
    print(fixed)


def speller_word():
    """
    Проверяет орфографию отдельного слова.
    Выводит информацию о правильности слова, вариантах исправления и безопасности от опечаток
    :return: None
    """
    word_to_check: str = "Programm"
    spell_checker: Word = Word(word_to_check)  # создаем объект типа Word для проверки


    # Проверка условия: исправленный вариант слова.
    if spell_checker.correct:
        print(f"Исправленное слово: {spell_checker.correct}")
    else:
        print(f"Слово '{word_to_check}' не содержит опечаток")


    # Проверка условия: список вариантов исправления, если они есть.
    if spell_checker.variants:
        print(f"Варианты исправления для '{word_to_check}': {spell_checker.variants}")
    else:
        print(f"Для слова '{word_to_check}' нет вариантов исправления")


    # Проверка условия: указывает на безопасность слова от опечаток.
    if spell_checker.spellsafe:
        print(f"Слово '{word_to_check}' считается безопасным от опечаток")
    else:
        print(f"Слово '{word_to_check}' не является безопасным от опечаток")


if __name__ == '__main__':
    speller_text()
    speller_word()
