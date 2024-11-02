from logic import get_joke
from config import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "привет")

@bot .message_handler(commands=['get_joke'])
def handler_start(message):
    bot.send_message(message.chat.id, get_joke())

bot.polling(none_stop=True)