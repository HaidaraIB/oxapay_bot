from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler
from telegram.constants import ChatMemberStatus
from common.keyboards import build_user_keyboard
import os


async def check_if_user_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = await context.bot.get_chat_member(
        chat_id=int(os.getenv("CHANNEL_ID")), user_id=update.effective_user.id
    )
    if chat_member.status == ChatMemberStatus.LEFT:
        text = (
            f"You have to join the channel before using the bot :)\n"
            "Then Press Verify ✅"
        )
        markup = InlineKeyboardMarkup.from_column(
            [
                InlineKeyboardButton(text="Join Here", url=os.getenv("CHANNEL_LINK")),
                InlineKeyboardButton(text="Verify ✅", callback_data="check joined"),
            ]
        )
        if update.callback_query:
            await update.callback_query.edit_message_text(
                text=text, reply_markup=markup
            )
        else:
            await update.message.reply_text(text=text, reply_markup=markup)
        return False
    return True


async def check_joined(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_memeber = await context.bot.get_chat_member(
        chat_id=int(os.getenv("CHANNEL_ID")), user_id=update.effective_user.id
    )
    if chat_memeber.status == ChatMemberStatus.LEFT:
        await update.callback_query.answer(
            text=f"You have to join the channel before using the bot :)",
            show_alert=True,
        )
        return

    await update.callback_query.edit_message_text(
        text="Welcome...",
        reply_markup=build_user_keyboard(),
    )


check_joined_handler = CallbackQueryHandler(
    callback=check_joined, pattern="^check joined$"
)
