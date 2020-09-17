import phrase
# Create your Game class logic in here.
class Game():
    def __init__(self, missed, phrases, active_phrase, guesses):
        self.missed = missed
        self.phrases = phrases
        self.active_phrases = active_phrase
        self.guesses = guesses

    def start():
        # Calls the welcome method, creates the game loop, calls the get_guess method, adds the user's guess to guesses, increments the number of missed by one if the guess is incorrect, calls the game_over method.
        pass
    def get_random_phrase():
        # this method randomly retrieves one of the phrases stored in the phrases list and returns it.
        pass
    def welcome():
        # this method prints a friendly welcome message to the user at the start of the game
        pass
    def get_guess():
        # this method gets the guess from a user and records it in the guesses attribute
        pass
    def game_over():
        # this method displays a friendly win or loss message and ends the game.
        pass