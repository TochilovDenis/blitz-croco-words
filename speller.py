from pyaspeller import YandexSpeller


def main():
    spell: YandexSpeller = YandexSpeller()
    letters: str = "в суббботу утромъ"
    fixed: str = spell.spelled(letters)
    print(fixed)


if __name__ == '__main__':
    main()

