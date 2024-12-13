from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
import re
import os
from utils.db import Database


async def start_register(message: Message, state: FSMContext):
    await message.answer("Давайте начнем регистрацию. Для начала скажите как к Вам обращаться: ")
    await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext):
    await message.answer(f"Приятно познакомиться {message.text} 🤝. Теперь введите свой номер телефона 📞 в формате +7 "
                         f"и будьте внимательны, я чувствителен к формату")
    await state.update_data(regname=message.text) # сохраняем введенное имя в хранилище по ключу "regname"
    await state.set_state(RegisterState.regPhone)


async def register_phone(message: Message, state: FSMContext):
    if re.findall("^\+?[7][-\(]?\d{3}\)?-?\d{3}-?\d{2}-?\d{2}$",message.text):  # находим в message.text все непересекающиеся шаблоны
        await state.update_data(regphone=message.text) # в случае успеха сохраняем телефон в хранилище по ключу regphone

        reg_data = await state.get_data() # передеаём в переменную данные из хранилищ
        reg_name = reg_data.get("regname")
        reg_phone = reg_data.get("regphone")

        await message.answer(f"Регистрация прошла успешно {reg_name}! Спасибо что выбираете нас!")
        db = Database(os.getenv("DATABASE_NAME"))  # возвращаем значение ключа DATABASE_NAME переменной среды
        db.add_user(reg_name,reg_phone,message.from_user.id)
        await state.clear()
    else:
        await message.answer("Номер телефона указан в неверном формате")


async def enter(message: Message, state: FSMContext):
    await message.answer("Введите свой номер телефона, чтобы войти: ")
    await state.set_state(RegisterState.enter)