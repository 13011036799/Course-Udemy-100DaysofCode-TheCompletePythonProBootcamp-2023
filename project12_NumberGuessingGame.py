#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def generator():
    print("I'm thinking of a number between 1 and 100.")
    global number
    number = random.randint(1,100)
    print(f"Pssst, the correct answer is {number}")

def choose_level():
    global chance
    loop = True
    while loop:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if level=="easy":
            chance = 10
            loop = False
        elif level=="hard":
            chance = 5
            loop = False
        else:
            print("Your input is wrong. Please try again.")

def guess(chance):
    for i in range(chance):
        guess = int(input("Make a guess: "))
        remain = 4-i
        if guess == number:
            print(f"You got it! The answer was {guess}")
            return 
        elif guess < number:
            print(f"Too low.")
            if remain == 0:
                print(f"You have {4-i} attempts remaining to guess the number.\nGame over!")
            else:
                print(f"Guess again.\nYou have {4-i} attempts remaining to guess the number.")
        elif guess > number:
            print(f"Too high.")
            if remain == 0:
                print(f"You have {4-i} attempts remaining to guess the number.\nGame over!")
            else:
                print(f"Guess again.\nYou have {4-i} attempts remaining to guess the number.")

def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")  
    generator()
    choose_level()
    print(f"You have {chance} attempts remaining to guess the number.")
    guess(chance)

play_game()

# -------------------------------------------------------
# art.py
logo = '''
   ______                        __  __            _   __                __                 
  / ____/_  _____  __________   / /_/ /_  ___     / | / /_  ______ ___  / /_  ___  _____    
 / / __/ / / / _ \/ ___/ ___/  / __/ __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/    
/ /_/ / /_/ /  __(__  |__  )  / /_/ / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /        
\____/\__,_/\___/____/____/   \__/_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/         
'''
