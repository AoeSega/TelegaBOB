from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# Укажите ваш токен бота
API_TOKEN = '7510750419:AAFkR1MMUvdnHtSYoVTNbKFk_jIctVbq_Mo'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(KeyboardButton("Хочу получить стратегию"))
main_menu.add(KeyboardButton("Посмотреть DashBoard"))

# Меню выбора бюджета
budget_menu = ReplyKeyboardMarkup(resize_keyboard=True)
budget_menu.add(KeyboardButton("50-100$"))
budget_menu.add(KeyboardButton("100-500$"))
budget_menu.add(KeyboardButton("500$ и более"))

# Меню для 50-100$
menu_50_100 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_50_100.add(KeyboardButton("Marqeta Inc. за 3,88$ 20шт"))
menu_50_100.add(KeyboardButton("Agilon Health Inc. за 2,09$ 30шт"))
menu_50_100.add(KeyboardButton("iQiyi Inc. за 2,16$ 30шт"))

# Меню для 100-500$
menu_100_500 = ReplyKeyboardMarkup(resize_keyboard=True)
menu_100_500.add(KeyboardButton("AT&T Inc за 23,16$ 20шт"))
menu_100_500.add(KeyboardButton("SoFi Technologies Inc. за 16,41$ 30шт"))
menu_100_500.add(KeyboardButton("Coupang LLC за 25,36$ 10шт"))

# Меню для 500$ и более
menu_500_plus = ReplyKeyboardMarkup(resize_keyboard=True)
menu_500_plus.add(KeyboardButton("Autodesk Inc. за 291,9$ 5шт"))
menu_500_plus.add(KeyboardButton("Informatica Corporation за 48,73$ 15шт"))
menu_500_plus.add(KeyboardButton("PRA Group Inc за 21,2$ 30шт"))


# Начало общения с ботом
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Выберите один из вариантов ниже", reply_markup=main_menu)


# Реакция на Главное меню
@dp.message_handler(lambda message: message.text == "Хочу получить стратегию")
async def choose_budget(message: types.Message):
    await message.answer("Каков ваш бюджет?", reply_markup=budget_menu)


@dp.message_handler(lambda message: message.text == "Посмотреть DashBoard")
async def show_dashboard(message: types.Message):
    await message.answer("Ссылка на Dashboard: ВСТАВЬ ССЫЛКУ ДАШБОРД")


# Реакция на выбор бюджета
@dp.message_handler(lambda message: message.text in ["50-100$", "100-500$", "500$ и более"])
async def choose_stock(message: types.Message):
    if message.text == "50-100$":
        await message.answer("Выберите один из вариантов ниже", reply_markup=menu_50_100)
    elif message.text == "100-500$":
        await message.answer("Выберите один из вариантов ниже", reply_markup=menu_100_500)
    elif message.text == "500$ и более":
        await message.answer("Выберите один из вариантов ниже", reply_markup=menu_500_plus)


# Реакция на выбор акций
@dp.message_handler(lambda message: message.text in [
    "Marqeta Inc. за 3,88$ 20шт",
    "Agilon Health Inc. за 2,09$ 30шт",
    "iQiyi Inc. за 2,16$ 30шт",
    "AT&T Inc за 23,16$ 20шт",
    "SoFi Technologies Inc. за 16,41$ 30шт",
    "Coupang LLC за 25,36$ 10шт",
    "Autodesk Inc. за 291,9$ 5шт",
    "Informatica Corporation за 48,73$ 15шт",
    "PRA Group Inc за 21,2$ 30шт",
])
async def strategy_created(message: types.Message):
    await message.answer("Стратегия успешно создана. В ближайшее время с вами свяжется специалист для более точной информации.")
    await message.answer("Пожалуйста, оставьте отзыв")


# Обработка отзыва
@dp.message_handler()
async def handle_feedback(message: types.Message):
    await message.answer("Спасибо за отзыв!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

