from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_lang = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Polish", callback_data="pl"),
            InlineKeyboardButton(text="English", callback_data="en"),
        ],
        [
            InlineKeyboardButton(text="Russian", callback_data="ru"),
            InlineKeyboardButton(text="Italian", callback_data="it"),
        ],
        [
            InlineKeyboardButton(text="Japanese", callback_data="ja"),
            InlineKeyboardButton(text="German", callback_data="de"),
        ],
        [
            InlineKeyboardButton(text="French", callback_data="fr"),
            InlineKeyboardButton(text="Czech", callback_data="cs"),
        ],


    ]
)
