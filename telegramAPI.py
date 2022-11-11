from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

BOT_TOKEN = "5645949742:AAGDmze2SXINA1kqc4UJjAsSVVNaE9aDjik"

updater = Updater(BOT_TOKEN,
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Hello sir {update.message.chat.username}."
    )

def stop_shit(update: Update, context: CallbackContext):
    update.message.reply_text(
        f"Stop do this shit\n{update.message.chat.full_name}"
    )

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, stop_shit))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker, stop_shit))
updater.start_polling()
