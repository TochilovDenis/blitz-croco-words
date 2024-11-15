import sqlite3


def main() -> None:
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    con.execute("CREATE TABLE movie(title, year, score)")


if __name__ == '__main__':
    main()

