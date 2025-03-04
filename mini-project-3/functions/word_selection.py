import random

def choose_word():
    """
    Selects a random word from a predefined list.
    """
    word_list = ["python", "developer", "hangman", "programming", "challenge"]
    return random.choice(word_list)
