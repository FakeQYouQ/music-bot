import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

API_TOKEN = '7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg'

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Добро пожаловать в музыкального бота! Отправьте команду /play, чтобы начать.")

@dp.message(commands=['play'])
async def play_music(message: Message):
    await message.answer("Вот ваш трек: /music_link")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
