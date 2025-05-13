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
