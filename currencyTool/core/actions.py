import sys
from argparse import Action
from datetime import datetime

from .db import DbClient
from .request import fetch_exchange_rates_by_currency
from currencyTool.config import get_config

