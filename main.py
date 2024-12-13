from aiogram import Bot, Dispatcher, F
import asyncio
from dotenv import load_dotenv
import os
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from utils.commands import set_commands
from handlers.start import get_start
from state.register import RegisterState
from handlers.register import start_register, enter, register_name, register_phone


load_dotenv() # загрузкa файла .env

# подключаем данные из окружения в переменные
token = os.getenv('TOKEN')  # обращения к этим переменным среды
admin_id = os.getenv('ADMIN_ID')

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


async def start_bot():
    await bot.send_message(admin_id, text="Я запустил бота")

dp.startup.register(start_bot)
dp.message.register(get_start, Command(commands='start')) # второй аргумент фильтр,
                                                          # при попадании в который будет вызван этот хендлер

# Регистрируем хендлеры регистрации
dp.message.register(start_register, F.text=="Регистрация")
dp.message.register(enter, F.text=="Войти")
dp.message.register(register_name, RegisterState.regName) # функция срабатывает только в состоянии regName
dp.message.register(register_phone, RegisterState.regPhone)

async def start():
    await set_commands(bot)
    try:
        # await dp.start_polling(bot, skip_updates=True)
        await bot.delete_webhook(drop_pending_updates=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())