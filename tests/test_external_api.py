from unittest.mock import patch

import pytest

from scr.external_api import convert_to_rub

# ==================================
# ====== Тесты convert_to_rub ======
# ==================================


@pytest.mark.parametrize(
    "transaction, mock_response, expected, should_raise",
    [
        ({"amount": 1000, "currency": "RUB"}, None, 1000, False),
        ({"amount": 66.6, "currency": "USD"}, {"rates": {"RUB": 79.13}}, 5270.06, False),
        ({"amount": 77.7, "currency": "EUR"}, {"rates": {"RUB": 90.38}}, 7022.53, False),
        ({"amount": 100, "currency": "CNY"}, None, None, True),
    ],
)
@patch("scr.external_api.requests.get")
def test_convert_to_rub(mock_get, transaction, mock_response, expected, should_raise):
    if mock_response:
        mock_get.return_value.status_cod = 200
        mock_get.return_value.json.return_value = mock_response

    if should_raise:
        with pytest.raises(ValueError):
            convert_to_rub(transaction)
    else:
        result = convert_to_rub(transaction)
        assert result == expected
