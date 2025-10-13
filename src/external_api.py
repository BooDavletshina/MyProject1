import os
from dotenv import load_dotenv
import requests


load_dotenv()

def get_convert_sum(transaction: dict) -> float:
    """Функция для конвертации валюты"""
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["operationAmount"]["amount"],
        "from": transaction["operationAmount"]["currency"]["code"],
        "to": "RUB"
    }

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=payload)

    result = response.json()

    return result["result"]
