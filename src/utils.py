import json


def get_dict_data_transactions(path):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as data_transactions:
            transactions = json.load(data_transactions)
            return transactions
    except FileNotFoundError:
        return []
