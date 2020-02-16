# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program
# will ask the user for their input. This project will better your
# understanding of while loops and if statements.
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


def game():
    computer = randint(1, 3)
    dict = {
        0: "scissors",
        1: "rock",
        2: "paper",
        3: "scissors",
        4: "rock",
        "r": 1,
        "p": 2,
        "s": 3
    }

    while True:
        try:
            player = input("Jack and Poy! what's your play? (r/p/s)")
            print(f'you: {dict[dict[player]]}')
            print(f'computer: {dict[computer]}')
        except KeyError:
            print("Input error! Try again")
            continue
        if dict[dict[player]] == dict[computer]:
            print("It's a tie. Try again")
            game()
            return
        elif dict[dict[player] + 1] == dict[computer]:
            print("You lose!")
            if playAgain():
                game()
            return
        elif dict[dict[player] - 1] == dict[computer]:
            print("Congratulations! You win!")
            if playAgain():
                game()
            return

print("Welcome to rock-paper-scissors game. Use 'r' for rock, 'p' for paper, and 's' for scissors.")
game()
