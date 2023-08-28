# @Time: 2023/7/14 17:40
# _*_coding : utf-8 _*_
# @Authon : 
# @File : telebot
# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
#python操作小飞机，发送消息/文件/图片
# as said previously, obtain your API ID, API Hash, and Token from Telegram.
api_id = '29778012'
api_hash = '0014bdcb9a38a91365966a9956f61e6b'
token = '6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y'
message = "api 终于申请 到了"
# phone number
phone = '+639272771573'
# establishing a telegraph session and
# allocating it to a movable client
client = TelegramClient('session', api_id, api_hash)
# creating the connection and the session
client.connect()
# If the script is run for the first time, it will prompt you to enter a token, an #OTPSentTo
# number, your Telegram ID, or both.
if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing of the client
    client.sign_in(phone, input('Enter the code: '))
try:
    # Use
# my user id and access hash as a reference when
#using the receiver user-id and access-hash.
    receiver = InputPeerUser('user_id', 'user_hash')
    # using the Telegram client to send a message

    client.send_message(-677235937, '这是来自idea', parse_mode='html')
except Exception as e:
    # There may be numerous errors, such as peer
# error, incorrect access hash, flood error, etc.
 print(e);
# cutting off the Telegram conversation
client.disconnect()
