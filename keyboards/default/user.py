from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍴 Меню")],
        [KeyboardButton(text="🛍 Мои заказы")],
        [KeyboardButton(text="✍ Оставить отзыв"), KeyboardButton(text="⚙ Настройки")]
    ],
    resize_keyboard=True,
    is_persistent=True
)

address_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🗺 Мои адреса")],
        [
            KeyboardButton(text="📍 Отправить геолокацию", request_location=True),
            KeyboardButton(text="⬅ Назад")
        ]
    ],
    resize_keyboard=True,
    is_persistent=True
)


back_user_main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅ Назад")]
    ],
    resize_keyboard=True,
    is_persistent=True
)

phone_number_share = KeyboardButton(text="📞 Отправить номер телефона", request_contact=True)
location_share = KeyboardButton(text="📍 Отправить геолокацию", request_location=True)
