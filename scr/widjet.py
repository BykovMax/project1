from scr.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_card_or_account: str) -> str:
    """
    Принимает строку с номером карты или счета, определяет номер это или счет, накладывает нужную маску,
    возвращает строку с наложенной маской.

    :param number_card_or_account: Номер карты или счета.
    :return: Возвращает строку с наложенной маской на номер карты или счета.
    """

    number = " ".join(number_card_or_account.split()[-1:])

    if len(number) == 16:
        mask_card = get_mask_card_number(number)
        name_card = " ".join(number_card_or_account.split()[:-1])
        return f"{name_card} {mask_card}"

    elif len(number) == 20:
        mask_account = get_mask_account(number)
        return f"Счет {mask_account}"

    else:
        raise ValueError("Не удалось определить формат(карта или счет) или недопустимая длина")
