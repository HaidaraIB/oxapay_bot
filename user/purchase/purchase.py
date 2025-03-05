from telegram import Chat, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler

from user.purchase.common import build_plans_keyboard, build_currencies_keyboard
from common.back_to_home_page import (
    back_to_user_home_page_button,
    back_to_user_home_page_handler,
)
from common.keyboards import build_back_button

from models.Currencies import Currencies
from models.Plans import Plans

import os

from start import start_command

PLAN, CURRENCY = range(2)


async def purchase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        plans_keyboard = build_plans_keyboard()
        plans_keyboard.append(back_to_user_home_page_button[0])
        await update.callback_query.edit_message_text(
            text="Choose the plan:",
            reply_markup=InlineKeyboardMarkup(plans_keyboard),
        )
        return PLAN


async def choose_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        if not update.callback_query.data.startswith("back"):
            context.user_data["plan"] = update.callback_query.data
        currencies_keyboard = build_currencies_keyboard()
        currencies_keyboard.append(build_back_button("back_to_choose_plan"))
        currencies_keyboard.append(back_to_user_home_page_button[0])
        await update.callback_query.edit_message_text(
            text="Choose the currency:",
            reply_markup=InlineKeyboardMarkup(currencies_keyboard),
        )
        return CURRENCY


back_to_choose_plan = purchase


async def choose_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        if not update.callback_query.data.startswith("back"):
            context.user_data["currency"] = update.callback_query.data
        await update.callback_query.edit_message_text(
            text=(
                "Send the coins to the following address:\n"
                f"<code>{Currencies.get_currency(update.callback_query.data).value['address']}</code>"
            ),
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(
                    text="Contact After Payment",
                    url=os.getenv("SUPPORT_URL"),
                )
            ),
        )
        return ConversationHandler.END


purchase_handler = ConversationHandler(
    entry_points=[
        CallbackQueryHandler(purchase, "^purchase$"),
    ],
    states={
        PLAN: [
            CallbackQueryHandler(
                choose_plan,
                lambda x: x in Plans.get_values(),
            )
        ],
        CURRENCY: [
            CallbackQueryHandler(
                choose_currency,
                lambda x: x in list(map(lambda c: c["name"], Currencies.get_values())),
            )
        ],
    },
    fallbacks=[
        CallbackQueryHandler(back_to_choose_plan, "back_to_choose_plan"),
        start_command,
        back_to_user_home_page_handler,
    ],
)
