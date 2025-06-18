from asyncio import run

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
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


async def start_handler(message: types.Message):
    text = (f"Assalomu alaykum, "
            f"{message.from_user.mention_html(f'{message.from_user.full_name}')}")
    await message.answer(text=text, reply_markup=user_main_keyboard)


async def menu_handler(message: types.Message):
    await message.answer(
        text="Отправьте 📍 геолокацию или выберите адрес доставки",
        reply_markup=address_keyboard
    )


async def orders_handler(message: types.Message):
    await message.answer("Sizning buyurtmangiz yo'q")


async def review_handlar(message: types.Message):
    await message.answer("Otzivlar yo'q")


async def settings_handler(message: types.Message):
    await message.answer("Nastroyka yo'q")


async def back_handler(message: types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=user_main_keyboard)


async def main():
    bot = Bot(token="7999529306:AAE_k-zJxD4A_Rk5ifaq3SAup2AtXLApH8M", default=DefaultBotProperties(parse_mode='HTML'))
    dp = Dispatcher()
    dp.message.register(start_handler, Command('start'))
    dp.message.register(menu_handler, F.text == "🍴 Меню")
    dp.message.register(back_handler, F.text == "⬅ Назад")
    dp.message.register(orders_handler, F.text == "🛍 Мои заказы")
    dp.message.register(review_handlar, F.text == "✍ Оставить отзыв")
    dp.message.register(settings_handler, F.text == "⚙ Настройки")

    await dp.start_polling(bot, polling_timeout=0)


if __name__ == '__main__':
    run(main())
