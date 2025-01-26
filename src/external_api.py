import json
import os
import typing

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = f"https://api.apilayer.com/exchangerates_data/convert"

def get_transactions_with_usd_eur(transaction: dict, RUB=None) -> float:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency_code != "RUB":
        try:
            payload = {"amount": f"{amount}", "from": f"{currency_code}", "to": "RUB"}
            headers = {"apikey": f"{API_KEY}"}
            response = requests.get(url, headers=headers, params=payload)
            status_code = response.status_code
            if status_code == 200:
                result = response.json()
                currency_amount = result["result"]
                return round(currency_amount, 2)
            else:
                print(status_code)
        except requests.exceptions.RequestException:
            print("Ошибка конвертации валюты")
    else:
        return round(amount, 2)


if __name__ == "__main__":
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    print(get_transactions_with_usd_eur(transaction))
