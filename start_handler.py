from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.config import CHANNEL_LINK, OWNER_ID, user_ids

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    user_id = user.id
    keyboard = [
        [InlineKeyboardButton("Join Channel 🔔", url=CHANNEL_LINK)],
        [InlineKeyboardButton("Contact Developer 💬", url="https://t.me/yourusername"),
         InlineKeyboardButton("Friend's GC 💌", url="https://t.me/yourgroup")],
        [InlineKeyboardButton("Notes Bot 📝", url="https://t.me/notes_bot_link")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if user_id not in user_ids:
        user_ids.append(user_id)
        await update.message.reply_text("Welcome! Please join the channel first:", reply_markup=reply_markup)
        await context.bot.send_message(chat_id=OWNER_ID,
            text=f"New User Started Bot!
• Name: {user.full_name}
• Username: @{user.username or 'N/A'}
• User ID: {user_id}")
    else:
        await update.message.reply_text("Welcome back to the Age Calculator Bot!", reply_markup=reply_markup)
