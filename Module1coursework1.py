from colorama import Fore, Back, Style, init
import random
import pyjokes
from deep_translator import GoogleTranslator
from termcolor import colored

init(autoreset=True)

my_library = {
    "films": {
        "action": [
            "Die Hard", "Mad Max: Fury Road", "John Wick", "Gladiator", 
            "The Dark Knight", "Inception", "The Matrix", "Kill Bill", 
            "Terminator 2", "Léon: The Professional", "Casino Royale", 
            "Mission: Impossible", "Heat", "Taken", "Speed"
        ],
        "comedy": [
            "Superbad", "The Hangover", "Dumb and Dumber", "Anchorman", 
            "Step Brothers", "Ferris Bueller's Day Off", "Groundhog Day", 
            "Bridesmaids", "Napoleon Dynamite", "Zoolander", "The Grand Budapest Hotel", 
            "Mean Girls", "Pineapple Express", "Hot Fuzz", "Tropic Thunder"
        ],
        "horror": [
            "The Exorcist", "A Nightmare on Elm Street", "Halloween", 
            "The Shining", "Hereditary", "The Babadook", "Get Out", 
            "Paranormal Activity", "The Conjuring", "It Follows", 
            "The Texas Chain Saw Massacre", "Scream", "The Ring", 
            "Saw", "The Witch"
        ]
    },
    "music": {
        "rock": [
            "Stairway to Heaven", "Bohemian Rhapsody", "Hotel California", 
            "Smoke on the Water", "Sweet Child O' Mine", "Highway to Hell", 
            "Born to Be Wild", "Eye of the Tiger", "Paint It Black", 
            "Dream On", "We Will Rock You", "Free Bird", 
            "Back in Black", "Comfortably Numb", "Thunderstruck"
        ],
        "hip-hop": [
            "Lose Yourself", "Juicy", "N.Y. State of Mind", "Dear Mama", 
            "Hypnotize", "99 Problems", "C.R.E.A.M.", "Alright", 
            "Mo Money Mo Problems", "Hotline Bling", "HUMBLE.", 
            "Sicko Mode", "In Da Club", "Gold Digger", "Work It"
        ],
        "pop": [
            "Thriller", "Like a Prayer", "Billie Jean", "Rolling in the Deep", 
            "Shape of You", "Uptown Funk", "Poker Face", "Firework", 
            "Bad Guy", "Sorry", "Levitating", "Can't Stop the Feeling!", 
            "All of Me", "Havana", "Blinding Lights"
        ]
    },
    "games": {
        "shooter": [
            "Call of Duty", "Counter-Strike", "Fortnite", "Overwatch", 
            "Battlefield", "Halo", "Rainbow Six Siege", "Doom", 
            "Apex Legends", "Destiny", "Quake", "Team Fortress 2", 
            "PUBG", "Valorant", "Gears of War"
        ],
        "role-playing": [
            "The Witcher 3", "Final Fantasy VII", "Skyrim", 
            "Persona 5", "Mass Effect", "Dragon Age", "Fallout", 
            "Dark Souls", "Bloodborne", "Cyberpunk 2077", 
            "Elder Scrolls Online", "Baldur's Gate", "Chrono Trigger", 
            "Divinity: Original Sin 2", "Pokémon"
        ],
        "sports": [
            "FIFA", "NBA 2K", "Madden NFL", "MLB The Show", 
            "Tony Hawk's Pro Skater", "Rocket League", "PGA Tour", 
            "NHL", "WWE 2K", "Skate", "Top Spin", "Fight Night", 
            "Virtua Tennis", "Gran Turismo", "Forza Motorsport"
        ]
    },
    "books": {
        "fiction": [
            "George Orwell: 1984", "F. Scott Fitzgerald: The Great Gatsby", 
            "Harper Lee: To Kill a Mockingbird", "J.K. Rowling: Harry Potter and the Sorcerer's Stone", 
            "Jane Austen: Pride and Prejudice", "Mark Twain: The Adventures of Huckleberry Finn", 
            "Ernest Hemingway: The Old Man and the Sea", "Gabriel Garcia Marquez: One Hundred Years of Solitude", 
            "J.D. Salinger: The Catcher in the Rye", "F. Dostoevsky: Crime and Punishment", 
            "Toni Morrison: Beloved", "Kurt Vonnegut: Slaughterhouse-Five", 
            "Margaret Atwood: The Handmaid's Tale", "Charles Dickens: Great Expectations", 
            "Leo Tolstoy: War and Peace"
        ],
        "non-fiction": [
            "Malcolm Gladwell: Outliers", "Michelle Obama: Becoming", 
            "Stephen Hawking: A Brief History of Time", "Yuval Noah Harari: Sapiens", 
            "James Clear: Atomic Habits", "Mark Manson: The Subtle Art of Not Giving a F*ck", 
            "Brené Brown: Daring Greatly", "Sheryl Sandberg: Lean In", 
            "Daniel Kahneman: Thinking, Fast and Slow", "Bill Bryson: A Short History of Nearly Everything", 
            "Viktor Frankl: Man's Search for Meaning", "Carl Sagan: Cosmos", 
            "Noam Chomsky: Manufacturing Consent", "Angela Duckworth: Grit", 
            "Elizabeth Gilbert: Eat, Pray, Love"
        ],
        "fantasy": [
            "J.R.R. Tolkien: The Hobbit", "C.S. Lewis: The Chronicles of Narnia", 
            "J.K. Rowling: Harry Potter and the Prisoner of Azkaban", "George R.R. Martin: A Game of Thrones", 
            "Philip Pullman: Northern Lights", "Brandon Sanderson: Mistborn", 
            "Neil Gaiman: American Gods", "Terry Pratchett: The Colour of Magic", 
            "Ursula K. Le Guin: A Wizard of Earthsea", "Patrick Rothfuss: The Name of the Wind", 
            "Rick Riordan: The Lightning Thief", "Robert Jordan: The Eye of the World", 
            "N.K. Jemisin: The Fifth Season", "Anne Rice: Interview with the Vampire", 
            "Madeleine L'Engle: A Wrinkle in Time"
        ]
    },
    '1': 'action',
    '2': 'comedy',
    '3': 'horror',
    '4': 'rock',
    '5': 'hip-hop',
    '6': 'pop', 
    '7': 'shooter',
    '8': 'role-playing',
    '9': 'sports', 
    '10': 'uk',
    '11': 'fr',
    '12': 'de',
    '13': 'es',
    '14': 'en',
    '15': "fiction",
    '16': "non-fiction",
    '17': "fantasy",
    '18': 'rock',
    '19': 'paper',
    '20': 'scissors',
    'elements': ['rock', 'paper', 'scissors']
}

