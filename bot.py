import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode  # Обновлено для aiogram 3.x
from aiogram.types import Message
from aiogram.utils import executor

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

if __name__ == '__main__':
    executor.run(dp)