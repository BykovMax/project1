from typing import Dict, Iterator, List


def filter_by_currency(transaction: list[Dict], currency_code: str = "RUB") -> Iterator[Dict]:
    """
     Фильтрует транзакции по коду валюты. По умолчанию 'RUB'.

    :param transaction: Список словарей транзакций.
    :param currency_code: Код валюты, по которому фильтровать (например, 'USD').
    :return: Итератор Отфильтрованных транзакций.
    """
    if currency_code is None:
        currency_code = "RUB"

    return (
        x for x in transaction if x.get("operationAmount", {}).get("currency").get("code") == currency_code
    )


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

    :param transactions: Список словарей транзакций.
    :yield: Возвращает описание транзакции.
    """
    for transaction in transactions:
        yield transaction["description"]
