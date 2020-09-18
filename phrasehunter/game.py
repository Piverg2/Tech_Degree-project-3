import random

from phrasehunter.phrase import Phrase
# Create your Game class logic in here.
class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase('Hello world'),
            Phrase('Just keep swimming'),
            Phrase('Get to the chopper'),
            Phrase('There is no place like home'),
            Phrase('May the force be with you')
            ]
        self.active_phrases = self.get_random_phrase()
        self.guesses = []


    def start(self):
        self.welcome()
        while self.missed < 5 and self.active_phrases.check_complete(self.guesses) == False:
            print("\nNumber missed: ", self.missed)
            self.active_phrases.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            # print(self.active_phrases.display(self.guesses))
            self.active_phrases.check_guess(user_guess)
            if not self.active_phrases.check_guess(user_guess):
                self.missed += 1
        self.game_over()
        self.play_again()

    def welcome(self):
        print("\n********************************")
        print("Welcome to WHEEL.OF.FORTUNE!!!!!")
        print("********************************\n")


    def get_random_phrase(self):
        return random.choice(self.phrases)
    

    def get_guess(self):
        # this method gets the guess from a user and records it in the guesses attribute
        while True:
            try: 
                guess = input('\nGuess a letter: ')
                # Googled how to check if input is a number: https://www.w3schools.com/python/ref_string_isnumeric.asp#:~:text=The%20isnumeric()%20method%20returns,considered%20to%20be%20numeric%20values.
                if guess.isnumeric():
                    raise ValueError("\nThis phrase only contains letters")
                elif len(guess) > 1:
                    raise ValueError("\nOne letter at a time please!")
                
            except ValueError as err:
                print(err)
                print("Try again!")
                
            else: 
                return guess


    def game_over(self):
        # this method displays a friendly win or loss message and ends the game.
        if self.missed == 5:
            print("\nNumber missed: ", self.missed)
            print("\nSorry, you ran out of guesses! Better luck next time!")
            print("\nThe correct phrase was: {}\n".format(self.active_phrases.phrase))
        elif self.active_phrases.check_complete(self.guesses) == True:
            print("Horray! You guessed the Phrase! You Win!!")
    
    
    def play_again(self):
        play_again = input("Would you like to play again? (Y/N) ")
        if play_again.lower() == "y":
            # resets the game
            self.__init__()
            # statrs it upon reset
            self.start()
        else:
            print("\nThanks for playing!")
