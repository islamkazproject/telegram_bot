from loader import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    # Command '/help' handler
    await message.answer(text='/dog - для генерации смешных картинок с собаками\n'
                              '/answer - для генерации ответов(да / нет), грубо говоря отдать запрос во вселенную\n'
                              '/memes для генерации мемов')

