# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is. If the user guesses wrong,
# tell them their guess is either too high, or too low.
# This will get you started with the random library if you haven't already used it.

from random import randint

def playAgain():
    while True:
        inp_continue = input("Do you want to play again? (Y/N): ")
        if inp_continue.lower() == "y":
            return True
        elif inp_continue.lower() == "n":
            return False
        else:
            print("Input Error. Try Again")

def guess():
    randomNumber = randint(0, 20)
    print(randomNumber)
    while True:
        try:
            inp = int(input("Guess the number from 0 to 20: "))
        except ValueError:
            print("Input Error, integers from 0 to 20 are only allowed")

        if 0 < inp > 20:
            print("Input Error, integers from 0 to 20 are only allowed")
        elif inp > randomNumber:
            print("Lower, try again!")
        elif inp < randomNumber:
            print("Higher, try again!")
        elif inp == randomNumber:
            print(f'CONGRATULATIONS!!! You got the correct number: {str(randomNumber)}')
            if playAgain():
                guess()
            return
guess()