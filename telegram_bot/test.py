import telebot
from telebot import apihelper


apihelper.proxy = {'https': 'socks5h://192.168.100.10:49170'}

TOKEN = '1135717420:AAHoduicdqhxOHohOna6bnmf_YMFXON_RBM'
bot = telebot.TeleBot("1135717420:AAHoduicdqhxOHohOna6bnmf_YMFXON_RBM")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Видать ты хорошо подумал, раз пишешь мне, исскуственному интелекту на задворках телеги..\nты решил предсказать свою судьбу? \nну смотри есть несколько вариантов развития событий: \n средний \n плохой \n вообще хуевый  \n так же ты можешь спросить у меня: \n расскажи о себе \n как писать бота \n погадай мне')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'средний':
        bot.send_message(message.chat.id, 'Учись кодить ежедневно, и пусть настройка proxy через socks5 -pain in the ass когда нибудь ты познаешь светлую сторону кода ')
    elif message.text == 'плохой':
        bot.send_message(message.chat.id, 'Че там за ошибка в логе консоли вылетает? достало, подумаю завтра')
    elif message.text == 'вообще хуевый':
        bot.send_message(message.chat.id, 'Помочь-подсказать?')
    elif message.text == 'расскажи о себе':
        bot.send_message(message.chat.id, 'Я бот, программа написанная на Python 3.8')
    elif message.text == 'как писать бота':
        bot.send_message(message.chat.id, 'тебе понадобятся редактор кода, гитхаб, консоль и прокси')
    elif message.text == 'погадай мне':
        bot.send_message(message.chat.id, ' я те шоу экстрасенсов, чтобы гадать, ты ниче не попутал?')

bot.polling()