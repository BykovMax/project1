import json
import logging
import os
from typing import Any

# ====== Настройка логгера модуля utils ======
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

# Путь к папке logs (в корне проекта)
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "utils.log")

# Handler + Formatter
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def read_operations_json(path: str) -> list[dict[str, Any]]:
    """
    Читает json-файл с финансовыми транзакциями.

    :param path: Путь к json-файлу.
    :return: Список транзакций (словарей). Если файл пуст, не найден или содержит не список — возвращает [].
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.debug(f"Файл прочитан успешно: {path}")
                return data
            else:
                logger.error(f"Файл не содержит список: {path}")
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
    except json.JSONDecodeError:
        logger.error(f"Неверный формат JSON в файле: {path}")
    return []


# if __name__ == "__main__":
#     from pprint import pprint
#
#     current_dir = os.path.dirname(os.path.dirname(__file__))
#     path = os.path.join(current_dir, "data", "operations.json")
#
#     result = read_operations_json(path)
#     pprint(result)
