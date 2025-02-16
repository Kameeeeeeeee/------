import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder
from flask import Flask, render_template_string
import threading

# Flask-приложение
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Веб-приложение</title>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }
                h1 {
                    font-size: 2.5rem;
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Привет, мир!</h1>
        </body>
        </html>
    """)

def run_flask():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    # Запуск Flask в отдельном потоке
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
