from aiogram import Dispatcher
from aiogram.filters import Command

from handlers.message_handlers import echo, translate, from_lang
from utils.fsm import TranslateFSM
from handlers.callback_handlers import callback_lang, callback_to_lang


def register(dp: Dispatcher):
    dp.message.register(translate, Command(commands=['translate']))
    dp.callback_query.register(callback_lang, TranslateFSM.FROM_LANG)
    dp.message.register(from_lang, TranslateFSM.TRANSLATE_TEXT)
    dp.callback_query.register(callback_to_lang, TranslateFSM.TO_LANG)
    dp.message.register(echo)
