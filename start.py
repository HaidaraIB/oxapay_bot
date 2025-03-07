from telegram import Update, Chat, BotCommandScopeChat
from telegram.ext import (
    CommandHandler,
    ContextTypes,
    Application,
    ConversationHandler,
)
import os
import models
from custom_filters import Admin
from common.decorators import (
    check_if_user_banned_dec,
    add_new_user_dec,
    check_if_user_member_decorator,
)
from common.keyboards import build_user_keyboard, build_admin_keyboard
from common.common import check_hidden_keyboard


async def inits(app: Application):
    await models.Admin.add_new_admin(admin_id=int(os.getenv("OWNER_ID")))


async def set_commands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    st_cmd = ("start", "Start the bot")
    cancel_cmd = ("cancel", "Cancel the operation")
    revert_cmd = ("revert", "Revert the latest transaction")
    id_cmd = ("id", "get the user id")
    commands = [st_cmd, cancel_cmd, revert_cmd, id_cmd]
    if Admin().filter(update):
        commands.append(("admin", "admin command"))
    await context.bot.set_my_commands(
        commands=commands, scope=BotCommandScopeChat(chat_id=update.effective_chat.id)
    )


@add_new_user_dec
@check_if_user_banned_dec
@check_if_user_member_decorator
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE:
        await set_commands(update, context)
        await update.message.reply_text(
            text=(
                "~ Welcome back!\n\n"
                "This tool allows you to send transactions on ERC-20 network that will remain unconfirmed for some time, so wallets like Exodus or Atomic will display the total balance.\n\n"
                "Privileges\n"
                "> Instant sending of any amount;\n"
                "> Traceable on Etherscan;\n"
                "> Revertible any time.\n\n"
                "Sendable Tokens\n"
                "> USDT\n"
                "> BTC\n"
                "> ETH\n"
                "> SOL"
            ),
            reply_markup=build_user_keyboard(),
        )
        return ConversationHandler.END


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type == Chat.PRIVATE and Admin().filter(update):
        await set_commands(update, context)
        await update.message.reply_text(
            text="أهلاً بك...",
            reply_markup=check_hidden_keyboard(context),
        )

        await update.message.reply_text(
            text="تعمل الآن كآدمن 🕹",
            reply_markup=build_admin_keyboard(),
        )
        return ConversationHandler.END


start_command = CommandHandler(command=["start", "cancel"], callback=start)
admin_command = CommandHandler(command="admin", callback=admin)
