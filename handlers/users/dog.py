from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.doggen import get_random_dog


@dp.message_handler(Command("dog"))
async def cmd_dog(message: types.Message):
    img_dog = get_random_dog()
    await message.answer(img_dog)
