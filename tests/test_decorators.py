import re

import pytest

from src.decorators import log


@log(filename=None)
def function(x, y):
    """Тестовая функция"""
    return x + y


def test_function_with_log_decorator():
    """Тестовая функция для проверки декоратора на вывод результата работы функции"""
    assert function(1, 2) == 3


def test_log_decorator_console_output(capsys):
    """Функция для тестирования вывода в консоль"""
    function(1, 2)
    captured = capsys.readouterr()
    assert re.search(r"Функция: function", captured.out)
    assert re.search(r"Результат: 3", captured.out)


@log(filename=None)
def example_function():
    """Тестовая функция"""
    raise ValueError()


def test_log_decorator_exception():
    """Функция для тестирования обработки исключения декоратором"""
    with pytest.raises(Exception):
        example_function()
