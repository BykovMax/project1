from typing import Dict, List

from datetime import datetime


def filter_by_state(list_dict: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param list_dict: Список словарей.
    :param state: Значение, по которому фильтровать (по умолчанию 'EXECUTED').
    :return: Новый список отфильтрованных словарей.
    """
    new_list_dict = []  # Создаём пустой список для хранения результата
    for item in list_dict:  # Проходим по каждому элементу в list_dict
        if item.get("state") == state:  # Если значение по ключу 'state' совпадает с переданным
            new_list_dict.append(item)  # Добавляем элемент в новый список
    return new_list_dict  # Возвращаем отфильтрованный список


def sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует список словарей по ключу 'date'.
    Формат даты должен быть: 'YYYY-MM-DDTHH:MM:SS.ffffff'.

    :param list_dict: Список словарей, содержащих ключ 'date'.
    :param reverse: Направление сортировки (по убыванию по умолчанию).
    :return: Новый список, отсортированный по дате.
    """
    return sorted(list_dict, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)


test_data = [
    {"id": 1, "state": "EXECUTED", "date": "2024-04-01T10:00:00.000000"},
    {"id": 2, "state": "CANCELED", "date": "2023-03-01T12:30:45.123456"},
    {"id": 3, "state": "EXECUTED", "date": "2025-01-01T08:15:00.000000"},
    {"id": 4, "date": "2022-05-01T09:00:00.000000"},  # без state
]

print(sort_by_date(test_data))
print(filter_by_state(test_data))
