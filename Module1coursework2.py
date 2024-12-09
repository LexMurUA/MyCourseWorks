from colorama import Fore, Back, Style, init
import random
from termcolor import colored
import pygame
import time
import os

PATH = os.path.abspath(os.path.dirname(__file__))
SOUNDS_PATH = os.path.join(PATH, "sounds")



pygame.init()
pygame.mixer.init

init(autoreset=True)

sounds = {
    'wellcome': 'wellcome.mp3',
    'pressure': 'pressure.mp3',
    'question': 'question.mp3',
    'wright': 'wright.mp3',
    'fon': 'fon.mp3',
    'khsm_50-50': 'khsm_50-50.mp3',
    'zal': 'zal.mp3',
    'wrong_answer': 'wrong_answer.mp3'
}
sounds = {key: os.path.join(SOUNDS_PATH, filename) for key, filename in sounds.items()}

def play_sound(sound_name):
    if sound_name in sounds:
        pygame.mixer.music.load(sounds[sound_name])
        pygame.mixer_music.play()



game_storage = {
    "What is the opposite of 'hot'?": "cold",
    "What is the capital of France?": "Paris",
    "What color is the sky on a clear day?": "blue",
    "What is dog?": "animal",
    "What is the first month of the year?": "January",
    "What is the largest planet in our solar system?": "Jupiter",
    "What do bees produce?": "honey",
    "What animal is known as man's best friend?": "dog",
    "What is the largest mammal?": "whale",
    "What metal is liquid at room temperature?": "mercury",
    "What is the primary color of grass?": "green",
    "What gas do plants absorb from the atmosphere?": "carbon",
    "What is the capital of Japan?": "Tokyo",
    "What is H2O?": "water",
    "What fruit is known for its high potassium content?": "banana",
    "What is the color of coal?": "black",
    "What month has Halloween?": "October",
    "What is the largest ocean?": "Pacific",
    "What is the smallest country in the world?": "Vatican",
    "What is the opposite of 'fast'?": "slow",
    "What is the main ingredient in bread?": "flour",
    "What is the name of our galaxy?": "Milkyway",
    "What do chickens lay?": "eggs",
    "What is the currency of the USA?": "dollar",
    "What planet is known as the Red Planet?": "Mars",
    "What do cows produce?": "milk",
    "What is the shape of a stop sign?": "octagon",
    "What is the capital of Ukraine?": "Kyiv",
    "What is the boiling point of water in Celsius?": "100",
    "What is the opposite of 'day'?": "night",
    "What do you call a baby cat?": "kitten",
    "What is the main ingredient in sushi?": "rice",
    "What do spiders build?": "web",
    "What is apple?": "fruit",
    "What is the capital of Canada?": "Ottawa",
    "What is the main language spoken in Brazil?": "Portuguese",
    "What is the color of a ripe banana?": "yellow",
    "What is the opposite of 'happy'?": "sad",
    "What is the chemical symbol for gold?": "Au",
    "What do you call a young dog?": "puppy",
    "What is the capital of Germany?": "Berlin",
    "What is the largest continent?": "Asia",
    "What is the main ingredient in wine?": "grapes",
    "What is the opposite of 'full'?": "empty",
    "What does ice become when it melts?": "water",
    "What is the longest river in the world?": "Nile",
    "What is the capital of Italy?": "Rome",
    "What animal is known for having a long trunk?": "elephant",
    "What is the main ingredient in cheese?": "milk",
    "What is the process of plants making food called?": "photosynthesis",
    "What color is blood?": "red",
    "What instrument has keys and is used in orchestras?": "piano",
    "What is the largest land animal?": "elephant",
    "What is the capital of China?": "Beijing",
    "What do frogs start their life as?": "tadpoles",
    "What is the color of chocolate?": "brown",
    "What animal is known for its spots and speed?": "cheetah",
    "What is the process of turning liquid into gas?": "evaporation",
    "What is the smallest planet in our solar system?": "Mercury",
    "What do we breathe in to survive?": "oxygen",
    "What is the capital of Australia?": "Canberra",
    "What is the opposite of 'soft'?": "hard",
    "What is the main ingredient in pizza?": "dough",
    "What do caterpillars become?": "butterflies",
    "What is the name of Earth's satellite?": "moon",
    "What metal is the Statue of Liberty made of?": "copper",
    "What do you call a group of fish?": "school",
    "What is the main ingredient in beer?": "barley",
    "What is the capital of South Korea?": "Seoul",
    "What is 5 x 5?": "25",
    "What fruit is an apple?": "fruit",
    "What animal is known for its stripes?": "tiger",
    "What is the largest organ in the human body?": "skin",
    "What does a baker make?": "bread",
    "What color is an emerald?": "green",
    "What is the chemical symbol for oxygen?": "O",
    "What do dogs use to bark?": "mouth",
    "What is the opposite of 'up'?": "down",

    "What color is the sun?": "yellow",
    "What do cows eat?": "grass",
    "What is the capital of Mexico?": "Mexico",
    "What is the capital of Egypt?": "Cairo",
    "What gas do humans exhale?": "carbon",
    "What is the capital of the United Kingdom?": "London",
    "What is the color of a lemon?": "yellow",
    "What animal is known for its shell?": "turtle",
    "What is the opposite of 'left'?": "right",
    "What animal is known for being pink?": "flamingo",
    "What is the main ingredient in pancakes?": "flour",
    "What is the capital of Spain?": "Madrid",
    "What is the name of the closest star to Earth?": "Sun",
    "What color are strawberries?": "red",
    "What animal has a pouch?": "kangaroo",
    "What does a blacksmith work with?": "metal",
    "What is the opposite of 'wet'?": "dry",
    "What is the chemical symbol for iron?": "Fe",
    "What do trees release into the air?": "oxygen",
    "What is the main ingredient in soup?": "water",
    "What animal is known for its tusks?": "walrus",
    "What is the opposite of 'young'?": "old",
    "What do birds build to live in?": "nest",
    "What is the currency of Japan?": "yen",
}
 
