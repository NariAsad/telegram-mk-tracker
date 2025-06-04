import os
import telebot

TOKEN = os.environ.get("TOKEN")
if TOKEN is None:
    raise ValueError("Переменная окружения TOKEN не найдена!")

bot = telebot.TeleBot(TOKEN)

# Обработчик новых сообщений (например, команды /start)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Бот работает!")

# Обработчик сообщений, приходящих непосредственно из канала
@bot.channel_post_handler(func=lambda message: True)
def handle_channel_post(message):
    # Здесь мы можем сохранить или вывести информацию из сообщения
    print("Новое сообщение из канала:")
    print("Message ID:", message.message_id)
    print("Date:", message.date)
    print("Text:", message.text)
    # (Можно сохранить данные в файл или базу данных для анализа)

# Обработчик редактированных сообщений канала
@bot.edited_channel_post_handler(func=lambda message: True)
def handle_channel_post_edit(message):
    print("Редактирование сообщения из канала:")
    print("Message ID:", message.message_id)
    print("Edit Date:", message.edit_date)
    print("New Text:", message.text)

# Запускаем бота
bot.polling(non_stop=True)
