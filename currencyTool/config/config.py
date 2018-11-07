from .config_error import ConfigError
from currencyTool.core import DbClient

def get_config():
    config = None

    # exchange_rates is the name of db, config is the name of the collection
    # instantiate a class with given argumetns and give it the name of db
    with DbClient('exchange_rates', 'config') as db:
        config = db.find_one()

        if config is None:
            error_message = ('It was not possible to get your base currency, that probably happened b/c it has not been set yet.\nPlease, use the option --setbasecurrency')
            raise ConfigError()

        return config
