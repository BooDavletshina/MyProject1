def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера."""
    card_number_str = str(card_number)

    if len(card_number_str) == 16:
        mask_card_number = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        return mask_card_number

    return "Неверно введен номер карты"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера"""
    account_number_str = str(account_number)

    if len(account_number_str) == 20:
        mask_account_number = f"**{account_number_str[-4:]}"
        return mask_account_number

    return "Неверно введен номер счета"
