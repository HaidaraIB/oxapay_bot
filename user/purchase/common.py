from telegram import InlineKeyboardButton
from models.Currencies import Currencies
from models.Plans import Plans


def build_plans_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                text=Plans.Daily.value,
                callback_data=Plans.Daily.value,
            ),
            InlineKeyboardButton(
                text=Plans.Weekly.value,
                callback_data=Plans.Weekly.value,
            ),
        ],
        [
            InlineKeyboardButton(
                text=Plans.Monthly.value,
                callback_data=Plans.Monthly.value,
            ),
            InlineKeyboardButton(
                text=Plans.Lifetime.value,
                callback_data=Plans.Lifetime.value,
            ),
        ],
    ]
    return keyboard


def build_currencies_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                text=Currencies.USDT.value["name"],
                callback_data=Currencies.USDT.value["name"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=Currencies.BTC.value["name"],
                callback_data=Currencies.BTC.value["name"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=Currencies.ETH.value["name"],
                callback_data=Currencies.ETH.value["name"],
            ),
        ],
        [
            InlineKeyboardButton(
                text=Currencies.SOL.value["name"],
                callback_data=Currencies.SOL.value["name"],
            ),
        ],
    ]
    return keyboard
