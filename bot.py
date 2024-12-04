import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.utils import executor

API_TOKEN = '7390881267:AAG1t89iR5VM9j1TAHBXiey'  # Убедитесь, что токен правильный

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher()

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.answer("Добро пожаловать в музыкального бота! Отправьте команду /play, чтобы начать.")

@dp.message_handler(commands=['play'])
async def play_music(message: Message):
    await message.answer("Вот ваш трек: /music_link")

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
