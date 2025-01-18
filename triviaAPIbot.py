import requests
import random
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command

API_TOKEN = 'Token'
url = 'https://the-trivia-api.com/v2/questions'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
user_state = {}


def new_question():
    query_param = {
        'limit': 1,
        'categories': random.choice([
            'music', 'sport_and_leisure', 'film_and_tv',
            'arts_and_literature', 'history', 'society_and_culture',
            'science', 'geography', 'food_and_drink', 'general_knowledge'
        ]),
        'difficulties': random.choice(['easy', 'hard', 'medium'])
    }
    res = requests.get(url, params=query_param)
    if res.status_code == 200:
        return res.json()[0]
    else:
        return None

@dp.message(Command('start'))
async def send_welcome(message:Message):
    await message.answer("Hello! Let's check your knowledge:\n"
                         "Press 'Start game' to begin or 'Exit' to stop.",
                         reply_markup=ReplyKeyboardMarkup(
                             keyboard=[[KeyboardButton(text="Start game"), KeyboardButton(text="Exit")]],
                             resize_keyboard=True
                         ))

@dp.message(lambda message: message.text == "Start game")
async def start_game(message:Message):
    question = new_question()
    if not question:
        await message.answer("Failed to get a question. Try again later.")
        return
    else:
        answers = question["incorrectAnswers"] + [question["correctAnswer"]]
        random.shuffle(answers)
        user_state[message.from_user.id] = {
            "question": question["question"]["text"],
            "correct_answer": question["correctAnswer"],
            "answers": answers
        }
        
        answer_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=answer)] for answer in answers] + [[KeyboardButton(text="Exit")]],resize_keyboard=True)
        await message.answer (f'{question["question"]["text"]}', reply_markup=answer_keyboard)


@dp.message(lambda message: message.from_user.id in user_state)
async def handle_answer(message: Message):
    user_data = user_state.get(message.from_user.id)
    if not user_data:
        await message.answer("Please start the game first",reply_markup=ReplyKeyboardMarkup(
                             keyboard=[[KeyboardButton(text="Start game"), KeyboardButton(text="Exit")]],
                             resize_keyboard=True))
        return
    elif message.text == "Exit":
        await exit_game(message)
        return
    elif message.text == user_data["correct_answer"]:
        await message.answer("🎉 Correct! Here's the next question:")
    else:
        await message.answer(f"❌ Wrong! The correct answer is: {user_data['correct_answer']}")   
    
    await start_game(message)

@dp.message(lambda message: message.from_user.id == "Exit")
async def exit_game(message:Message):
    await message.answer('Goodbay!')
    user_state.pop(message.from_user.id, None)
    await message.answer("Thanks for playing! See you next time.", reply_markup=ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="/start")]],
        resize_keyboard=True
    ))


if __name__ == "__main__":
    import asyncio
    asyncio.run(dp.start_polling(bot))