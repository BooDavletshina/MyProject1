from masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card: str) -> str:
    """Функция, которая принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    new_account_card = ""
    number_card = ""

    for symbol in account_card:
        if symbol.isalpha() or symbol.isspace():
            new_account_card += symbol
        else:
            number_card += symbol

    if len(number_card) == 16:
        modified_number_card = get_mask_card_number(int(number_card))
        new_account_card += modified_number_card
    else:
        modified_number_card = get_mask_account(int(number_card))
        new_account_card += modified_number_card

    return new_account_card


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку
    с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    new_date = date[0:10]
    return f"{new_date[-2:]}.{new_date[5:7]}.{new_date[0:4]}"
