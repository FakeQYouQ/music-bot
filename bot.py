from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

def start(update: Update, context):
    # Кнопка для запуска мини-приложения
    keyboard = [[InlineKeyboardButton("Слушать музыку", url="https://yourappurl.com")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Нажмите на кнопку, чтобы послушать музыку.", reply_markup=reply_markup)

def main():
    updater = Updater("7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
