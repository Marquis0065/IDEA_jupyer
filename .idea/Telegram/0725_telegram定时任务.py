import schedule
import time
import datetime
import telebot
# schedule，可以参考官网：https://schedule.readthedocs.io/en/stable/
# 多线程使用：https://www.cnblogs.com/anpengapple/p/8051923.html
# 创建Telegram bot实例
bot = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
# 定义要发送的消息内容和目标聊天ID
message = f"这里是pycharm,3分钟的时间到了：{time.time()}"
chat_id = -677235937
# 定义定时任务函数
def send_message():
    bot.send_message(chat_id, message)
# 设置每天定时发送消息的时间
# schedule.every().day.at("09:00").do(send_message)
schedule.every(3).minutes.do(send_message)
# 循环执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)