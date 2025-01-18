import tempfile

import pytest

from src.decorators import log, my_function


def test_log_text(capsys) -> None:
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ("Функция my_function запущена\n" "Функция my_function отработана\n")


def test_log_error_text(capsys) -> None:
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(1, "3")
    captured = capsys.readouterr()
    assert captured.out == (
        "Функция my_function запущена\n" "Ошибка в функции my_function: TypeError, входные параметры (1, '3') {}\n"
    )


def test_log_text_in_filename(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):

        return x + y

    my_function(1, 3)

    with open(log_file_path, "r", encoding="utf-8") as file:

        logs = file.read()
    assert logs == ("Функция my_function запущена\n" "Функция my_function отработана. Результат: 4\n")


def test_log_error_in_filename(capsys):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def my_function(x, y):
        return x + y

    my_function(1, "3")

    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()

    assert logs == (
        "Функция my_function запущена\n" "Ошибка в функции my_function: TypeError, входные параметры (1, '3') {}\n"
    )
