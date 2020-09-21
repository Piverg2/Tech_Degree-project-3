import random


# This Class diplays the Phrase, checks the letters, and checks if phrase is complete
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.clue_received = 0
    
    
    def display(self, guess):
        for letter in self.phrase: 
            if letter in guess:
                print(f"{letter}", end = " ")
            elif letter != " ":
                print('_', end= " ")
            else:
                print(end=" ")


    def check_guess(self, guess):
            if guess in self.phrase:
                return True
            else:
                return False
    
    
    def return_clue(self, guess):
        self.clue_received += 1
        for letter in self.phrase:
            if letter not in guess:
                print(f"\nTry this Free Letter: '{(letter)}'\n", end = " ")
                break


    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True