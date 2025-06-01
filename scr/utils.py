import json
from typing import Any
import os

def read_operations_json(path: str) -> list[dict[str, Any]]:
    """
    Читает json-файл с финансовыми транзакциями.

    :param path: Путь к json-файлу.
    :return: Список транзакций (словарей). Если файл пуст, не найден или содержит не список — возвращает [].
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data =json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Данные не являются списком!")
    except FileNotFoundError:
        print("Файл не найден")
    except json.JSONDecodeError:
        print("Ошибка: файл не в формате JSON!")
    return []


# if __name__ == "__main__":
#     from pprint import pprint
#
#     current_dir = os.path.dirname(os.path.dirname(__file__))
#     path = os.path.join(current_dir, "data", "operations.json")
#
#     result = read_operations_json(path)
#     pprint(result)
