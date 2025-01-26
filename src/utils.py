import json
import os
import typing


def get_path_to_file(path_to_file: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    if path_to_file:
        with open(path_to_file, "r", encoding="utf-8") as file:
            transactions_list = json.load(file)
            if transactions_list:
                return transactions_list
        return []

    else:
        return []


if __name__ == "__main__":
    print(get_path_to_file("../data/operations.json"))
