import random
from functions.word_selection import choose_word
from functions.display import display_word
from functions.input_handler import get_guess


def hangman():
    """
    Runs the Hangman game loop.
    """
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")

    while incorrect_guesses < max_attempts:
        print("\nCurrent word:", display_word(word, guessed_letters))
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print("Incorrect guesses remaining:", max_attempts - incorrect_guesses)

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    print("\nGame over! The word was:", word)


if __name__ == "__main__":
    hangman()
