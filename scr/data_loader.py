from typing import Dict, List

import pandas as pd


def read_transactions_csv(path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из CSV-файла и возвращает список словарей.

    :param path: Путь к CSV-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8")
        df.columns = df.columns.str.strip()
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_transactions_excel(path: str) -> List[Dict]:
    """
    Считывает финансовые транзакции из Excel (XLSX) и возвращает список словарей.

    :param path: Путь к XLSX-файлу.
    :return: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []


# if __name__ == "__main__":
#     import os
#     from pprint import pprint
#
#     current_dir = os.path.dirname(os.path.dirname(__file__))
#     csv_path = os.path.join(current_dir, "data", "transactions.csv")
#     excel_path = os.path.join(current_dir, "data", "transactions_excel.xlsx")
#
#     print("CSV:")
#     pprint(read_transactions_csv(csv_path))
#     print("Excel:")
#     pprint(read_transactions_excel(excel_path))
