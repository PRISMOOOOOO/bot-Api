from data import get_data_as_API
import telebot
from telebot.types import Message

bot = telebot.TeleBot("7150015201:AAGrbxtIkeST2-DMVivnVwhqm_pFHQQlWbY")

@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, "سلام! لطفاً نام یک شهر را بنویسید.")

@bot.message_handler(func=lambda message: True)
def get_city_name(message: Message):
    city_name = message.text
    data = get_data_as_API(city_name)

    for k,v in data.items():
        bot.send_message(message.chat.id, f"{k}-->{v}")

bot.polling()

