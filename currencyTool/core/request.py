import requests
from http import HTTPStatus
import json

# Uses currency var to send a request to fixer.io to get the latest exchange rates with currency as a base
def fetch_exchange_rates_by_currency(currency):
    response = requests.get(f'https://api.fixer.io/latest?base={currency}')

    if response.status_code == HTTPStatus.OK:
        return json.loads(response.text)
    elif response.status_code == HTTPStatus.NOT_FOUND:
        raise ValueError(f'Could not find the exchange rates for: {currency}.')
    elif response.status_code == HTTPStatus.BAD_REQUEST:
        raise ValueError(f'Invalid base currency value: {currency}.')
    else:
        raise Exception((f'Something went wrong and we were unable to fetch the exchange rates for: {currency}'))

