def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера."""
    card_number_str = str(card_number)
    mask_card_number = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return mask_card_number


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера"""
    account_number_str = str(account_number)
    mask_account_number = f"**{account_number_str[-4:]}"
    return mask_account_number
