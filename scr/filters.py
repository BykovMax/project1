import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Возвращает список транзакций, в описании которых содержится искомая строка.

    :param data: Список транзакций (словарей)
    :param search: Строка для поиска (можно часть слова)
    :return: Список транзакций, где найдено совпадение в description
    """
    pattern = re.compile(search, re.IGNORECASE)

    return [
        item for item in data
        if pattern.search(item.get("description", ""))
    ]
