import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")

if TOKEN is None:
    raise ValueError("BOT_TOKEN не задан в переменных окружения")

bot = telebot.TeleBot(TOKEN)
