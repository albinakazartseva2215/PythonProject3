import json
import os
import typing
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    filename="../logs/utils.log",
                    filemode="w", encoding="utf-8")

# Создаем логеры для различных компонентов программы
utils_loger = logging.getLogger("utils")


def get_path_to_file(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    utils_loger.debug("Начало работы функции")
    if path_to_file:
        utils_loger.debug("Файл указан")
        with open(path_to_file, "r", encoding="utf-8") as file:
            transactions_list = json.load(file)
            if transactions_list:
                utils_loger.debug("Файл загружен")
                return transactions_list

        utils_loger.error("Файл не открылся")
        return []

    else:
        utils_loger.error("Файл не указан")
        return []


if __name__ == "__main__":
    print(get_path_to_file("../data/operations.json"))
    utils_loger.debug("Работа программы завершена")
