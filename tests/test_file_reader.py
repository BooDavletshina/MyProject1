from unittest.mock import mock_open, patch

from src.file_reader import read_transactions_csv, read_transactions_excel


import pandas as pd

mock_csv_data = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
"""

@patch('builtins.open', new_callable=mock_open, read_data=mock_csv_data)
def test_read_transactions_csv(mock_file):
    """Тест на корректное открытие и чтение CSV-файла"""
    result = read_transactions_csv('fake_path.csv')
    assert result == [{'amount': '16210',
  'currency_code': 'PEN',
  'currency_name': 'Sol',
  'date': '2023-09-05T11:30:32Z',
  'description': 'Перевод организации',
  'from': 'Счет 58803664561298323391',
  'id': '650703',
  'state': 'EXECUTED',
  'to': 'Счет 39745660563456619397'}]
    mock_file.assert_called_once_with('fake_path.csv', encoding='utf-8')


def test_read_transactions_csv_not_found():
    """Тестирование функции при отсутствии CSV-файла"""
    result = read_transactions_csv('non_existent_file.csv')
    assert result == []


@patch('pandas.read_excel')
def test_read_transactions_excel(mock_read_excel):
    mock_data = pd.DataFrame([{'key': 'value'}])
    mock_read_excel.return_value = mock_data

    result = read_transactions_excel('fake_path.xlsx')
    assert result == [{'key': 'value'}]
    mock_read_excel.assert_called_once_with('fake_path.xlsx')


def test_read_transactions_excel_not_found():
    """Тестирование функции при отсутствии Excel-файла"""
    result = read_transactions_excel('non_existent_file.xlsx')
    assert result == []
