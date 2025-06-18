import pytest

from scr.processing import filter_by_currency, filter_by_state, sort_by_date

# ===================================
# ====== Тесты filter_by_state ======
# ===================================


# Тест filter_by_state с параметризацией
@pytest.mark.parametrize(
    "state, expected",
    [
        (
                None,  # По умолчанию — "EXECUTED"
                [
                    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                ],
        ),
        (
                "CANCELED",
                [
                    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                ],
        ),
        ("WAITING", []),
    ],
)
def test_filter_by_state_parametrize(mixed_state_data, state, expected):
    assert filter_by_state(mixed_state_data, state) == expected


# ================================
# ====== Тесты sort_by_date ======
# ================================


@pytest.mark.parametrize(
    "input_data, expected_order",
    [
        (
                # Разные форматы дат
                [
                    {"id": 1, "date": "2020-06-07T11:11:36Z"},  # без миллисекунд + Z
                    {"id": 2, "date": "2020-06-07T11:11:36.123456"},  # с миллисекундами
                    {"id": 3, "date": "2020-06-07T11:11:36.123456+00:00"},  # с таймзоной
                    {"id": 4, "date": "2020-06-06T11:11:36"},  # просто без микросекунд
                    {"id": 5, "date": "2020-06-08"},  # только дата
                ],
                [4, 1, 2, 3, 5],  # отсортировано по возрастанию
        )
    ],
)
def test_sort_by_date_various_formats(input_data, expected_order):
    sorted_data = sort_by_date(input_data, reverse=False)
    actual_order = [item["id"] for item in sorted_data]
    assert actual_order == expected_order


# ======================================
# ====== Тесты filter_by_currency ======
# ======================================


@pytest.mark.parametrize(
    "currency, expected_count, expected_codes",
    [
        ("RUB", 2, {"RUB"}),
        ("USD", 3, {"USD"}),
        ("EUR", 0, set()),
    ],
)
def test_filter_by_currency_param(transactions, currency, expected_count, expected_codes):
    result = filter_by_currency(transactions, currency)
    assert isinstance(result, list)
    assert len(result) == expected_count
    assert {tx.get("operationAmount", {}).get("currency", {}).get("code") for tx in result} <= expected_codes
