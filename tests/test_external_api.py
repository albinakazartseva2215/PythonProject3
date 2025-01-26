import json
from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import get_transactions_with_usd_eur


def test_get_transactions_with_usd_eur():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 959922.59}

    with patch("requests.get", return_value=mock_response):
        result = get_transactions_with_usd_eur(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
        assert result == 959922.59
