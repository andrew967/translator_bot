from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command="help",
            description="Bot help"
        ),
        BotCommand(
            command="translate",
            description="Translator"
        )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
