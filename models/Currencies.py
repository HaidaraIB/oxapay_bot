from models.BaseEnum import BaseEnum


class Currencies(BaseEnum):
    USDT = {
        "name": "USDT",
        "address": "",
    }
    BTC = {
        "name": "BTC",
        "address": "",
    }
    ETH = {
        "name": "ETH",
        "address": "",
    }
    SOL = {
        "name": "SOL",
        "address": "",
    }

    @staticmethod
    def get_currency(value):
        if value == "USDT":
            return Currencies.USDT
        elif value == "BTC":
            return Currencies.BTC
        elif value == "ETH":
            return Currencies.ETH
        elif value == "SOL":
            return Currencies.SOL
