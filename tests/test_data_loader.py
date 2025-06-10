from unittest.mock import MagicMock, patch

from scr.data_loader import read_transactions_csv, read_transactions_excel

# =============================================
# ====== Тесты для read_transactions_csv ======
# =============================================


@patch("scr.data_loader.pd.read_csv")
def test_read_transactions_csv_success(mock_read_csv, transactions):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = transactions
    mock_read_csv.return_value = mock_df

    result = read_transactions_csv("fake_path.csv")
    assert result == transactions
    mock_read_csv.assert_called_once()


@patch("scr.data_loader.pd.read_csv", side_effect=Exception("Ошибка CSV"))
def test_read_transactions_csv_error(mock_read_csv):
    result = read_transactions_csv("wrong.csv")
    assert result == []


# ===============================================
# ====== Тесты для read_transactions_excel ======
# ===============================================


@patch("scr.data_loader.pd.read_excel")
def test_read_transactions_excel_success(mock_read_excel, transactions):
    mock_df = MagicMock()
    mock_df.to_dict.return_value = transactions
    mock_read_excel.return_value = mock_df

    result = read_transactions_excel("fake_path.xlsx")
    assert result == transactions
    mock_read_excel.assert_called_once()


@patch("scr.data_loader.pd.read_excel", side_effect=Exception("Ошибка Excel"))
def test_read_transactions_excel_error(mock_read_excel):
    result = read_transactions_excel("wrong.xlsx")
    assert result == []
