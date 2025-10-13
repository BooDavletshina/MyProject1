import os
from dotenv import load_dotenv
import requests
import json


load_dotenv()

def get_convert_sum(transaction: dict) -> float:
    url = "https://api.apilayer.com/exchangerates_data/convert"

    payload = {
        "amount": transaction["amount"],
        "from": transaction["code"],
        "to": "RUB"
    }

    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers, params=payload)

    result = response.json()

    data = json.loads(result)

    return data["result"]
