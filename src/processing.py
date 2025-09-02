def filter_by_state(list_state: list, state: str = 'EXECUTED') -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state. Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    filter_list = []
    for dictionary in list_state:
        for k,v in dictionary.items():
            if v == state:
                filter_list.append(dictionary)
    return filter_list
