import random
from functions.word_selection import choose_word
from functions.display import display_word
from functions.get_guess import get_guess

def get_difficulty():
    """
    Prompts the player to select a difficulty level.
    """
    difficulty_levels = {
        # Longer words, more attempts
        "easy": (8, 8),
        # Balanced difficulty
        "medium": (6, 6),
        # Shorter words, fewer attempts
        "hard": (4, 4)
    }

    while True:
        choice = input("\nChoose difficulty (easy, medium, hard): ").lower()
        if choice in difficulty_levels:
            return difficulty_levels[choice]
        print("Invalid choice. Please select easy, medium, or hard.")


def hangman():
    """
    Run the Hangman game loop.
    """

    print("Welcome to Hangman!")
    word_length, max_attempts = get_difficulty()
    word = choose_word(word_length)
    guessed_letters = set()
    incorrect_guesses = 0

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
