from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


register_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Регистрация"
        ),
        KeyboardButton(
            text="Войти"
        )
    ]
], resize_keyboard=True, one_time_keyboard=True,input_field_keyboard='Для продолжения нажмите кнопку ниже')
