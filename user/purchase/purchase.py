from telegram import Chat, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, ConversationHandler, CallbackQueryHandler
from user.purchase.common import build_plans_keyboard
from models.Plans import Plans
import os
from start import start_command

PLAN = range(1)


async def purchase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        plans_keyboard = build_plans_keyboard()
        await update.callback_query.edit_message_text(
            text="Choose the plan:",
            reply_markup=InlineKeyboardMarkup(plans_keyboard),
        )
        return PLAN


async def choose_plan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        plan = Plans.get_plan_from_text(update.callback_query.data).value
        await update.callback_query.edit_message_text(
            text=(
                f"Created a new invoice for <b>{plan['text']}</b>\n\n"
                f"Here's the invoice <a href='{plan['link']}'>link</a> you have to pay in case to receive the plan.\n\n"
                "Make sure you're sending the exact amount of coins as in the invoice, you may not receive your plan if you weren't."
            ),
            reply_markup=InlineKeyboardMarkup.from_button(
                InlineKeyboardButton(
                    text="Contact After Payment",
                    url=os.getenv("SUPPORT_URL"),
                ),
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
                lambda x: x in [p.value["text"] for p in Plans],
            )
        ],
    },
    fallbacks=[start_command],
    name="purchase_conversation",
    persistent=True,
)