def random_platform(text, genre):
    print(Style.BRIGHT + Fore.GREEN + f'===> {text}: {random.choice(genre)} <===')
    
def filming():
    while True:
        choice = input(Style.BRIGHT + 'Choose genre: 1-action;2-comedy;3-horror:')
        if choice in ['1','2','3']:
            print(my_library[choice])
            genre = my_library[choice]
            random_platform('Here random film for you' , my_library['films'][genre] )
            break
        else:
            print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')
            
def musicing():
    while True:
        choice = input(Style.BRIGHT + 'Choose genre: 4-rock;5-hip-hop;6-pop:')
        if choice in ['4','5','6']:
            print(my_library[choice])
            genre = my_library[choice]
            random_platform('Here random music for you' , my_library['music'][genre] )
            break
        else:
            print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')
            
def gaming():
     while True:
        choice = input(Style.BRIGHT + 'Choose genre: 7-shooter;8-role-playing;9-sports:')
        if choice in ['7','8','9']:
            print(my_library[choice])
            genre = my_library[choice]
            random_platform('Here random game for you' , my_library['games'][genre] )
            break
        else:
            print('Invalid choice. Please try again.😔')

def booking():
    while True:
        choice = input(Style.BRIGHT + 'Choose genre: 15-fiction;16-non-fiction;17-fantasy:')
        if choice in ['15','16','17']:
            print(my_library[choice])
            genre = my_library[choice]
            random_platform('Here random book for you' , my_library['books'][genre] )
            break
        else:
            print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')

def joking():
      while True:
        jokes = pyjokes.get_jokes()
        random_platform('Here random joke 😂' , jokes)
        break

