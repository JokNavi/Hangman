import random
from Graphics import Grid, push_up


special_word = str()
# The word that was generated at the beggining of the game. if this word is found before the hangman dies the game ends

shown_word = list()
# List containing all the correctly guessed letters and empty slot placeholders.

wrong_guesses = list()
# List of all the guesses made that weren't correct. Contains both letters and words.

def good_guess():
    '''Contains the logic for when the guess was correct. Will update the shown_word global variable and check if the word is found yet.'''
    pass


def bad_guess(user_choice):
    '''Contains the logic for when the guess was wrong. Will update the hangman display.'''
    global wrong_guesses
    wrong_guesses.append(user_choice)
    # Append the wrong characters to the global list; wrong_guesses.
    match len(wrong_guesses):
    # Check how many wrong guesses are now in the list and update the hangman visual accordingly.         
        case 1:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 2.txt")
        case 2:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 3.txt")
        case 3:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 4.txt")
        case 4:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 5.txt")
        case 5:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 6.txt")
        case 6:
            HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 7.txt")
            print("RIP; Too many wrong guesses. You let the hangman die...")
            exit(0)
            # Close the game if the hangman is completed.
        case _:
            print("Invalid bad guesses amount. Closing program.")
            exit(-1)
    pass


def contains_letter_check():
    '''Checks if the chosen word contains the selected letter. Can check words'''
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

    generate_word()
    print(f"Generated word: \"{special_word.capitalize()}\"")

    push_up(20)

    HangmanScreen.load_picture_file(0, 2, "H-Line.txt")
    HangmanScreen.load_picture_file(0, 0, "H-Line.txt")
    HangmanScreen.load_picture_file(0, 2, "V-Line.txt")
    HangmanScreen.load_picture_file(29, 2, "V-Line.txt")
    HangmanScreen.load_picture_file(10, 9, "Dead Guy\Character 1.txt")
    #bad_guess()
    HangmanScreen.print_grid()


if __name__ == "__main__":
    SIZE = 10
    HangmanScreen = Grid(SIZE*3, SIZE)

    main_program()

  