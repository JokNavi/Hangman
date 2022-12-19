import random
from Graphics import Grid, push_up


special_word = str()
# The word that was generated at the beggining of the game. if this word is found before the hangman dies the game ends

wrong_guesses = list()
# List of all the guesses made that weren't correct. Contains both letters and words.


def contains_letter_check():
    '''Checks if the chosen word contains the selected letter.'''
    pass


def generate_word():
    '''Picks a word from a list of a bunch of possible words'''
    with open(r'Project/Possible words.txt', "r") as f:
    # Open the file containing random words used in hangman.
        possible_words = [word.strip().lower() for word in f.readlines()]
        # Read the file and strip the newline and captital letters from each word.
        global special_word
        special_word = random.choice(possible_words)
        # Set the global variable special_word to a random word from the possible words list.


def main_program():
    '''The main game loop. Handles the main logic of the game. Such as scores and the word to look for.'''
    pass


if __name__ == "__main__":
    SIZE = 20
    HangmanScreen = Grid(SIZE*3, SIZE)

    #push_up(20)

    # HangmanScreen.print_grid()
    generate_word()
    print(special_word)
