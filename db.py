import sqlite3  # для работы с SQLite базами данных


def add_data(con: sqlite3.Connection, table_name, data_dict: list[tuple[str, int, float]]  ):
    """
    Добавляет данные в указанную таблицу SQLite.
    Args:
       con (sqlite3.Connection): Объект соединения с базой данных SQLite.
       table_name (str): Название таблицы, куда будут добавлены данные.
       data_dict (dict): Словарь, содержащий данные для вставки. Ключи - столбцы, значения - строки.
    Returns:
        None
    """
    # Создаем список значений для вставки
    values = [value for value in data_dict]
    cur = con.cursor()
    cur.executemany(f"INSERT INTO {table_name} VALUES({', '.join(['?' for _ in values])})", data_dict)
    con.commit()

def main() -> None:
    # Устанавливаем соединение с базой данных SQLite
    con = sqlite3.connect('words.db')

    # Создаем объект курсора для выполнения SQL-запросов
    cur = con.cursor()

    # Создаем таблицу 'movie' с колонками title, year и score
    # Используем IF NOT EXISTS, чтобы избежать ошибок при повторном создании таблицы
    cur.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT, year INTEGER, score REAL)")

    # Создаем список данных для вставки
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]

    # Добавляем данные в указанную таблицу
    add_data(con, "movie", data)


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


"""
Задача 2024.11.15.13

(Задача 2024.11.15.12
Что делает запрос SELECT name FROM sqlite_master?)

Исходя из того, что успешный запрос в 12 задаче делается к таблице sqlite_master, 
а в списке таблиц её нет - что можно об этом сказать?

это встроенная таблица в sqlite. она служебная!
"""
