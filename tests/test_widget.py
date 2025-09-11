import pytest
from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("account_card, expected_result", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758","MasterCard 7158 30** **** 6758" ),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
])
def test_mask_account_card(account_card, expected_result):
    """Тест для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от типа
     входных данных (карта или счет)."""
    assert mask_account_card(account_card) == expected_result


def test_mask_account_card_incorrect_input():
    """Тест на вызов исключения при некорректном вводе (пустая строка)"""
    with pytest.raises(ValueError):
        mask_account_card("")

def test_mask_account_card_incorrect_type_int():
    """Тест на вызов исключения при вводе аргумента типа int"""
    with pytest.raises(ValueError):
        mask_account_card(123456)

def test_mask_account_card_incorrect_type_float():
    """Тест на вызов исключения при вводе аргумента типа float"""
    with pytest.raises(ValueError):
        mask_account_card(1234.56)


@pytest.mark.parametrize("date, expected_result", [
                        ("2024-03-11T02:26:18.671407", "11.03.2024"),
                        ("2024-03-11", "11.03.2024"),
                        ("2024.03.11", "11.03.2024")
])
def test_get_date(date, expected_result):
    """Функция, которая тестирует правильность преобразования даты."""
    assert get_date(date) == expected_result

def test_get_date_empty():
    """Функция, которая тестирует код при вводе пустой строки"""
    assert get_date("") == "Некорректный ввод данных"
