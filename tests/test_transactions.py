from unittest.mock import Mock, patch

import pytest
from src.transactions import read_transactions_from_csv, read_transactions_from_excel

@pytest.fixture
def mock_read_file():
    with patch("src.transactions") as mock_read:
        mock_read.return_value = [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  },
  {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }]
        yield mock_read


def test_read_transactions_from_csv(mock_read_file):
    transactions_list = mock_read_file("../data/transactions.csv")
    assert len(transactions_list) == 3


def test_read_transactions_from_csv_no_path():
    transactions_list = read_transactions_from_csv("")
    assert transactions_list == []


def test_read_transactions_from_excel(mock_read_file):
  transactions_list = mock_read_file("../data/transactions_excel.xlsx")
  assert len(transactions_list) == 3





