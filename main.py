from src.file_reader import read_transactions_csv, read_transactions_excel
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import get_dict_data_transactions
from src.widget import get_date, mask_account_card

# Функции для приведения файлов к единому формату

def process_csv_or_excel_data(data_transactions):
    """Функция для обработки данных из CSV-файлов/Excel-файлов"""
    transactions = [
        {
            "date": transaction.get("date"),
            "description": transaction.get("description"),
            "state": transaction.get("state"),
            "amount": transaction.get("amount", 0),
            "currency_code": transaction.get("currency_code"),
            "currency_name": transaction.get("currency_name"),
            "from": transaction.get("from"),
            "to": transaction.get("to")
        }
        for transaction in data_transactions
    ]

    return transactions


def process_json_data(data_transactions):
    """Функция для обработки данных из JSON-файла"""
    transactions = [
        {
            "date": transaction.get("date"),
            "description": transaction.get("description"),
            "amount": transaction.get("operationAmount", {}).get("amount"),
            "state": transaction.get("state"),
            "currency_code": transaction.get("operationAmount", {}).get("currency", {}).get("code"),
            "currency_name": transaction.get("operationAmount", {}).get("currency", {}).get("name"),
            "from": transaction.get("from"),
            "to": transaction.get("to")
        }
        for transaction in data_transactions
    ]

    return transactions


def filter_transactions_by_status(data_transactions):
    """Функция фильтрации банковских транзакций по статусу"""
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.\n"
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_input_status = input().upper()

        if user_input_status in ["EXECUTED", "CANCELED", "PENDING"]:
            return filter_by_state(data_transactions, user_input_status)
        else:
            print(f"Статус операции {user_input_status} недоступен.")


def filter_transactions_by_currency(data_transactions):
    """Функция, которая выводит (фильтрует) только рублевые транзакции"""
    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_qw_tree = input().lower()

    if user_input_qw_tree == "да":
        filter_transactions = []
        for item in filter_by_currency(data_transactions, "RUB"):
            filter_transactions.append(item)
        return filter_transactions
    else:
        return data_transactions


def filter_transactions_by_word(data_transactions):
    """Функция, которая фильтрует список транзакций по определенному слову в описании"""
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    user_input_qw_four = input().lower()

    if user_input_qw_four == "да":
        user_input = input("Введите слово, по которому требуется отфильтровать список транзакций")
        filter_by_word = process_bank_search(data_transactions, user_input)
        return filter_by_word
    else:
        return data_transactions


def get_final_transactions(data_transactions):
    """Функция, которая возвращает итоговый список транзакций"""
    print("Распечатываю итоговый список транзакций...")

    print(f"Всего банковских операций в выборке: {len(data_transactions)}")

    if len(data_transactions) != 0:
        for transact in data_transactions:
            date = get_date(transact["date"])
            print(f"{date} {transact["description"]}")

            if "from" in transact and "to" in transact and "from" != "" in transact:
                from_ = mask_account_card(transact.get("from"))
                to = mask_account_card(transact.get("to"))
                print(f"{from_} -> {to}")
                print(f"Сумма: {transact["amount"]} {transact["currency_name"]}")
            else:
                to = mask_account_card(transact.get("to"))
                print(f"{to}")
                print(f"Сумма: {transact["amount"]} {transact["currency_name"]}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


def get_additional_questions(data_transactions):
    """Функция, которая выводит дополнительные вопросы для фильтрации банковских транзакций"""
    print("Отсортировать операции по дате? Да/Нет")
    user_input_qw_one = input().lower()

    if user_input_qw_one == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input_qw_two = input().lower()

        if user_input_qw_two == "по убыванию":
            data_transactions_sort_by_date = sort_by_date(data_transactions)
            transactions_by_currency = filter_transactions_by_currency(data_transactions_sort_by_date)
            transactions_by_word = filter_transactions_by_word(transactions_by_currency)
            get_final_transactions(transactions_by_word)

        elif user_input_qw_two == "по возрастанию":
            data_transactions_sort_by_date = sort_by_date(data_transactions, False)
            transactions_by_currency = filter_transactions_by_currency(data_transactions_sort_by_date)
            transactions_by_word = filter_transactions_by_word(transactions_by_currency)
            get_final_transactions(transactions_by_word)

    else:
        transactions_by_currency = filter_transactions_by_currency(data_transactions)
        transactions_by_word = filter_transactions_by_word(transactions_by_currency)
        get_final_transactions(transactions_by_word)


def main():
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """)

    user_input = int(input())

    if user_input == 1:
        print("Для обработки выбран JSON-файл.")

        user_input_path_json = input("Выберите файл:")
        data_transactions = process_json_data(get_dict_data_transactions(user_input_path_json))
        filter_data_transactions = filter_transactions_by_status(data_transactions)
        get_additional_questions(filter_data_transactions)

    elif user_input == 2:
        print("Для обработки выбран CSV-файл.")

        user_input_path_csv = input("Выберите файл:")
        data_transactions = process_csv_or_excel_data(read_transactions_csv(user_input_path_csv))
        filter_data_transactions = filter_transactions_by_status(data_transactions)
        get_additional_questions(filter_data_transactions)

    elif user_input == 3:
        print("Для обработки выбран XLSX-файл.")

        user_input_path_xlsx = input("Выберите файл:")
        data_transactions = process_csv_or_excel_data(read_transactions_excel(user_input_path_xlsx))
        filter_data_transactions = filter_transactions_by_status(data_transactions)
        get_additional_questions(filter_data_transactions)


if __name__ == "__main__":
    print(main())
