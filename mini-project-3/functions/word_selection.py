import random

def choose_word(min_length=0):
    """
    Selects a random word from a predefined list based on the minimum length.
    """
    word_list = [
        "python", "developer", "hangman", "programming", "challenge",
        "code", "script", "debug", "variable", "function", "arrays", "loops"
    ]

    # Filter words based on minimum length (for difficulty levels)
    filtered_words = [word for word in word_list if len(word) >= min_length]

    # If no words match the criteria, fall back to the full list
    return random.choice(filtered_words) if filtered_words else random.choice(word_list)

