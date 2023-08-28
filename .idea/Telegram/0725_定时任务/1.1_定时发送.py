import schedule
import time
import datetime
import telebot

# 创建Telegram bot实例
token2 =  '6321364690:AAFvTiujKew0Fqi6OfL6awyM5Nx2LscJbVs'
# bot_3 = telebot.TeleBot("6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y")
bot_3 = telebot.TeleBot(token2)
# 定义要发送的消息内容和目标聊天ID
message = f"IDEA报告,当前时间：{datetime.datetime.now():%H:%M:%S}，这是你的对象照片"  #localtime()为当前时区的时间
chat_id = -677235937
# 定义定时任务函数
def send_message():
    bot_3.send_message(chat_id, message)
    bot_3.send_photo(chat_id,open(r"C:\Users\fzh00\Desktop\文件\测试图片\hr.jpg",'rb'))
# 设置每天定时发送消息的时间
# schedule.every().day.at("09:00").do(send_message)
schedule.every(5).minutes.do(send_message)
# 循环执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)