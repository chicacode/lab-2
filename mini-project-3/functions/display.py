def display_word(word, guessed_letters):
    """
    Displays the word with guessed letters revealed and unguessed letters as underscores.
    """
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)
