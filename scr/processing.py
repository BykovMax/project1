from typing import Dict, List

import pytz
from dateutil import parser

# from scr.decorators import log


# @log(filename="mylog.txt")
def filter_by_state(list_dict: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param list_dict: Список словарей.
    :param state: Значение, по которому фильтровать (по умолчанию 'EXECUTED').
    :return: Новый список отфильтрованных словарей.
    """
    if state is None:
        state = "EXECUTED"

    new_list_dict = []  # Создаём пустой список для хранения результата
    for item in list_dict:  # Проходим по каждому элементу в list_dict
        if item.get("state") == state:  # Если значение по ключу 'state' совпадает с переданным
            new_list_dict.append(item)  # Добавляем элемент в новый список
    return new_list_dict  # Возвращаем отфильтрованный список


# @log(filename="mylog.txt")
def sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    Формат даты должен быть: 'YYYY-MM-DDTHH:MM:SS.ffffff'.

    :param list_dict: Список словарей, содержащих ключ 'date'.
    :param reverse: Направление сортировки (по убыванию по умолчанию).
    :return: Новый список, отсортированный по дате.
    """

    # Преобразуем строку даты в datetime объект с временной зоной (если её нет, устанавливаем UTC)
    def parse_date(date_str):
        dt = parser.parse(date_str)
        if dt.tzinfo is None:
            # Если дата без временной зоны, добавляем UTC
            dt = dt.replace(tzinfo=pytz.UTC)
        return dt

    return sorted(list_dict, key=lambda x: parse_date(x["date"]), reverse=reverse)


def filter_by_currency(transactions: list[dict], currency_code: str) -> list[dict]:
    """
    Фильтрует транзакции по коду валюты (например, "RUB").
    """
    return [
        tx for tx in transactions if tx.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    ]


#
# mixed_state_data = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
# invalid_date = [
#     [{"id": 1, "date": "2025-13-13T17:16:00.000000"}],  # Неверная дата
#     [{"id": 2, "date": "13.05.25"}],  # Неверный формат
#     [{"id": 3, "date": "2025-05-13T18:04:00+03:00"}],
#     [{"id": 4, "date": "May 13 2025"}],
# ]
#
# if __name__ == "__main__":
#     print(filter_by_state(mixed_state_data))
#     print(sort_by_date(mixed_state_data))
#     print(sort_by_date(invalid_date))
