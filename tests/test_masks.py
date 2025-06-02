import pytest

from scr.masks import get_mask_account, get_mask_card_number

# ============================================
# ====== Тесты для get_mask_card_number ======
# ============================================


# Тест с фиксутрой для валидного номера карт.
def test_get_mask_card_number(number_card):
    assert get_mask_card_number(number_card) == "7000 79** **** 6361"
    assert get_mask_card_number(5999414228426353) == "5999 41** **** 6353"
    assert get_mask_card_number("8990922113665229") == "8990 92** **** 5229"


# Параметризованный тест на невалидные номера карт.
@pytest.mark.parametrize(
    "invalid_card",
    [
        "700079228960636",  # длина меньше 16.
        "700079228960636132",  # длина больше 16.
        "7OO079S28960636I",  # содержит не только цифры.
        "",  # Отсутствие номера
    ],
)
def test_invalid_number_card(invalid_card):
    with pytest.raises(ValueError):
        get_mask_card_number(invalid_card)


# ========================================
# ====== Тесты для get_mask_account ======
# ========================================


# Тест с фикстурой для валидного номер счета.
def test_get_mask_account(number_account):
    assert get_mask_account(number_account) == "**4305"
    assert get_mask_account(64686473678894779589) == "**9589"
    assert get_mask_account("35383033474447895560") == "**5560"


# Параметризованный тест на невалидные номера счетов.
@pytest.mark.parametrize(
    "invalid_account",
    [
        "7365410843013587430",  # длина меньше 20.
        "736541084301358743052",  # длина больше 20.
        "7365410843O1358743O5",  # содержит не только цифры.
        "",  # Отсутствие номера
    ],
)
def test_invalid_number_account(invalid_account):
    with pytest.raises(ValueError):
        get_mask_account(invalid_account)
