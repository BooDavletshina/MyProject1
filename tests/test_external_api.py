import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_convert_sum

load_dotenv()

api_key = os.getenv("API_KEY")

@patch('requests.get')
def test_get_convert_sum(mock_get, get_transactions):
    mock_get.return_value.json.return_value = {
                                                  "query": {
                                                    "amount": 25,
                                                    "from": "GBP",
                                                    "to": "JPY"
                                                  },
                                                  "result": 3724.305775,
                                                }
    assert get_convert_sum(get_transactions) == 3724.305775
    mock_get.assert_called_once_with(
        'https://api.apilayer.com/exchangerates_data/convert',
        headers = {'apikey': api_key},
        params = {'amount': '77302.31', 'from': 'USD', 'to': 'RUB'})
