"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""
import os
import random

import exercise1


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("A number between ? and _ ?")
    print("lower bound:")
    #lowerBound = input("Enter an lower bound: ")
    lowerBound = 0
    low = exercise1.not_number_rejector (lowerBound)

    print("Upper bound:")
    upperBound = 100
    up = exercise1.not_number_rejector (upperBound)

    print("OK then, a number between {} and {} ?".format(low,up))
    upperBound = int(upperBound)

    actualNumber = exercise1.stubborn_asker(low, up )
    
   
    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    print(advancedGuessingGame())
