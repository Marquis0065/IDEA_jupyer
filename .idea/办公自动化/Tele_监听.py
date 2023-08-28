# Use your own values from my.telegram.org
# 自己根据上面地址注册的机器人
api_id =29778012
api_hash = '0014bdcb9a38a91365966a9956f61e6b'

# telethon直接pip安装最新的就好了
import builtins
from telethon import TelegramClient, events, sync
from telethon.tl.custom import button
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.users import GetFullUserRequest

phone_number = '+639272771573'  # 用户号码
client = TelegramClient(phone_number, api_id, api_hash)

# 群号的地址，自己建个群可以找到群号的地址
channel = 'https://t.me/+DpNQkRpZO_IzYzVl'
import time

from telethon import functions
all_id=[]

button=1
chat_id=None

# 监听事件，当你收到一条信息，无论是群也好或者个人也好都会触发这个
@events.register(events.NewMessage)
async def msg_event_handler(event):
    global chat_id;global all_id
    if(chat_id==event.chat_id):
        message = event.message
        print(888888)
        # 判断是否是群组或者频道发送的消息
        # if event.is_channel or event.is_group:
        ## 获取消息的id，
        print(event.sender_id)
        print(event.chat_id)
        all_id.append(event.sender_id)
        print(888888)
    # await client.send_message(event.sender_id, 'What are you sending?')

client.add_event_handler(callback=msg_event_handler,
                         event=events.NewMessage(incoming=True))

async def main():
    global button;global chat_id;global all_id
    # 发信息
    # await client.send_message('键平 键平', 'Hello, myself!')
    #
    # # You can, of course, use markdown in your messages:
    # message = await client.send_message(
    #     '键平 键平',
    #     '1111',
    #     link_preview=False
    # )
    # # You can reply to messages directly if you have a message object
    # await message.reply('Cool!')

    # 可以拿到发给个人的信息
    # You can print the message history of any chat:
    # async for message in client.iter_messages('键平'):
    #     print(message.text)
    # 可以根据群地址拿到群里面的信息
    messages = client.iter_messages(channel, limit=1)
    async for message in messages:
        print(message.text)

        # 这里可以拿到群id
        chat_id=message.chat_id
        print(chat_id)
        button=0


# 可以拿到自己所有好友或者群号的id，这个id可以用来拉群用
# async for dialog in client.iter_dialogs():
#     print(dialog.name, 'has ID', dialog.id)

# path = await client.download_profile_photo(channel)
# print(path)


# @client.on(events.UserUpdate)
# async def handler(event):
#     # If someone is uploading, say something
#     if event.uploading:
#         await client.send_message(event.user_id, 'What are you sending?')

# result = await client(functions.photos.GetUserPhotosRequest(
#     user_id="",
#     offset=0,
#     max_id=0,
#     limit=100
# ))

# 这all_id是数组，看我上面的监听函数，只要有人发信息，就把他的id记下来，然后放到数组里面，下一次循环就会把这个人拉进群，只是不是好友拉不进，
    while(len(all_id)>0):
        id=all_id.pop()

        try:
            await client(AddChatUserRequest(
            # 这个chat_id是拿到的群id，群id上面的中间部分代码可以拿到
            chat_id,
            # 这个是监听拿到的id
            id,
            fwd_limit=10  # Allow the user to see the 10 last messages
            ))
        except Exception as e:
            print("eeee")

while 1:
    with client:
        client.loop.run_until_complete(main())
    time.sleep(10)
