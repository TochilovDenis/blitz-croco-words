import sqlite3


def main() -> None:
    con = sqlite3.connect('words.db')
    cur = con.cursor()


if __name__ == '__main__':
    main()

