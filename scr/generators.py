from typing import Dict, Iterator, List, Union
from scr.decorators import log


def filter_by_currency(transaction: list[Dict], currency_code: str = "RUB") -> Iterator[Dict]:
    """
     Фильтрует транзакции по коду валюты. По умолчанию 'RUB'.

    :param transaction: Список словарей транзакций.
    :param currency_code: Код валюты, по которому фильтровать (например, 'USD').
    :return: Итератор Отфильтрованных транзакций.
    """
    if currency_code is None:
        currency_code = "RUB"

    return (x for x in transaction if x.get("operationAmount", {}).get("currency").get("code") == currency_code)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

    :param transactions: Список словарей транзакций.
    :yield: Возвращает описание транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]


# @log(filename="mylog.txt")
def card_number_generator(start: Union[int, str], end: Union[int, str]) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате 'XXXX XXXX XXXX XXXX'.

    :param start: Начальное значение (целое число от 1 до 9999999999999999).
    :param end: Конечное значение (целое число от 1 до 9999999999999999).
    :yield: Строка с форматированным номером карты.
    """
    # Преобразуем в строки для проверки длины и содержания
    start_str = str(start)
    end_str = str(end)

    # Проверка на цифры
    if not start_str.isdigit() or not end_str.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")

    # Проверка на длину (не более 16 цифр)
    if len(start_str) > 16 or len(end_str) > 16:
        raise ValueError("Номер карты не должен превышать 16 цифр.")

    # Преобразуем в int
    start_int = int(start_str)
    end_int = int(end_str)

    # Проверка на неправильный диапазон
    if start_int > end_int:
        raise ValueError("Начальное значение не может быть больше конечного.")

    # Генерация номера
    for number in range(start_int, end_int + 1):
        card_str = f"{number:016d}"
        yield f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"


# if __name__ == "__main__":
#     for card_number in card_number_generator(5, 4):
#         print(card_number)
