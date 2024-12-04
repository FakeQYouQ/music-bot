from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен вашего бота
TOKEN = '7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg'

# Функция, которая будет отправлять сообщение пользователю с кнопкой
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Open Music App", web_app=WebAppInfo(url="https://fakeqyouq.github.io/music-bot/"))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Добро пожаловать в музыкальную платформу!', reply_markup=reply_markup)

# Основная функция для запуска бота
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
