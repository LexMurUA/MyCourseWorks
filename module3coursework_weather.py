from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import requests
import re
from datetime import datetime
import asyncio

# Ваш токен Telegram бота
API_TOKEN = 'Token'

# Створення об'єкта бота
bot = Bot(token=API_TOKEN) 
dp = Dispatcher() 

# API ключ для OpenWeather
WEATHER_API_KEY = '39d64c97b795988c322ff6228a8dc8a7'

# Кнопки для вибору режиму
mode_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Поточна погода"), KeyboardButton(text="Прогноз на 24 години")]
], resize_keyboard=True)

# Словник для збереження стану користувача
user_state = {}

# Функція для очищення назв міст
def clean_city_name(city_name):
    cleaned_name = re.sub(r"[^a-zA-Zа-яА-ЯёЁіІїЇєЄ'’\-\s]", "", city_name)
    return cleaned_name.strip()

# Функція для отримання поточної погоди
def new_status(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ua&units=metric&appid={WEATHER_API_KEY}'
    res = requests.get(url)
    return res.json()


def new_status_four(city):
    url_four_days = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&cnt=8&lang=ua&units=metric&appid={WEATHER_API_KEY}'
    res_four_days = requests.get(url_four_days)
    return res_four_days.json()

# Обробник команди /start
@dp.message(Command("start"))  
async def send_welcome(message: Message):
    await message.answer("Привіт! Я погодний бот, оберіть режим прогнозу:\n"
                         "- Поточна погода\n"
                         "- Прогноз на 24 години",
                         reply_markup=mode_keyboard)

# Обробник вибору режиму
@dp.message(lambda message: message.text in ["Поточна погода", "Прогноз на 24 години"])
async def select_mode(message: Message):
    user_state[message.from_user.id] = {"mode": message.text}
    await message.answer("Введіть назву міста для отримання інформації.")

# Обробник текстових повідомлень (назва міста)
@dp.message()
async def handle_city_input(message: Message):
    user_data = user_state.get(message.from_user.id)
    if not user_data or "mode" not in user_data:
        await message.answer("Будь ласка, спочатку оберіть режим роботи за допомогою команд або меню.")
        return

    city = clean_city_name(message.text)
    if not city:
        await message.answer("Будь ласка, введіть коректну назву міста.")
        return

    if user_data["mode"] == "Поточна погода":
        # Отримання поточної погоди
        status = new_status(city)
        if status.get("cod") != 200:
            await message.answer(f"Помилка: {status.get('message', 'Не вдалося отримати дані')}")
            return

        timestamp = status["dt"]
        normal_date = datetime.fromtimestamp(timestamp)
        weather_info = (f'Погода в місті {status["name"]}, {status["sys"]["country"]}:\n'
                        f'Статус: {status["weather"][0]["description"]}\n'
                        f'Температура: {status["main"]["temp"]}°C\n'
                        f'Відчувається як: {status["main"]["feels_like"]}°C\n'
                        f'Мінімальна: {status["main"]["temp_min"]}°C, Максимальна: {status["main"]["temp_max"]}°C\n'
                        f'Тиск: {status["main"]["pressure"]} гПа\n'
                        f'Вологість: {status["main"]["humidity"]}%\n'
                        f'Актуальний час: {normal_date.strftime("%Y-%m-%d %H:%M:%S")}')
        await message.answer(weather_info)
        await message.answer("Оберіть, що хочете зробити далі:", reply_markup=mode_keyboard)

    elif user_data["mode"] == "Прогноз на 24 години":
    
        status_for_four = new_status_four(city)
        if status_for_four.get("cod") != "200":
            await message.answer(f"Помилка: {status_for_four.get('message', 'Не вдалося отримати дані')}")
            return

        forecast = []
        for i, day in enumerate(status_for_four["list"]):
            day_info = (f'=== +3 години {i + 1} ===\n'
                        f'Дата та час: {day["dt_txt"]}\n'
                        f'Статус: {day["weather"][0]["description"]}\n'
                        f'Температура: {day["main"]["temp"]}°C, Відчувається як: {day["main"]["feels_like"]}°C\n'
                        f'Мінімальна: {day["main"]["temp_min"]}°C, Максимальна: {day["main"]["temp_max"]}°C\n'
                        f'Тиск: {day["main"]["pressure"]} гПа\n'
                        f'Вологість: {day["main"]["humidity"]}%\n'
                        f'Швидкість вітру: {day["wind"]["speed"]} м/с\n'
                        f'Хмарність: {day["clouds"]["all"]}%\n')
            forecast.append(day_info)

        await message.answer("\n\n".join(forecast))
        await message.answer("Оберіть, що хочете зробити далі:", reply_markup=mode_keyboard)

# Головна функція
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
