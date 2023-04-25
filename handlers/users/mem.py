
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Command
from utils.memegen import get_random_answer

from loader import dp, bot


# создаем класс состояний FSM
class MemeStates(StatesGroup):
    waiting = State()


@dp.message_handler(Command("answer"))
async def cmd_meme(message: types.Message):
    # сохраняем состояние в FSM
    await MemeStates.waiting.set()

    # отправляем сообщение с вопросом о подтверждении получения мема
    await message.answer("Хочешь получить ответ? (да / нет)")


# функция, которая будет вызываться при получении ответа на вопрос о получении мема
@dp.message_handler(state=MemeStates.waiting)
async def process_meme(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # получаем случайный гиф
        gif_url = get_random_answer()
        await message.answer(gif_url)

    else:
        # если пользователь не хочет получать мем, отправляем сообщение об отмене
        await message.answer("Хорошо, отменяем получение ответа.")

    # очищаем состояние FSM
    await state.finish()


