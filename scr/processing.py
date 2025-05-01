def filter_by_state(list_dict, state="EXECUTED"):
    """
    Фильтрует список словарей

    :param list_dict:
    :param state:
    :return:
    """
    new_list_dict = []
    for item in list_dict:
        if item.get("state") == state:
            new_list_dict.append(item)
    return new_list_dict
