from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет!")

def main() -> None:
    application = Application.builder().token("7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg").build()
    
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    application.run_polling()

if __name__ == "__main__":
    main()
