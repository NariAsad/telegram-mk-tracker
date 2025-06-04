import os
import telebot

TOKEN = os.environ.get("TOKEN")
if TOKEN is None:
    raise ValueError("Переменная окружения TOKEN не найдена!")

bot = telebot.TeleBot(TOKEN)
