import sqlite3


def main() -> None:
    con = sqlite3.connect('words.db')
    cur = con.cursor()
    con.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

    res = con.execute("SELECT name FROM sqlite_master")
    res = res.fetchone()
    print(type(res)) # <class 'tuple'>
    print(res) # ('movie',)


if __name__ == '__main__':
    main()

