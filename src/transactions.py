import csv

import pandas as pd

import re


def read_transactions_from_csv(path_to_file_csv: str) -> list[dict]:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями"""
    if path_to_file_csv:
        with open(path_to_file_csv, "r", encoding="utf-8") as file:
            reader_csv = csv.DictReader(file, delimiter=";")
            result = [line for line in reader_csv]
            return result
        return []
    return []


def read_transactions_from_excel(path_to_file_excel: str) -> list[dict]:
    """Функция для считывания финансовых операций из Excel выдает список словарей с транзакциями"""
    if path_to_file_excel:
        df = pd.read_excel(path_to_file_excel, header=0)
        data = df.to_dict("records")
        return data
    return []


if __name__ == "__main__":
    result_csv = read_transactions_from_csv("../src/transactions.csv")
    print(result_csv)
    result_excel = read_transactions_from_excel("../src/transactions_excel.xlsx")
    print(result_excel)
