from art import tprint
from sys import exit
import random

tprint("Guess it",font="isometric1")

#assests
def generate_Quest():
    languages = ['Python','C','C++','Java','Rust','Javascript','HTML']
    description = [ 'The language is user friendly and is used mostly for automation',
                    'The language is developed by late Denis Ritchie and mostly used unix based for systems',
                    'The language is used mainly for game development and is used as the language in Unity Game Engine',
                    'The language is developed by James Gosling and is used mainly for application development',
                    'The fastest static and compiled programming language mainly used for embedded software development',
                    'The language is manly used for web development with HTML and CSS',
                    'The web development language that is not actually a programming language']
    dict_chooser = {}
    for i in range(len(languages)):
        dict_chooser[languages[i]] = description[i]
    selected = random.choice(languages)
    return selected,dict_chooser[selected]
def update(secret_word,clue,guess):
    for i in range(len(clue)):
        if secret_word[i] == guess:
            clue[i] = guess
    return clue

def play():
    lives = 3
    secret_word,description = generate_Quest()
    clue = ['?' for i in range(len(secret_word))]
    win = False
    while lives > 0:

        print('Lives Remaining ->','*'*lives)
        print()
        print('Clue ===> ',clue)
        print('Hint <=>',description)
        character_or_word = input('Guess a character or the whole secret_word :)-> ')

        if character_or_word in secret_word:
            clue = update(secret_word,clue,character_or_word)
        elif character_or_word == secret_word:
            win = True
        else:
            print('Your guess is incorrect!','Please Try Again')
            lives -= 1

        if ''.join(clue) == secret_word:
            win = True

        if win is True:
            print('Congratulation! You won the game')
            ask = input('Wanny play again Y/N?')
            if ask.lower() == 'y':
                play()
            else:
                print('Arigato Gozaimasu','FAREWELL FAREWELL FAREWELL')
                exit()
    else:
        print('Sorry You Lost the Game')
        print('The correct secret word is ',secret_word)
        ask = input('Do you want to play again? Y/N')
        if ask.lower() == 'y':
            play()
        else:
            print('Thanks for your participation')
            exit()
play()
