import pytest

from scr.generators import filter_by_currency

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
            "RUB", # Фильтрация по RUB
            [873106923, 594226727],
        ),
        (
            "USD", # Фильтрация по USD
            [939719570, 142264268, 895315941],
        ),
        (
            "EUR", # Нет такого кода валюты
            [],
        ),
    ],
)
def test_filter_by_currency_parametrize(transactions, currency_code, expected_id):
    result = list(filter_by_currency(transactions, currency_code))
    result_id = [item["id"] for item in result]
    assert result_id == expected_id