def translating():
    while True:
        original_language =input(Style.BRIGHT + 'Enter original language: 10-Uk;11-Fr;12-Ge;13-Sp;14-En:')
        if original_language in ['10','11','12','13','14']:
            original_language = my_library[original_language]
            word = input(Style.BRIGHT + 'Enter word or sentence to translate:')
            language_translated = input(Style.BRIGHT + 'Enter language translated: 10-Uk;11-Fr;12-Ge;13-Sp;14-En:')
            if language_translated in ['10','11','12','13','14']:
                language_translated = my_library[language_translated]
                translated_word = GoogleTranslator(source=original_language, target=language_translated).translate(word)
                print(Style.BRIGHT + Fore.GREEN + f'===>Here your translate on {language_translated}:{translated_word}<===')
                break  
            else:
                print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')
        else:
            print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')
    
def summing(num1, num2): 
    return num1 + num2

def difference(num1, num2): 
    return num1 - num2

def multiplication(num1, num2): 
    return num1 * num2

def division(num1, num2): 
    return ("Division by zero is not allowed") if num2 == 0 else num1 / num2

def calculating():
    while True:
        print(Fore.BLUE + '======Welcome to calculator!🤓======\n'
                'Choose operation:\n'
                '1 to calculate\n'
                '2 to Exiting calculation')
        try:
            operation = input(Style.BRIGHT + 'Enter your choose:')
            if operation == '2':
                print(Style.BRIGHT + Fore.RED + 'Exiting...')
                break
            elif operation == '1':
                    print(Fore.BLUE + 'Let\'s calculate!')
                    num1 = float(input(Style.BRIGHT + 'Enter number:'))
                    operation = input(Style.BRIGHT + 'enter operation(+,-,*,/):')
                    if operation not in ['+','-','*','/']:
                        print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.')
                    else:
                        num2 = float(input(Style.BRIGHT + 'Enter number:'))
                        match operation:
                            case '+':
                                result = summing(num1, num2)
                                print(Style.BRIGHT + Fore.GREEN + f'Result:{num1} + {num2} = {result}')
                            case '-':
                                result = difference(num1, num2)
                                print(Style.BRIGHT + Fore.GREEN + f'Result:{num1} - {num2} = {result}')
                            case '*':
                                result = multiplication(num1, num2)
                                print(Style.BRIGHT + Fore.GREEN + f'Result:{num1} * {num2} = {result}')
                            case '/':
                                result = division(num1, num2)
                                print(Style.BRIGHT + Fore.GREEN + f'{result}')                        
            else:
                print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.')
        except:
            ValueError
            print(Style.BRIGHT + Fore.RED + 'Invalid input. Please try again.')
def game_space():
    while True:
        print(Style.BRIGHT + Fore.YELLOW + '======Hello, welcome to The Game!=====')
        choice = input(Style.BRIGHT + 'Enter your choice(18-rock;19-paper;20-scissors;q-to exit):')
        if choice == 'q':
            break
        elif choice in ['18','19','20']:
            user_choice = my_library[choice] 
            computer_choice = random.choice(my_library['elements'])
            if user_choice == computer_choice:
                print('It\'s a tie!')
            elif (user_choice == 'rock' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice =='scissors') or \
            (user_choice =='scissors' and computer_choice == 'rock'):
                print(Style.BRIGHT + Fore.GREEN + f'===> You choose {user_choice} and computer choose {computer_choice}-You lose!😔 <===')
            else:
                print(Style.BRIGHT + Fore.RED + f'===> You choose {user_choice} and computer choose {computer_choice}-You win <===')
        else:
            print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')    

def game_hub():
    while True:
        print(Fore.YELLOW + '======Hello, wellcome to The Game assistant!😜=====\n'
                    'How can I help?\n'
                    '1-Film recommendation\n' 
                    '2-Music recommendation\n'
                    '3-Games recommendation\n'
                    '4-Books recommendation\n'
                    '5-Jokes\n'
                    '6-Play game(rock,paper,scissors)\n'
                    '7-Translater\n'
                    '8-calculater\n'
                    'q-to exti\n'
                    '====================')
        choice = input(Style.BRIGHT + 'Choose an option:')
        match choice:
            case 'q':
                print(colored('Goodbye!', 'green'))
                break
            case '1':
                filming()
            case '2':
                musicing()
            case '3':
                gaming()
            case '4':
                booking()
            case '5':
                joking()
            case '6':
                game_space()
            case '7':
                translating()
            case '8':
                calculating() 
            case _ :
                print(Style.BRIGHT + Fore.RED + 'Invalid choice. Please try again.😔')
                                   







game_hub()
