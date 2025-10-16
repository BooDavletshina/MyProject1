import logging

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='C:\\Users\\Boo_D\\PycharmProjects\\pythonProject2\\logs\\masks.log',
    format='%(asctime)s-%(filename)s-%(levelname)s: %(message)s',
    datefmt='%d-%m-%d %H:%M:%S',
    encoding='utf-8'
)

masks_logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X — это цифра номера."""
    card_number_str = str(card_number)

    if len(card_number_str) == 16:
        masks_logger.info("Успешная проверка длины номера карты")
        mask_card_number = f"{card_number_str[0:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        masks_logger.info("Маскировка номера карты")
        return mask_card_number

    masks_logger.warning("Неверно введен номер карты")
    return "Неверно введен номер карты"


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску. Номер счета замаскирован и отображается в формате
    **XXXX, где X — это цифра номера"""
    account_number_str = str(account_number)

    if len(account_number_str) == 20:
        masks_logger.info("Успешная проверка длины номера счета")
        mask_account_number = f"**{account_number_str[-4:]}"
        masks_logger.info("Маскировка номера счета")
        return mask_account_number

    masks_logger.warning("Неверно введен номер счета")
    return "Неверно введен номер счета"


if __name__ == '__main__':
    print(get_mask_card_number(7000792289606361))
    print(get_mask_card_number(73654108430135874305))
    print(get_mask_account(73654108430135874305))
    print(get_mask_account(7000792289606361))