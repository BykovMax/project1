from typing import Dict, List


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
