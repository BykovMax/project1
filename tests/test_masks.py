import pytest

from scr.masks import get_mask_card_number, get_mask_account

# Тесты для get_mask_card_number.
# Фикстура для валидного номера карты.
@pytest.fixture
def valid_number_card():
    return "7000792289606361"

# Тест с фиксутрой для валидного номера карт.
def test_get_mask_card_number(valid_number_card):
    assert get_mask_card_number(valid_number_card) == "7000 79** **** 6361"

# Параметризованный тест на невалидные номера карт.
@pytest.mark.parametrize("invalid_card", [
    "700079228960636", # длина меньше 16.
    "700079228960636132", # длина больше 16.
    "7OO079S28960636I" # содержит не только цифры.
])
def test_invalid_number_card(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)


# Тесты для get_mask_account.
# Фикстура для валидного номера счета .
@pytest.fixture
def valid_number_account():
    return "73654108430135874305"

# Тест с фикстурой для валидного номер счета.
def test_get_mask_account(valid_number_account):
    assert get_mask_account(valid_number_account) == "**4305"

# Параметризованный тест на невалидные номера счетов.
@pytest.mark.parametrize("invalid_account", [
    "7365410843013587430", # длина меньше 20.
    "736541084301358743052", # длина больше 20.
    "7365410843O1358743O5" # содержит не только цифры.
])
def test_invalid_number_account(invalid_account):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)
