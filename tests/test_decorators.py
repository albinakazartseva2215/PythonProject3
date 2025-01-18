import pytest

from src.decorators import log, my_function


def test_log_text(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ("Функция my_function запущена\n" "Функция my_function отработана\n")


def test_log_error_text(capsys):
    my_function(1, "3")
    captured = capsys.readouterr()
    assert captured.out == (
        "Функция my_function запущена\n" "Ошибка в функции my_function: TypeError, входные параметры (1, '3') {}\n"
    )
