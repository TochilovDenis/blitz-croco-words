from pyaspeller import YandexSpeller


def check_spelling(words: set[str]) -> list[str]:
    print(f"Проверка {len(words)} слов на правописание с помощью Yandex Speller")
    speller: YandexSpeller = YandexSpeller()
    result_speller: list[str] = speller.spelled(' '.join(words)).split(" ")
    print(f"Проверка орфографии выполнена")
    return result_speller

