from aiogram.fsm.state import State, StatesGroup


class TranslateFSM(StatesGroup):
    FROM_LANG = State()
    TRANSLATE_TEXT = State()
    TO_LANG = State()
