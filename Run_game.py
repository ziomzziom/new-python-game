# Hangman Game

import random

words = ["apple", "banana", "cherry"]

# Function to pick a random word
def pick_word():
    return random.choice(words)

# Function to check if the letter is in the word
def check_letter(word, letter):
    return letter in word

# Function to check if the player won
def check_win(word, guessed):
    for letter in word:
        if letter not in guessed:
            return False
    return True

# Function to print the hangman
def print_hangman(attempts):
    if attempts == 5:
        print(" ____")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("____|")
    elif attempts == 4:
        print(" ____")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("____|")
    elif attempts == 3:
        print(" ____")
        print(" |  |")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("____|")
    elif attempts == 2:
        print(" ____")
        print(" |  |")
        print(" O  |")
        print("    |")
        print("    |")
        print("____|")
    elif attempts == 1:
        print(" ____")
        print(" |  |")
        print("    |")
        print("    |")
        print("    |")
        print("____|")
    else:
        print(" ____")
        print(" |  |")
        print("    |")
        print("    |")
        print("    |")
        print("____|")

# Main game loop
print("H A N G M A N")
play = True
while play:
    # Pick a random word
    word = pick_word()
    # Create an empty list to store the guessed letters
    guessed = []
    attempts = 6
    playing = True
    while playing:
        # Print the hangman
        print_hangman(attempts)
        # Print the guessed letters
        print("Guessed letters: ", end="")
        for l in guessed:
            print(l, end=" ")
        print()
        # Print the word
        for letter in word:
            if letter in guessed:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print()
        # Get user input
        guess = input("Guess a letter: ")
        # Check if the letter is in the word
        if check_letter(word, guess):
            # Add the letter to the guessed list
            guessed.append(guess)
            print("Correct!")
        else:
            attempts -= 1
            print("Wrong!")
        # Check if the player won
        if check_win(word, guessed):
            print("You won!")
            playing = False
        # Check if the player lost
        if attempts == 0:
            print("You lost!")
            playing = False
    # Ask the player if they want to play again
    again = input("Do you want to play again? (y/n) ")
    if again != "y":
        play = False
        print("Bye!")
