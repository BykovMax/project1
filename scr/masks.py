from typing import Union


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
        raise ValueError("Номер карты должен содержать 16 цифр.")

    # Проверка, что только цифры.
    if not str_card.isdigit():
        raise ValueError("Номер карты должен содержать только цифры.")

    # формирование маски карты.
    mask_card = f"{str_card[:4]} {str_card[4:6]}** **** {str_card[-4:]}"
    return mask_card


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
        raise ValueError("Номер счета должен содержать 20 цифр.")

    # Проверка, что только цифры.
    if not str_account.isdigit():
        raise ValueError("Номер счета должен содержать только цифры.")

    # формирование маски счета.
    mask_account = f"**{str_account[-4:]}"
    return mask_account
