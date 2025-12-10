def filter_by_currency(transactions: list[dict], currency: str):
    """Функция-генератор, которая поочередно выдает транзакции, где валюта операции соответствует заданной"""
    filter_transactions = filter(lambda x: x["currency_code"] == currency, transactions)

    for transact in filter_transactions:
        yield transact


def transaction_descriptions(transactions: list[dict]):
    """Функция-генератор, которая принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    for transact in transactions:
        yield transact.get("description")


def card_number_generator(start: int, end: int):
    """Функция-генератор, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты."""
    for num in range(start, end):
        number_card = str(num).zfill(16)
        yield f'{number_card[0:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}'
        num += 1
