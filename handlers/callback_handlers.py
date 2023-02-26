from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.fsm import TranslateFSM

from translate_api.translate_method import get_translate


async def callback_lang(call: CallbackQuery, state: FSMContext):
    await state.update_data(from_lang=call.data)
    await call.message.answer("Введите текст для перевода")
    await state.set_state(TranslateFSM.TRANSLATE_TEXT)
    await call.answer()


async def callback_to_lang(call: CallbackQuery, state: FSMContext):
    await call.answer()
    await state.update_data(to_lang=call.data)
    data = await state.get_data()
    inf = get_translate(data).json()
    await state.clear()
    await call.message.answer(f"Перевод: {inf['translations'][0]['translated'][0]}")

