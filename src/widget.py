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
