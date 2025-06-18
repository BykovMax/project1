import re
from collections import Counter
from typing import Dict, List


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Возвращает список транзакций, в описании которых содержится искомая строка.

    :param data: Список транзакций (словарей)
    :param search: Строка для поиска (можно часть слова)
    :return: Список транзакций, где найдено совпадение в description
    """
    pattern = re.compile(search, re.IGNORECASE)

    return [item for item in data if pattern.search(item.get("description", ""))]


def process_bank_operations(transactions: List[Dict], mapping: Dict[str, str]) -> Dict[str, int]:
    """
    Подсчитывает количество операций по типам на основе шаблонов из mapping.
    """
    counter = Counter()
    for item in transactions:
        description = item.get("description", "").lower()
        for key, category in mapping.items():
            if key.lower() in description:
                counter[category] += 1
    return dict(counter)