lies = ["apple", "table", "pencil", "orange", "phone", "book", "sky", "cat", "river", "car",
        "tree", "moon", "cup", "sand", "chair", "flower", "spoon", "bottle", "stone", "grass",
        "shoe", "clock", "water", "hat", "pen", "towel", "candle", "paper", "leaf", "star",
        "frog", "sun", "mask", "egg", "ring", "soap", "fish", "belt", "cloud", "key",
        "bus", "glass", "bread", "coin", "mirror", "bee", "box", "light", "lamp", "star",
        "stick", "radio", "ship", "rose", "fire", "glove", "door", "soil", "ocean", "desk",
        "hill", "milk", "bridge", "shirt", "toy", "flag", "king", "queen", "blanket", "jar",
        "pot", "seed", "lake", "road", "leaf", "piano", "wing", "horn", "cake", "bag",
        "dust", "cloud", "wind", "rope", "wheel", "fence", "ship", "card", "sock", "web",
        "nail", "rope", "dust", "yarn", "coin", "sword", "grape", "bat", "fan", "snow",
        "saw", "face", "page", "bone", "film", "tube", "vine", "pipe", "wave", "foam",
        "mist", "vine", "slug", "game", "wind", "globe", "clock", "line", "plant", "nail",
        "map", "coin", "pearl", "tent", "grip", "shoe", "quiz", "lens", "boot", "ash",
        "horn", "twig", "face", "shell", "log", "seed", "mist", "nut", "wing", "match"]
    
users_data = {}


def random_questions(question, wright_answer, lie1, lie2, lie3):
    numbering = ['1','2','3','4']
    random_choice = [wright_answer, lie1, lie2, lie3]
    random.shuffle(random_choice)
    print(f'{Style.BRIGHT}Question is: {Fore.WHITE}{Style.BRIGHT}{question}\n {Fore.GREEN}{numbering[0]}.{random_choice[0]}; {Fore.YELLOW}{numbering[1]}.{random_choice[1]}; {Fore.MAGENTA}{numbering[2]}.{random_choice[2]}; {Fore.CYAN}{numbering[3]}.{random_choice[3]}\nPress "H" to hint🤫')
    return  {numbering[0] : random_choice[0],
        numbering[1] : random_choice[1],
        numbering[2] : random_choice[2],
        numbering[3] : random_choice[3]
        }    
 
def new_user():
    while True:
        username = input('Enter your username: ').strip() 
        if not username:
            print("Username cannot be empty. Please try again.")
            continue
        elif username in users_data:
            print("This username already exists. Please choose a different username.")
            continue
        else:
            users_data[username] = {'result': 0}
            print(f"Wellcome, {username}!")
            return username
def result_view():
    if users_data == {}:
        print(Fore.CYAN + Style.BRIGHT + 'No users data found.')
        return
    else:
        for name, data in users_data.items():
            print(f'{Fore.MAGENTA}======{Fore.YELLOW}{Style.BRIGHT}{name} - {Fore.GREEN}{Style.BRIGHT}{data["result"]} points{Fore.MAGENTA}======')


    
