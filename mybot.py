import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pushpull.settings')
import django
django.setup()
from secret import token
import telebot 
from tasklist import models
from mainpage import models

class MyBot(telebot.TeleBot):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__users = {}
        try:
            self.__load_users()
        except:
            print('No users')
    
    def add_user(self, msg):
        if msg.chat.id not in self.__users:
            self.__users[msg.chat.id] = ''
            self.__save_users()

    def __save_users(self):
        f = open('my_users.txt', 'w')
        for u in self.__users:
            f.write(str(u) + '\n')
        f.close()
    
    def __load_users(self):
        f = open('my_users.txt')
        for line in f:
            self.__users[line] = ''
        f.close()



bot = MyBot(token)

@bot.message_handler(commands= ['start'])
def start(message):
    print ("В консоль: начало работы")
    bot.add_user(message)
    bot.send_message(
        message.chat.id,
        '<b>Пользователю: готов!</b>', parse_mode='html')
    
@bot.message_handler(commands= ['list'])
def start(message):
    dists = models.Dist.objects.all()
    print(dists)
    print(message.text)
    new_message = "Введите пункт погрузки и выгрузки"
    for t in dists:
        new_message += "%s\n" % (
            str(t)
        )
    #bot.add_user(message)
    bot.send_message(
        message.chat.id,
        '<b>Пункт погрузки: </b>\n%s' % new_message,
        parse_mode='html')

bot.polling(none_stop=True)


@bot.message_hadler(commands=['order'])
def start(message):
    zapros = models.Zapros.objects.all()
    print(zapros)
    print(message.text)
    new_message = ''
    for z in zapros:
        new_message += 'стоимость равна='(
            str(z)
        )

    bot.send_message(
    message.chat.id,
    '<b>Точка загрузки и точка выгрузки: </b>\n%s' % new_message,
    parse_mode='html')