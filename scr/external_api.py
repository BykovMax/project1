import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли (если нужно).

    :param transaction: Словарь с ключами "amount" и "currency"
    :return: Сумма в рублях
    """
    amount = float(transaction.get("amount", 0))
    currency = transaction.get("currency")

    if currency == "RUB":
        return amount

    if currency not in {"USD", "EUR"}:
        raise ValueError(f"Неподдерживаемая валюта для конвертирования {currency}")

    headers = {"apikey": API_KEY}
    params = {"base": currency, "symbols": "RUB"}

    response = requests.get(API_URL, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    rate = data["rates"]["RUB"]
    return round(amount * rate, 2)


# if __name__ == "__main__":
#
#     transaction = {
#         "amount": 85,
#         "currency": "EUR"
#     }
#
#     result = convert_to_rub(transaction)
#     print(f"Конвертировано: {result} RUB")
