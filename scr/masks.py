import logging
import os.path
from typing import Union

# from scr.decorators import log


# ====== Настройка логгера модуля masks ======
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)

# Путь к папке logs (в корне проекта)
log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)
log_path = os.path.join(log_dir, "masks.log")

# Handler + Formatter
file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
formatter = logging.Formatter(
    "%(asctime)s |" " модуль %(filename)s |" " функция %(funcName)s |" " уровень %(levelname)s |" " %(message)s"
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# @log(filename="mylog.txt")
def get_mask_card_number(card_number: Union[int, str]) -> str:
    """
    Принимает номер карты из 16 цифр и возвращает в формате "XXXX XX** **** XXXX", где Х это цифра номера карты.

    :param card_number: Номер карты.
    :return: Возвращает маску номера карты.
    """
    # Преобразование в строку если номер карты запрашивается не через input.
    str_card = str(card_number)

    # Проверка длины номера карты.
    if len(str_card) != 16:
        logger.error(f"Ошибка: номер карты некорректной длины ({len(str_card)}): {card_number}")
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Проверка, что только цифры.
    if not str_card.isdigit():
        logger.error(f"Ошибка: номер содержит не только цифры: {card_number}")
        raise ValueError("Номер карты должен содержать только цифры.")

    # формирование маски карты.
    mask_card = f"{str_card[:4]} {str_card[4:6]}** **** {str_card[-4:]}"
    logger.debug(f"Сформирована маска карты: {mask_card}")
    return mask_card


# @log(filename="mylog.txt")
def get_mask_account(account_number: Union[int, str]) -> str:
    """
    Принимает номер счета и скрывает его отображая в формате **XXXX, где Х это цифра номера.

    :param account_number: Номер счета.
    :return: Возвращает маску номера счета.
    """
    # Преобразование в строку если номер счета запрашивается не через input.
    str_account = str(account_number)

    # Проверка длины номера счета.
    if len(str_account) != 20:
        logger.error(f"Ошибка: номер счета некорректной длины ({len(str_account)}): {str_account}")
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Проверка, что только цифры.
    if not str_account.isdigit():
        logger.error(f"Ошибка: номер счета содержит не только цифры: {str_account}")
        raise ValueError("Номер счета должен содержать только цифры.")

    # формирование маски счета.
    mask_account = f"**{str_account[-4:]}"
    logger.debug(f"Сформирована маска счета: {mask_account}")
    return mask_account


def mask_entity(entity: str) -> str:
    """
    Возвращает замаскированный номер карты или счёта, если это возможно.
    """
    if not isinstance(entity, str):
        return ""

    if "Счет" in entity:
        number = entity.split()[-1]
        try:
            return f"Счет {get_mask_account(number)}"
        except ValueError:
            return entity

    elif any(
        brand in entity for brand in ["Visa", "Mastercard", "Maestro", "Discover", "American", "Platinum", "Classic"]
    ):
        parts = entity.split()
        if len(parts) >= 2:
            brand, number = parts[0], parts[-1]
            try:
                return f"{brand} {get_mask_card_number(number)}"
            except ValueError:
                return entity

    return entity


# if __name__ == "__main__":
#     print(get_mask_card_number(5999414228426353))
#     print(get_mask_account("35383033474447895560"))
#
#     # Ошибки:
#     try:
#         get_mask_card_number("12345678abc12345")
#     except ValueError:
#         pass
#
#     try:
#         get_mask_account("1232342342432423432")
#     except ValueError:
#         pass
