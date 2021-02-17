__author__ = 'varuna'

"""
This script runs a hangman game. 
Steps:
    1. import the RandomWords package
    2. generate a random word using the package
    3. replace letters in word by underscores and display to user 
    4. get the user's guess
        a. if the guess is correct, get the index of the letter in the word and replace underscore with the guess
        b. if the guess is incorrect, player loses one try
    5. game ends when word is guessed, or when number of tries equals zero
"""

from random_words import RandomWords


def get_word():
    """
    picks a random word from the random words package and stores in a variable
    """
    rw = RandomWords()
    word = rw.random_word()
    return word


def hide(word):
    """
    takes a word as input and replaces the letters with underscores
    :param word: string that needs to be hidden
    :return: word hidden by underscores
    """
    # Replace letters with underscore and store in a list
    underscore_list = list(len(word) * "_")
    # Format underscores into string to improve visualization
    x = " "
    hidden_word = x.join(underscore_list)
    # Display underscores
    print(hidden_word)


def game(n):
    """
    Main script that runs the hangman game.
    :param n: number of tries
    :return: player's progress
    """
    # generate word
    secret_word = get_word()
    # display underscores
    hide(secret_word)
    # store progress inside a list
    underscore_list = list(len(secret_word) * "_")
    # main loop that runs the game until all tries used or word is guessed
    while n != 0:
        # Get player's input
        players_guess = input('Guess a letter : ')
        try:
            # handle inputs that are not strings
            if not players_guess.isalpha():
                raise ValueError
        except ValueError:
            print("You can't guess a number in a word ! Try again!")
            continue
        # create string to display progress to the user
        x = " "
        if players_guess in secret_word:
            print("Nice !")
            # get the index of letter guessed
            indices = list()
            for location, letter in enumerate(secret_word):
                if letter == players_guess:
                    indices.append(location)
            # from the index, add the guessed letter into the hidden word and print
            for index in indices:
                underscore_list[index] = players_guess
                print(x.join(underscore_list))
            # if all the letters guessed match the secret word, player won game
            if x.join(underscore_list).replace(" ", "") == secret_word:
                print("Congratulations, you won the game !!!")
                exit()
        else:
            # If player guesses incorrectly, they lose one try
            n -= 1
            # if all the tries have been used, game over
            if n == 0:
                print("Sorry! You lost the game!")
                print("The word was {}".format(secret_word))
                exit()
            # if player has remaining tries, continue
            else:
                print("Sorry! Try again!")
                print(x.join(underscore_list))


if __name__ == '__main__':
    game(6)


