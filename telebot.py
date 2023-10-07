import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import openai

class Reference:
    '''
    A class to store previously response from the chartGPT API
    '''
    def __init__(self) -> None:
        self.response = ""

load_dotenv()
openai.api_key = os.getenv("OpenAI_API_KEY")

reference = Reference()
TOKEN = os.getenv("TOKEN")

# model name
MODEL_NAME = "gpt-3.5-turbo"

# Initialize bot and dispatcher
bot = Bot(token = TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    '''
    a function to clear the previous convertionsatioin
    '''
    reference.response = ""


@dispatcher.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am tele Bot!\n Created By Dibya")

@dispatcher.message_handler(commands=['help'])
async def command_start_handler(message: types.Message):
    """
    This handler to display the help menu.
    """
    help_com = """
    Hi there, do you need some help !!!
    refer from following options:
    /start - to start the conversatioin
    /clear - to remove the previous conversation
    /help - how did you get this you stupid,
    Hope this help :)
    """
    await message.reply(help_com)


@dispatcher.message_handler(commands=['clear'])
async def command_start_handler(message: types.Message):
    """
    A handler to clear the previous conversatioin and context
    """
    clear_past()
    await message.reply("Hi Dibya clear all your previous conversatioin. So rest assure.")



if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)