from scr.constants import CATEGORY_MAPPING
from scr.data_loader import read_transactions_csv, read_transactions_excel
from scr.filters import process_bank_operations, process_bank_search
from scr.masks import mask_entity
from scr.processing import filter_by_currency, filter_by_state, sort_by_date
from scr.utils import ask_yes_no, get_unique_descriptions, read_operations_json


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите источник данных:")
    print("1. JSON-файл")
    print("2. CSV-файл")
    print("3. XLSX-файл")

    source_map = {
        "1": ("data/operations.json", read_operations_json),
        "2": ("data/transactions.csv", read_transactions_csv),
        "3": ("data/transactions_excel.xlsx", read_transactions_excel),
    }

    while True:
        choice = input("Введите номер (1/2/3): ").strip()
        if choice in source_map:
            path, loader = source_map[choice]
            transactions = loader(path)
            if not transactions:
                print("Файл пустой или не найден. Завершаем программу.")
                return
            print(f"Для обработки выбран файл: {path}")
            break
        else:
            print("Неверный ввод. Повторите.")

    # ===== Фильтрация по статусу =====
    valid_states = {"executed", "canceled", "pending"}
    while True:
        state = input("Введите статус (EXECUTED, CANCELED, PENDING): ").strip().lower()
        if state in valid_states:
            filtered = filter_by_state(transactions, state.upper())
            print(f"Операции отфильтрованы по статусу: {state.upper()}")
            break
        else:
            print(f"Статус операции '{state}' недоступен.")

    # ===== Сортировка по дате =====
    if ask_yes_no("Отсортировать по дате? Да/Нет: "):
        while True:
            direction = input("По возрастанию или по убыванию?: ").strip().lower()
            if direction in ("по возрастанию", "возрастание"):
                reverse = False
                break
            elif direction in ("по убыванию", "убывание"):
                reverse = True
                break
            else:
                print('Некорректный ввод. Введите "по возрастанию" или "по убыванию".')

        filtered = sort_by_date(filtered, reverse)

    # ===== Фильтрация только по рублям =====
    if ask_yes_no("Выводить только рублевые транзакции? Да/Нет: "):
        filtered = filter_by_currency(filtered, "RUB")

    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # ===== Фильтрация по ключевому слову =====
    if ask_yes_no("Отфильтровать по слову в описании? Да/Нет: "):
        descriptions = get_unique_descriptions(filtered)
        print(f"\nВсего найдено описаний: {len(descriptions)}")

        if not descriptions:
            print("Нет доступных описаний для фильтрации.")
            return

        print("Возможные ключевые слова из поля 'description':")
        for desc in sorted(descriptions):
            print(f"- {desc}")

        while True:
            keyword = input("\nВведите ключевое слово для фильтрации по описанию: ").strip().capitalize()
            if keyword in descriptions:
                filtered = process_bank_search(filtered, keyword)
                break
            else:
                print(f'Категория "{keyword}" не найдена в списке. Попробуйте ещё раз.')

    # ===== Вывод результата =====
    print("\nРаспечатываю итоговый список транзакций...")
    if not filtered:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    print(f"\nВсего операций: {len(filtered)}\n")
    for item in filtered:
        date = item.get("date", "")[:10]
        desc = item.get("description", "")
        from_ = item.get("from", "")
        to_ = item.get("to", "")
        amount = item.get("operationAmount", {}).get("amount", item.get("amount", ""))
        currency = item.get("operationAmount", {}).get("currency", {}).get("name", item.get("currency_name", ""))

        print(f"{date} {desc}")
        if from_ and to_:
            print(f"{mask_entity(from_)} -> {mask_entity(to_)}")
        elif from_:
            print(f"{mask_entity(from_)}")
        elif to_:
            print(f"{mask_entity(to_)}")
        print(f"Сумма: {amount} {currency}\n")

    # ===== Подсчёт категорий =====
    print("Статистика по типам операций:")
    stats = process_bank_operations(filtered, CATEGORY_MAPPING)
    for category, count in stats.items():
        print(f"{category}: {count}")


if __name__ == "__main__":
    main()