def game_hub():
    while True:
        play_sound('wellcome')
        print(Fore.CYAN + Style.BRIGHT + '===😀🤩🤑Wellcome to:"Who Wants to Be a Millionaire?"🤑🤩😀===\n'
                    '1-New game🤠\n' 
                    '2-Show result🤓\n'
                    'q-to exit😔\n'
                    '====================')
        choice = input(Fore.MAGENTA + 'Choose an option: ')
        match choice:
            case 'q':
                print(f'{Fore.YELLOW}{Style.BRIGHT}Goodbye!👋')
                break
            case '1':
                name = new_user() 
                attempts_of_mistake = 3
                counter_of_question = 0
                
                while counter_of_question < 10 and attempts_of_mistake > 0:
                    counter_of_question += 1
                    print(f'{Style.BRIGHT}{Fore.YELLOW}Round {counter_of_question}')
                    random_question = random.choice(list(game_storage.keys()))
                    wright_answer = game_storage[random_question]
                    random.shuffle(lies)
                    is_hint_used = False
                    
                    pygame.mixer_music.stop()
                    play_sound('question')
                    while True:
                        wright_answer_number = random_questions(random_question, wright_answer, lies[0],lies[1],lies[2])
                        user_answer = input(Style.BRIGHT + 'Enter your answer:')
                        play_sound('pressure')
                        time.sleep(5)
                        if user_answer == 'h' and not is_hint_used:
                            pygame.mixer_music.stop()
                            play_sound('fon')
                            while True:
                                print('1 - call friend | 2 - 50/50 | 3 - help from the audience')
                                select_hint = input()
                                if select_hint not in ["1", '2','3']:
                                    continue
                                elif select_hint == "1":
                                    pygame.mixer_music.stop()
                                    play_sound('zal')
                                    time.sleep(3)
                                    friend_is_brain = random.randint(1,100)
                                    if friend_is_brain <= 70:
                                        print(f"I think its: {wright_answer}")
                                        time.sleep(2)
                                        pygame.mixer_music.stop()
                                        play_sound('pressure')
                                    else:
                                        print("Sorry i`m stupid")
                                        time.sleep(2)
                                        pygame.mixer_music.stop()
                                        play_sound('pressure')
                                    is_hint_used = True
                                    break
                                elif select_hint == "2":
                                    pygame.mixer_music.stop()
                                    play_sound('khsm_50-50')
                                    time.sleep(3)
                                    rand_chande = random.choice([lies[2],lies[0]])
                                    print(f"We can hide next answers:{lies[1]} and {rand_chande}")
                                    time.sleep(1)
                                    pygame.mixer_music.stop()
                                    play_sound('pressure')
                                    is_hint_used = True
                                    break
                                elif select_hint == "3":
                                    pygame.mixer_music.stop()
                                    play_sound('zal')
                                    time.sleep(3)
                                    audience = ['For sure','Maybe','Impossible']
                                    random.shuffle(audience)
                                    print(f'{Fore.RED}{lies[0]}-{audience[0]}; {wright_answer}-We doubt; {lies[1]}-{audience[1]}; {lies[2]}-{audience[2]}')
                                    time.sleep(2)
                                    pygame.mixer_music.stop()
                                    play_sound('pressure')
                                    is_hint_used = True
                                    break
                        elif user_answer not in ['1','2','3','4']:
                            print(f'{Fore.RED}Invalid input. Please enter a number from 1 to 4.')
                            pygame.mixer_music.stop()
                            play_sound('question')
                            continue
                        elif wright_answer_number[user_answer] != wright_answer:
                            attempts_of_mistake -= 1
                            pygame.mixer_music.stop()
                            print(f'{Fore.RED}Wrong answer. You have {attempts_of_mistake} attempts left.')
                            play_sound('wrong_answer')
                            time.sleep(3) 
                            pygame.mixer_music.stop()
                            break                          
                        else:
                            pygame.mixer_music.stop()  
                            print(f'{Fore.GREEN}{Style.BRIGHT}Congratulations, you got it right!')
                            play_sound('wright')
                            users_data[name]['result'] += 100000
                            print(f'{Fore.YELLOW}{Style.BRIGHT}{users_data}')
                            time.sleep(3) 
                            pygame.mixer_music.stop()
                            break
                if attempts_of_mistake == 0:
                    print(f'{Fore.RED}{Style.BRIGHT}Game Over! You used all attempts.')
                else:
                    if users_data[name]['result'] < 1000000:
                        print(f'{Fore.GREEN}{Style.BRIGHT}Congratulations, you have won a lot of money!') 
                    else:
                        pygame.mixer_music.stop()
                        play_sound('wellcome')
                        print(f'{Fore.GREEN}{Style.BRIGHT}🥳🥳🥳Congratulations, you have become a millionaire!🥳🥳🥳')    
                print(f'{Fore.YELLOW}Your final score: {users_data[name]["result"]}')
            case '2':
                result_view()                



Millionaire = game_hub()
