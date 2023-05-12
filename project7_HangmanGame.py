import random
import hangman_art
import hangman_words
from replit import clear

print(hangman_art.logo + "\n")
end_of_game = False
# generate the random word
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
live = 7

# ask the letter and feedback
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #Check guessed letter
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                index = i
                display[i] = guess
        #Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")
        print("Your live state is: \n" + hangman_art.stages[7 - live])
    else:
        live -= 1
        if live > 1:
            print(f"{' '.join(display)}")
            print("Your guess is wrong. Please do it again!")
            print("Your live state is: \n" + hangman_art.stages[7 - live])
        else:
            print("Your live state is: \n" + hangman_art.stages[7 - live])
            print("You die.")
            print("The chosen word is: " + chosen_word)
            end_of_game = True

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
