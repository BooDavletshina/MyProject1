import json
from src.external_api import get_convert_sum


def get_dict_data_transactions(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as data_transactions:
            transactions = json.load(data_transactions)
            return transactions
    except FileNotFoundError:
        return []


def get_transaction_sum(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
     в рублях"""
    if transaction["code"] != "RUB":
        convert_sum = get_convert_sum(transaction)
        return float(convert_sum)
    else:
        return float(transaction["amount"])