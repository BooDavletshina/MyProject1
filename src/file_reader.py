import csv

import pandas as pd


def read_transactions_csv(path):
    """Функция для считывания финансовых операций из CSV-файла"""
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        transaction_list = []
        for row in reader:
            transaction_list.append(row)
        return transaction_list


def read_transactions_excel(path):
    """Функция для считывания финансовых операций из Excel-файла"""
    excel_data = pd.read_excel(path)
    dict_data = excel_data.to_dict(orient='records')
    return dict_data


if __name__ == "__main__":
    print(read_transactions_csv('C:\\Users\\Boo_D\\PycharmProjects\\pythonProject2\\data\\transactions.csv'))
    print(read_transactions_excel('C:\\Users\\Boo_D\\PycharmProjects\\pythonProject2\\data\\transactions_excel.xlsx'))
