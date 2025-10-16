import json
import logging

from src.external_api import get_convert_sum

logging.basicConfig(
    level=logging.DEBUG,
    filemode='w',
    filename='C:\\Users\\Boo_D\\PycharmProjects\\pythonProject2\\logs\\utils.log',
    format='%(asctime)s-%(filename)s-%(levelname)s: %(message)s',
    datefmt='%d-%m-%d %H:%M:%S',
    encoding='UTF-8'
)

utils_logger = logging.getLogger(__name__)


def get_dict_data_transactions(path: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей
     с данными о финансовых транзакциях."""
    try:
        with open(path, encoding='utf-8') as data_transactions:
            utils_logger.info('Открыт JSON-файл с данными о финансовых транзакциях')
            transactions = json.load(data_transactions)
            utils_logger.info('Создан список словарей c данными о финансовых транзакциях')
            return transactions
    except FileNotFoundError as ex:
        utils_logger.error(f'Ошибка: {ex}')
        return []
    except json.JSONDecodeError as ex:
        utils_logger.error(f'Ошибка: {ex}')
        return []


def get_transaction_sum(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount)
     в рублях"""
    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        utils_logger.info('Проверка наименования валюты суммы транзакции')
        convert_sum = get_convert_sum(transaction)
        utils_logger.info('Успешная конвертация валюты')
        return float(convert_sum)
    else:
        return float(transaction["operationAmount"]["amount"])


if __name__ == '__main__':
    print(get_dict_data_transactions('C:\\Users\\Boo_D\\PycharmProjects\\pythonProject2\\data\\operations.json'))
    print(get_dict_data_transactions('\\data\\operations.json'))
    print(get_transaction_sum(
        {
            "id": 608117766,
            "state": "CANCELED",
            "date": "2018-10-08T09:05:05.282282",
            "operationAmount": {"amount": "77302.31", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на счет",
            "from": "Visa Gold 6527183396477720",
            "to": "Счет 38573816654581789611",
        }
    ))