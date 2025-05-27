import pytest
from scr.processing import filter_by_state, sort_by_date

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


# Тест сортировка по убыванию (по умолчанию)
def test_sort_by_date_decreasing(mixed_state_data):
    assert sort_by_date(mixed_state_data)


# Тест сортировка по возрастанию
def test_sort_by_date_ascending(mixed_state_data):
    assert sort_by_date(mixed_state_data, reverse=False)


# Тест на одинаковые даты
def test_sort_by_date_same_dates():
    same_date_data = [
        {"id": 1, "date": "2025-05-13T17:16:00.000000"},
        {"id": 2, "date": "2020-05-13T17:16:00.000000"},
        {"id": 3, "date": "2020-05-13T17:16:00.000000"},
    ]
    assert sort_by_date(same_date_data) == same_date_data


# Тест с неверными форматами дат
@pytest.mark.parametrize(
    "invalid_date",
    [
        [{"id": 1, "date": "2025-13-13T17:16:00.000000"}],  # Неверная дата
        [{"id": 2, "date": "13.05.25"}],  # Неверный формат
        [{"id": 3, "date": "2025-05-13T18:04:00+03:00"}],
        [{"id": 4, "date": "May 13 2025"}],
    ],
)
def test_sort_by_date_invalid_format(invalid_date):
    with pytest.raises(ValueError):
        sort_by_date(invalid_date)
