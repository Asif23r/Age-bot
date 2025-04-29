from telegram import Update
from telegram.ext import ContextTypes
from bot.config import OWNER_ID, user_ids

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != OWNER_ID:
        await update.message.reply_text("You are not authorized to use this command.")
        return

    message = ' '.join(context.args)
    for user_id in user_ids:
        try:
            await context.bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send to {user_id}: {e}")
    await update.message.reply_text("Broadcast sent.")
