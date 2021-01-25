# This script creates a hangman game

from random_words import RandomWords


def game():
    # Generate a random word and print underscores
    rw = RandomWords()
    word = rw.random_word()
    # print(word)
    # Display underscores
    underscores = "{word}".format(word=len(word) * "_")
    print(underscores)
    under = list(underscores)
    # Get player's guess and print
    h = 6
    while h != 0:
        guess = input('Guess a letter : ')
        # If player guesses letter correctly, get index and replace underscore
        if guess in word:
            print("Nice !")
            indices = list()
            for i, x in enumerate(word):
                if x == guess:
                    indices.append(i)
            for index in indices:
                under[index] = guess
                underscores = " "
                print(underscores.join(under))
            if underscores.join(under).replace(" ", "") == word:
                print("Congratulations !!! You have guessed the word !!!!")
                break
        else:
            # If player guesses incorrectly, they lose one try
            h = h - 1
            if h == 0:
                print("Sorry! You lost the game!")
                print("The word was {}".format(word))
            else:
                print("Yikes! Try again!")
                print(underscores.join(under))


if __name__ == '__main__':
  game()
