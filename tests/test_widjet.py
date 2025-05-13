import pytest

from scr.widjet import get_date, mask_account_card

# =========================================
# ====== Тесты для mask_account_card ======
# =========================================


# Тест с фиксутрой для валидного номера карт.
def test_mask_card_valid(number_card_indication):
    assert mask_account_card(number_card_indication) == "Maestro 1596 83** **** 5199"
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


# Тест с фиксутрой для валидного номера счета.
def test_mask_account_valid(number_account_indication):
    assert mask_account_card(number_account_indication) == "Счет **9589"
    assert mask_account_card("Счет 35383033474447895560") == "Счет **5560"


# Параметризованный тест mask_account_card на валидные номера.
@pytest.mark.parametrize(
    "number, mask",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874303", "Счет **4303"),
    ],
)
def test_mask_account_card(number, mask):
    assert mask_account_card(number) == mask


# Параметризованный тест mask_account_card на невалидные номера.
@pytest.mark.parametrize(
    "invalid_data",
    [
        "Visa Classic 6831982476737",  # Номер не равен 16 или 20
        "Счет 35383О33474447895560",  # В номере содержаться не только цифры
        "",  # Отсутствие данных
    ],
)
def test_mask_account_card_invalid(invalid_data):
    with pytest.raises(ValueError):
        mask_account_card(invalid_data)


# =========================================
# ====== Тесты для mask_account_card ======
# =========================================


def test_get_date(iso_date):
    assert get_date(iso_date) == "11.03.2024"
    assert get_date("2023-03-15T14:30:59.123456") == "15.03.2023"


@pytest.mark.parametrize(
    "invalid_date",
    [
        "11.05.2025",  # Неверный формат
        "2025/05/11",
        "Одиннадцатое марта две тысячи двадцать пятого года",  # Написано словами
        "2025-13-01T00:00:00",  # Неверный месяц
        "",  # Отсутствие даты
        "2025-04-31T14:30:59.123456",  # Несуществующая дата
    ],
)
def test_get_date_invalid(invalid_date):
    with pytest.raises(ValueError):
        get_date(invalid_date)
