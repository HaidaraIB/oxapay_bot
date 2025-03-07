from models.BaseEnum import BaseEnum


class Currencies(BaseEnum):
    USDT = {
        "name": "USDT",
        "address": "TGfobWF8wxobxKvVbJTojqtpPG6kWnoRMB",
    }
    BTC = {
        "name": "BTC",
        "address": "1Ldovnto26am2cNdPLcWhwbY5rm1cn7sJC",
    }

    @staticmethod
    def get_currency(value):
        if value == "USDT":
            return Currencies.USDT
        elif value == "BTC":
            return Currencies.BTC
