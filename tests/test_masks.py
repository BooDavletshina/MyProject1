import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("card_number, expected_result", [
                        (1596837868705199, "1596 83** **** 5199"),
                        (7158300734726758, "7158 30** **** 6758"),
                        (6831982476737658, "6831 98** **** 7658")])
def test_get_mask_card_number(card_number, expected_result):
    """Функция, которая тестирует правильность маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize("card_number, expected_result", [
                        (15968378, "Неверно введен номер карты"),
                        (71534726758, "Неверно введен номер карты"),
                        (683198247658, "Неверно введен номер карты")])
def test_get_mask_card_number_invalid_length(card_number, expected_result):
    """Функция, которая тестирует правильность ввода номера карты"""
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize("account_number, expected_result", [
                        (64686473678894779589, "**9589"),
                        (35383033474447895560, "**5560"),
                        (73654108430135874305, "**4305")])
def test_get_mask_account(account_number, expected_result):
    """Функция, которая тестирует правильность маскировки номера счета"""
    assert get_mask_account(account_number) == expected_result


@pytest.mark.parametrize("account_number, expected_result", [
                        (73654108430135874305642, "Неверно введен номер счета"),
                        (7365410843013, "Неверно введен номер счета"),
                        (736541084301358, "Неверно введен номер счета")])
def test_get_mask_account_invalid_length(account_number, expected_result):
    """Функция, которая тестирует правильность ввода номера счета"""
    assert get_mask_account(account_number) == expected_result
