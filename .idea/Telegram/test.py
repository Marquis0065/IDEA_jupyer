# from telethon import TelegramClient,sync
# import socks
# api_id = 29778012
# api_hash = '0014bdcb9a38a91365966a9956f61e6b'
# phone='+639272771573'
# client = TelegramClient('teleClient_2',api_id,api_hash)
# client.connect()
# if not client.is_user_authorized():
#     client.send_code_request(phone)
#     # signing of the client
#     client.sign_in(phone, input('Enter the code: '))
# print(client.get_me())
# client.send_message(-677235937, 'H,当地文化',parse_mode='html')
# client.disconnect()

#-------------------------------------------------chatGPT-------
# import openai
# openai.api_key= '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'
# messages = []
# system_message = input("What type of chatbot you want me to be?")
# messages.append({"role":"system","content":system_message})
# print("Alright! I am ready to be your friendly chatbot" + "\n" + "You can now type your messages.")
# message = input("")
# messages.append({"role":"user","content": message})
# response=openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=messages
# )
# reply = response["choices"][0]["message"]["content"]
# print(reply)

#-------------------------------------
# import openai
# openai.api_key= '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'
# messages = []
# system_message = input("What type of chatbot you want me to be?")
# messages.append({"role":"system","content":system_message})
# print("Alright! I am ready to be your friendly chatbot" + "\n" + "You can now type your messages.")
# message = input("")
# messages.append({"role":"user","content": message})
# response=openai.ChatCompletion.create(
#
#     model="gpt-3.5-turbo",
#     messages=messages
# )
# reply = response["choices"][0]["message"]["content"]
# print(reply)

#---------------------------------------chatGPT--------------
from telethon import TelegramClient, sync
import openai

openai.api_key = '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'
def getChat(text):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.3,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.8,
        best_of=1,
        max_tokens=1000
    )

    return completion["choices"][0]["text"]
api_id = 29778012
api_hash = '0014bdcb9a38a91365966a9956f61e6b'
phone = '+639272771573'
# token='6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y'
client = TelegramClient('test',api_id,api_hash)
client.connect()
#此处的some_name是一个随便起的名称，第一次运行会让你输入手机号和验证码，之后会生成一个some_name.session的文件，再次运行的时候就不需要反复输入手机号验证码了
if not client.is_user_authorized():
    client.send_code_request(phone)
    # signing of the client
    client.sign_in(phone, input('Enter the code: '))

@app.on_message()
async def echo(client: client, message: message):
    chatGpt_text = getChat(message.text)
    await message.reply(chatGpt_text)