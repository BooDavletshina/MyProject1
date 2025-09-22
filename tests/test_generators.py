from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(list_transactions: list) -> None:
    """Тест, проверяющий, что функция корректно фильтрует транзакции по заданной валюте"""
    generator = filter_by_currency(list_transactions, "USD")
    assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(generator) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }


def test_filter_by_currency_no_transactions(list_transactions: list) -> None:
    """Тест, проверяющий, что функция вызывает исключение при отсутствии транзакций с заданным значением валюты"""
    generator = filter_by_currency(list_transactions, "EUR")
    try:
        next(generator)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


def test_transaction_descriptions(list_transactions: list) -> None:
    """Тест, проверяющий, что функция возвращает корректные описания для каждой транзакции."""
    generator = transaction_descriptions(list_transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"


def test_transaction_descriptions_no_transactions() -> None:
    """Тест, проверяющий, что функция вызывает исключение при отсутствии списка транзакций"""
    generator = transaction_descriptions([])
    try:
        next(generator)
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True


def test_card_number_generator() -> None:
    """Тест, который проверяет, что генератор выдает правильные номера карт в заданном диапазоне."""
    generator = card_number_generator(1, 5)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"


def test_card_number_generator_() -> None:
    """Тест, проверяющий, что функция вызывает исключение при достижении конца диапазона"""
    generator = card_number_generator(1, 2)
    try:
        assert next(generator) == "0000 0000 0000 0001"
        assert next(generator) == "0000 0000 0000 0002"
        assert False, "Должно было быть выброшено исключение StopIteration"
    except StopIteration:
        assert True
