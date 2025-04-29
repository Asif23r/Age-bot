from telegram.ext import Application, CommandHandler
from bot.handlers.start_handler import start
from bot.handlers.age_handler import age
from bot.handlers.broadcast_handler import broadcast
from bot.config import API_TOKEN

async def main():
    app = Application.builder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("age", age))
    app.add_handler(CommandHandler("broadcast", broadcast))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
