import logging
# from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# 导入ChatGPT模型和tokenizer
from transformers import AutoModelForCausalLM, AutoTokenizer
# 设置ChatGPT模型和tokenizer的名称
MODEL_NAME = "microsoft/DialoGPT-large"
TOKENIZER_NAME = "microsoft/DialoGPT-large"

# 初始化ChatGPT模型和tokenizer
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)

# 设置Telegram Bot的访问令牌
TOKEN = "6377312623:AAGz3ZSMVswWq0QVlihRPklw8b7skSBP16Y"
# 启用日志记录
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# 定义start命令处理程序
def start(update: Update, context: CallbackContext) -> None:
    """发送欢迎消息"""
    update.message.reply_text('你好！我是ChatGPT Bot。请向我发送消息进行对话。')

# 定义对话处理程序
def chat(update: Update, context: CallbackContext) -> None:
    """使用ChatGPT模型生成回复"""
    # 获取用户输入的消息
    user_input = update.message.text
    # 将用户输入编码为ChatGPT模型可接受的输入格式
    input_ids = tokenizer.encode(user_input, return_tensors='pt')
    # 使用ChatGPT模型生成回复
    output = model.generate(input_ids, max_length=1000, num_return_sequences=1)
    # 解码模型输出为文本
    bot_reply = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    # 发送回复消息给用户
    update.message.reply_text(bot_reply)

# 定义错误处理程序
def error(update: Update, context: CallbackContext) -> None:
    """在错误发生时记录错误信息"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# 创建Telegram Bot的Updater和Dispatcher
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# 添加命令处理程序和消息处理程序
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
dispatcher.add_error_handler(error)

# 启动Telegram Bot
updater.start_polling()
updater.idle()