import sqlite3


def main() -> None:
    con = sqlite3.connect('words.db')


if __name__ == '__main__':
    main()

    