from telegram import Chat, Update
from telegram.ext import ContextTypes, CommandHandler


async def get_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        await update.message.reply_text(
            text=f"<code>{update.effective_user.id}</code>",
        )


get_user_id_command = CommandHandler("id", get_user_id)
