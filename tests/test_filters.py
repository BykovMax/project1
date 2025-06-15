import pytest
from scr.filters import process_bank_search

# =======================================
# ====== Тесты process_bank_search ======
# ======================================


@pytest.mark.parametrize("search,expected_count", [
    ("перевод", 5),
    ("организац", 2),       # ищем по корню
    ("со счета", 2),
    ("пополнение", 0),
])
def test_process_bank_search(transactions, search, expected_count):
    result = process_bank_search(transactions, search)
    assert isinstance(result, list)
    assert len(result) == expected_count

