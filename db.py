import sqlite3


def main() -> None:
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

    res = con.execute("SELECT name FROM sqlite_master")
    print(type(res))  # <class 'sqlite3.Cursor'>
    print(res)  # <sqlite3.Cursor object at 0x0000019942026F40>


if __name__ == '__main__':
    main()

