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


"""
Задача 2024.11.15.10

Что вы узнали в результате работы кода в прошлой задаче?

1. База данных SQLite была успешно подключена и соединение было установлено с файлом 'words.db'.
2. Таблица 'movie' была создана в базе данных SQLite. Это подтверждается тем фактом, что запрос SELECT name FROM sqlite_master возвращает результат.
3. Результат запроса SELECT name FROM sqlite_master содержит одну строку с именем таблицы 'movie'.
4. Тип возвращаемого результата - это кортеж (tuple), как показывает вывод типа(res).
5. Значение кортежа - строка 'movie', что подтверждает наличие таблицы с таким именем в базе данных.
6. Это указывает на то, что предыдущий запрос создания таблицы успешно выполнился и таблица 'movie' была добавлена в базу данных SQLite.

Таким образом, код подтвердил успешное подключение к базе данных, создание таблицы 'movie' и ее существование в базе данных SQLite.
"""
