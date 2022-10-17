#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/10/17
# Randomizes a number between 0 and 9 and
# Asks the user to guess. Try Catch code put in place
# To make sure integers are being used.

# to be able to create random numbers
import random


def main():

    # Title
    print("Guess the Randomized Number")

    # To create the randomized correct number
    random_number = random.randint(0, 9)

    # User input for the guessed number
    guess = input("Guess the number between 0 and 9: ")
    try:
        guess_as_integer = int(guess)

    # Exception to the try catch to tell the user to enter an integer
    except Exception:
        print("Please enter an integer instead of a string.")

    else:
        # If the user input is not between 0 and 9
        if guess_as_integer > 9 or guess_as_integer < 0:
            print("Please enter an integer between 0 and 9!")
        else:
            # IF statement if the user guesses the integer correctly
            if guess_as_integer == random_number:
                print("You guessed the number correctly! Great job!")

            # ELSE statement if the user guesses the integer incorrectly
            else:
                print(
                    "You guessed the number incorrectly. The correct number was {}".format(
                        random_number
                    )
                )


if __name__ == "__main__":
    main()
