from aiogram import Bot, types
from aiogram.fsm.context import FSMContext
from keyboards.inline_keyboards import select_lang
from utils.fsm import TranslateFSM


async def echo(message: types.Message):
    await message.answer(message.text)


async def translate(message: types.Message, state: FSMContext):
    await message.answer("Выберите язык с которого будет перевод", reply_markup=select_lang)
    await state.set_state(TranslateFSM.FROM_LANG)


async def from_lang(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Выберите язык на который надо перевести текст", reply_markup=select_lang)
    await state.set_state(TranslateFSM.TO_LANG)
