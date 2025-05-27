from datetime import datetime

from scr.decorators import log
from scr.masks import get_mask_account, get_mask_card_number


# @log(filename="mylog.txt")
def mask_account_card(number_card_or_account: str) -> str:
    """
    Принимает строку с номером карты или счета, определяет номер это или счет, накладывает нужную маску,
    возвращает строку с наложенной маской.

    :param number_card_or_account: Номер карты или счета.
    :return: Возвращает строку с наложенной маской на номер карты или счета.
    """

    # Извлекаем номер.
    number = " ".join(number_card_or_account.split()[-1:])

    # Накладывает маску на номер карты и выводит строку.
    if len(number) == 16:
        mask_card = get_mask_card_number(number)
        name_card = " ".join(number_card_or_account.split()[:-1])
        return f"{name_card} {mask_card}"

    # Накладывает маску на номер счет и выводит строку.
    elif len(number) == 20:
        mask_account = get_mask_account(number)
        return f"Счет {mask_account}"

    # Проверка на корректность данных.
    else:
        raise ValueError("Не удалось определить формат(карта или счет) или недопустимая длина")


# @log(filename="mylog.txt")
def get_date(date_iso: str) -> str:
    """
    Принимает на вход строку с датой в формате "ГГГГ-ММ-ДДTЧЧ:ММ:СС.ffffff" (ISO формат).
    Где:
      - ГГГГ — год
      - ММ — месяц
      - ДД — день
      - T — указание начала времени, просто маркер-разделитель.
      - ЧЧ — часы
      - ММ — минуты
      - СС — секунды
      - ffffff — микросекунды
    Возвращает строку с датой в формате "ДД.ММ.ГГГГ".

    :param date_iso: Строка с датой в формате "ГГГГ-ММ-ДДTЧЧ:ММ:СС.ffffff".
    :return: Строка с датой в формате "ДД.ММ.ГГГГ".
    """

    date = datetime.fromisoformat(date_iso)
    return date.strftime("%d.%m.%Y")


# if __name__ == "__main__":
#     print(mask_account_card("Maestro 1596837868701959"))
#     print(mask_account_card("Maestro 1596837868701959"))
#     print(get_date("2023-03-15T14:30:59.123456"))
#     print(get_date("11.05.2025"))
