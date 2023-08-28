import time
from telegram.ext import Updater, CommandHandler
import schedule

TELEGRAM_BOT_TOKEN="6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y"
def send_message(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, Telegram!")

def schedule_message(bot, update):
    schedule.every(20).seconds.do(send_message, bot, update)
    while True:
        schedule.run_pending()
        time.sleep(1)

updater = Updater(token=TELEGRAM_BOT_TOKEN)
updater.dispatcher.add_handler(CommandHandler('send_message', schedule_message))

updater.start_polling()
updater.idle()