from aiogram import Bot, Dispatcher
import asyncio

from aiogram.filters import Text

from handlers.register_handlers import register as register_handlers
from utils.comands import set_commands
from settings import bot_token, admin_id

async def startup_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(admin_id, text='Bot starts work')


async def shutdown_bot(bot: Bot):
    await bot.send_message(admin_id, text='Bot ends work')


async def start():
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    # register block
    dp.startup.register(startup_bot)
    dp.shutdown.register(shutdown_bot)
    register_handlers(dp=dp)
    # end of register block

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start())
