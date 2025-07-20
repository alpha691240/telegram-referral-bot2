from telegram.ext import Updater, CommandHandler
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    user = update.effective_user
    update.message.reply_text(f"Hello {user.first_name}, welcome to Freshman Tutorials!")

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))

updater.start_polling()
print("Bot is running...")
updater.idle()
