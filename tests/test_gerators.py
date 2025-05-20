import pytest

from scr.generators import card_number_generator, filter_by_currency, transaction_descriptions

# ==========================================
# ====== Тесты для filter_by_currency ======
# ==========================================


@pytest.mark.parametrize(
    "currency_code, expected_id",
    [
        (
            None,  # По умолчанию RUB
            [873106923, 594226727],
        ),
        (
            "RUB",  # Фильтрация по RUB
            [873106923, 594226727],
        ),
        (
            "USD",  # Фильтрация по USD
            [939719570, 142264268, 895315941],
        ),
        (
            "EUR",  # Нет такого кода валюты
            [],
        ),
    ],
)
def test_filter_by_currency_parametrize(transactions, currency_code, expected_id):
    result = list(filter_by_currency(transactions, currency_code))
    result_id = [item["id"] for item in result]
    assert result_id == expected_id


# ================================================
# ====== Тесты для transaction_descriptions ======
# ================================================


@pytest.mark.parametrize(
    "expected_description",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ]
    ],
)
def test_transaction_descriptions(transactions, expected_description):
    result = list(transaction_descriptions(transactions))
    assert result == expected_description


def test_transaction_descriptions_no_key():
    transaction_without_description = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            # "description" отсутствует
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    with pytest.raises(KeyError):
        list(transaction_descriptions(transaction_without_description))


# =============================================
# ====== Тесты для card_number_generator ======
# =============================================


def test_card_number_generator_range():
    result = list(card_number_generator(1, 5))
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_card_number_generator_same_value(number_card):
    result = list(card_number_generator(number_card, int(number_card)))
    expected = ["7000 7922 8960 6361"]
    assert result == expected


def test_card_number_generator_incorrect_range():
    with pytest.raises(ValueError):
        list(card_number_generator(4, 1))  # Неверный диапазон


def test_card_number_generator_out_of_bounds_start():
    with pytest.raises(ValueError):
        list(card_number_generator(-1, 10))  # Отрицательное число


def test_card_number_generator_invalid(number_card):
    with pytest.raises(ValueError):
        list(card_number_generator(number_card, "70007922896063611"))  # Длина больше 16
