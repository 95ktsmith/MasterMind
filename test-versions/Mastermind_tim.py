#!/usr/bin/python3
""" funny """
import random


def Mastermind():
    """
    Mastermind game
    """

    # Game settings
    Tries = 6
    Duplicates = False
    Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    # Internal variables
    Master = []
    uinput = []
    info = ""
    counter = 0
    _try = 0  # Tries loop

    for selector in range(0, 4):
        Master.append(str(random.choice(Numbers)))
        if not Duplicates:
            Numbers.remove(int(Master[selector]))

    # print("Dirty cheater mode: ", end="")
    # print("".join(Master))

    while _try < Tries:
        print("Remaining tries: {}".format(Tries - _try))
        uinput = list(str(input("> ")))

        if len(uinput) != 4:
            # Input isn't 4 digits
            print("Please input 4 digits at a time")
            continue

        if uinput == list("quit"):
            # Forfeit game
            print("The user has forfeit! The Mastermind's code: ", end="")
            print("".join(Master))
            return

        for v in uinput:
            if v in Master:
                if v == Master[counter]:
                    # Perfect match, number and position
                    info += "*"
                else:
                    # Correct number, wrong position
                    info += "#"
            else:
                # Number not present in code
                info += "-"
            counter += 1

        print("".join(sorted(info)))
        counter = 0

        if info == "****":
            # Winner
            print("Winner winner!")
            return

        info = ""
        _try += 1

    print("You lose! The Mastermind's code: {}".format("".join(Master)))


if __name__ == "__main__":
    print("Welcome to the game of Mastermind!\n\
The goal of the game is to blah blah blah i dont care :/\n\
'#' means a correct number, '*' means a correct number and position\n\
Input 4 digits at a time\n\
Type 'quit' to quit\n\
----------------------------------\n\n")
    Mastermind()
