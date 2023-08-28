from telethon import TelegramClient, sync
import socks
# Use your own values here
api_id = 29778012
api_hash = '0014bdcb9a38a91365966a9956f61e6b'
phone = '+639272771573'
# token='6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y'
client = TelegramClient('teleClient_2',api_id,api_hash)
client.connect()
#此处的some_name是一个随便起的名称，第一次运行会让你输入手机号和验证码，之后会生成一个some_name.session的文件，再次运行的时候就不需要反复输入手机号验证码了
if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing of the client
    client.sign_in(phone, input('Enter the code: '))
print(client.get_me())
client.send_message(-677235937, '哪里不一样',parse_mode='html')
client.disconnect()