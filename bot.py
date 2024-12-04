import logging
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.types import Message

API_TOKEN = '7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Добро пожаловать в музыкального бота! Отправьте команду /play, чтобы начать.")

@dp.message(commands=['play'])
async def play_music(message: Message):
    await message.answer("Вот ваш трек: /music_link")

async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
