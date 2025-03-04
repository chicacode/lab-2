def get_guess(guessed_letters):
    """
    Prompts the player to enter a letter, ensuring it's a valid single character not guessed before.
    """
    while True:
        guess = input("\nGuess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            return guess
        print("Invalid input. Please enter a single, new letter.")
