from telegram import InlineKeyboardButton
from models.Currencies import Currencies
from models.Plans import Plans


def build_plans_keyboard():
    keyboard = [
        [
            InlineKeyboardButton(
                text=Plans.Daily.value['text'],
                callback_data=Plans.Daily.value['text'],
            ),
            InlineKeyboardButton(
                text=Plans.Weekly.value['text'],
                callback_data=Plans.Weekly.value['text'],
            ),
        ],
        [
            InlineKeyboardButton(
                text=Plans.Monthly.value['text'],
                callback_data=Plans.Monthly.value['text'],
            ),
            InlineKeyboardButton(
                text=Plans.Lifetime.value['text'],
                callback_data=Plans.Lifetime.value['text'],
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
    ]
    return keyboard
