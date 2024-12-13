from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, "Рад приветствовать вас!😁 Этот бот поможет Вам найти жильё🏠 любого"
                                                 " вида в Шри-Ланке. Для начала войдите или зарегистрируйтесь.",
                           reply_markup=register_keyboard)