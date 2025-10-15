from unittest.mock import mock_open, patch

from src.utils import get_dict_data_transactions, get_transaction_sum


@patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"}]')
def test_get_dict_data_transactions(mock_file):
    """Тест на корректное открытие и чтение JSON-файла"""
    result = get_dict_data_transactions('fake_path.json')
    assert result == [{"key": "value"}]
    mock_file.assert_called_once_with('fake_path.json', encoding='utf-8')


def test_get_dict_data_transactions_file_not_found():
    """Тестирование функции при отсутствии JSON-файла"""
    result = get_dict_data_transactions('non_existent_file.json')
    assert result == []

@patch('builtins.open', new_callable=mock_open, read_data='[{"key": "value"]')
def test_get_dict_data_transactions_file_decode_error(mock_file):
    """Тестирование функции при ошибке чтения JSON-файла"""
    result = get_dict_data_transactions('invalid_file.json')
    assert result == []
    mock_file.assert_called_once_with('invalid_file.json', encoding='utf-8')


def test_get_transaction_sum(get_transactions_rub):
    """Тест на корректное выведение суммы транзакции"""
    assert get_transaction_sum(get_transactions_rub) == 62621.51
