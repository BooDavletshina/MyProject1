def filter_by_state(list_state: list, state: str = 'EXECUTED') -> list:
    """Функция, которая принимает список словарей и опционально значение для ключа state. Функция возвращает новый
    список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    filter_list = []

    for dictionary in list_state:
        for k,v in dictionary.items():
            if v == state:
                filter_list.append(dictionary)

    return filter_list


def sort_by_date(list_state: list, reverse: bool = True ) -> list:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание). Функция возвращает новый список, отсортированный по дате (date)."""
    sorted_list = sorted(list_state, key = lambda element_by_list: element_by_list['date'], reverse = reverse)

    return sorted_list
