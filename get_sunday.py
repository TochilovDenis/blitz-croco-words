"""
Задача 2024.11.06.01

Попробуйте написать даты, когда проходила каждая игра, учитывая что игры проходили по воскресеньям.
"""
from datetime import datetime, timedelta


def generate_sunday_dates(count: int) -> list[str]:
    """
    Функция для генерации списка дат воскресений
    """
    current_date: datetime = datetime.now()  # Текущая дата и время
    sunday_dates: list[str] = list()   # Создаем пустой список для хранения дат воскресений

    # Цикл для генерации заданного количества дат воскресений
    for _ in range(count):
        # Проверяем, является ли текущая дата воскресеньем (суббота - 6)
        if current_date.weekday() == 6:
            # Если это воскресенье, добавляем его дату в список формате YYYY-MM-DD
            sunday_dates.append(current_date.strftime("%Y-%m-%d"))
        # Увеличиваем текущую дату на один день
        current_date += timedelta(days=1)

    return sunday_dates  # Возвращаем список дат воскресений


def main() -> None:
    # список из 24 последних дат воскресений
    sundays: list[str] = generate_sunday_dates(24)
    # Выводим список дат воскресений в одну строку
    print(*sundays)


if __name__ == '__main__':
    main()