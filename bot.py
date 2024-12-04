import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import os

API_TOKEN = '7390881267:AAG1t89iR5VM9j1TAHBXieyWu9S4nvtQDzg'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Добро пожаловать в музыкального бота! Отправьте команду /play, чтобы начать.")

# Обработчик команды /play
@dp.message_handler(commands=['play'])
async def play_music(message: types.Message):
    await message.reply("Вот ваш трек: /music_link")

# Отправка ссылки на трек
@dp.message_handler(commands=['music_link'])
async def send_music_link(message: types.Message):
    await message.reply("Трек доступен по следующей ссылке: http://your_server_address/tracks/aikko-prinjat-sebja.mp3")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
