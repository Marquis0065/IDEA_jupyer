from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

while True:
    try:
        user_input = input("You: ")
        bot_response = bot.get_response(user_input)
        print("Bot: ", bot_response)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
