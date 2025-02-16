import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from flask import Flask, render_template_string
import threading

# Токен вашего бота
BOT_TOKEN = "7737944594:AAGauma1NWN41Lv9R61JoT6fLNnpqFUj_L8"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    # Создаем кнопку с веб-приложением
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Открыть веб-приложение",
        web_app=WebAppInfo(url="http://127.0.0.1:5000/")  # Укажите URL вашего Flask-приложения
    )

    # Отправляем сообщение с кнопкой
    await message.answer(
        "Нажмите кнопку ниже, чтобы открыть веб-приложение:",
        reply_markup=builder.as_markup()
    )

# Запуск бота
async def run_bot():
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запуск бота
    import asyncio
    asyncio.run(run_bot())