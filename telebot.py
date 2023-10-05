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
dp = Dispatcher(bot)

def clear_past():
    '''
    a function to clear the previous convertionsatioin
    '''
    reference.response = ""


@dp.message_handler(commands=['start'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or  `/help `command
    """
    await message.reply("Hi\nI am tele Bot!\n Created By Dibya")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)