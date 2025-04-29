from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        birth_date = datetime.strptime(context.args[0], '%d-%m-%Y')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        await update.message.reply_text(f"Your age is: {age} years old. 🎂")
    except IndexError:
        await update.message.reply_text("Please provide your birthdate: /age dd-mm-yyyy")
    except ValueError:
        await update.message.reply_text("Invalid format. Use: dd-mm-yyyy")
