import random
import telebot
from parser import parser


URL = 'https://citaty.info/man/quotes'
BOT_KEY = '1855772848:AAECdtBCM5LWyRbmEi0LplbCUJNWLLaDpbQ'

quotes_list = parser(URL)

bot = telebot.TeleBot(BOT_KEY)

@bot.message_handler(commands=['start'])
def greeting(msg):
    bot.send_message(msg.chat.id, 'Greetings, hero!')

@bot.message_handler(commands=['quote'])
def quotes_daily(msg):
    bot.send_message(msg.chat.id, str(random.choice(quotes_list)))

bot.polling()