# @Time: 2023/7/30 20:50
# _*_coding : utf-8 _*_
# @Authon :
# @File : Timeloop库
from timeloop import Timeloop
import time
import datetime
from datetime import timedelta
import telebot

bot = telebot.TeleBot('6106076754:AAHjxPSBpyjwpY-lq1iEslUufW46XQvAfr0')
t1 = Timeloop()

while 1:
    @t1.job(interval=timedelta(seconds=300))
    def loop_monitor():
        bot.send_message(-677235937,'Timeloop库运行idea：{}'.format(datetime.datetime.now().strftime('%H:%M')))

