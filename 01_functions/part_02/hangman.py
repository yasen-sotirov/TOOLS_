"""
Hangman
Let's create a console version of the popular game Hangman.
Create a directory named Hangman and create an empty main.py file in it.
The application should be able to perform the following tasks:
1. Read a word from the console.
1. Print hidden and guessed letters. For example, the word hangman should be printed as h-----n initially.
1. Check if the player has remaining attempts.
1. Accept next guessed letter.
1. Check if that letter exists in the word or not:
1. If yes - Reveal the position of the letter. For example, if the player guesses g from the word hangman,
then print h--g--n. (Assuming no other letters are guessed)
2. If no - decrease the number of attempts remaining and print them.
1. Check for win (all letters are guessed) or loss (no attempts remaining)
"""


def get_word():
    secret_word = input("write secret word:")
    secret_word = secret_word.lower()
    for el in secret_word:
        if el.isnumeric():
            return "The word must contain only letters"
    return secret_word


def get_initial_positions(position):
    number_of_letters = len(position)
    lst = [] * number_of_letters


def hide_word(guessed_letter, secret_word):
    guessed_letter = input()
    if guessed_letter.isnumeric():
        return "Please guess a letter"

    if guessed_letter in secret_word:
        for index, letter in enumerate(secret_word):
            pass

