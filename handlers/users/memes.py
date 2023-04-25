from random import random
import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.memegenerator import get_random_meme_url


@dp.message_handler(Command("memes"))
async def generate_meme(message: types.Message):
    meme_url = get_random_meme_url()
    response = requests.get(meme_url)
    await message.answer_photo(response.content)
