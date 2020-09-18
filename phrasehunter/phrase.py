# This Class diplays the Phrase, checks the letters, and checks if phrase is complete
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()


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
    

    def check_complete(self, guesses):
        if len(guesses) == len(self.phrase):
            return True
        else:
            return False