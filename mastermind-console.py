#!/usr/bin/python3
""" Running this will run the console version of the game """

from game_logic.code_gen import generate_code_no_dups
from game_logic.code_gen import generate_code_dups
from game_logic.guess_checking import Checker

from sys import argv

if __name__ == '__main__':

    #default settings
    duplicates = False
    code_length = 4

    # Checks if the user added options
    if (len(argv) > 1):
        if ('help' in argv[1]):
            print("./mastermind-console.py [code length] [duplicates (true for false)]")
            print("Ex. ./mastermind-console.py 6 false")
            print("If no options provided, defaults will be used. (Code: 4, Defaults: False)")
            exit(1)

        # Checks if the user input an option and validates it
        if (argv[1].isdigit()):
            code_length = int(argv[1])
        else:
            print("Options format: ./mastermind-console.py [code length] [duplicates (true for false)]")
            print("Ex. ./mastermind-console.py 6 false")
            print("If no options provided, defaults will be used. (Code: 4, Defaults: False)")
            exit(1)
    #^ V just making sure the user isnt typing anything dumb as an option
    # Checks if the user input an option and validates it
    if (len(argv) > 2):
        if ('True' in argv[2] or 'true' in argv[2]):
            duplicates = True
        elif ('False' in argv[2] or 'false' in argv[2]):
            duplicates = False
        else:
            print("Options format: ./mastermind-console.py [code length] [duplicates (true for false)]")
            print("Ex. ./mastiomind-console.py 6 false")
            print("If not options provided, defaults will be used. (Code: 4, Defaults: False)")
            exit(1)

    # assigns game rules based on user input (Or sticks with defaults)
    if (duplicates is True):
        code = generate_code_dups(code_length)
    elif (duplicates is False):
        code = generate_code_no_dups(code_length)
    else:
        print("Something went wrong :/ try again")

    print("____----Mastermind----____")
    print(" Can you crack the code?\n")
    print("Code length: {}".format(code_length))
    print("Duplicates allowed: {}\n".format(duplicates))

    print("'Run ./mastermind-console.py help' for rules and helpful tips")

    guesses_remaining = 10
    while (guesses_remaining >= 0):
        guess = input("Type in your guess, {} digits: ".format(code_length))
        print(guess)

        if (len(guess) > code_length):
            print("Woops, too many digits ({} > {})\n".format(len(guess), code_length))
            continue
        if (len(guess) < code_length):
            print("Woops, not enough digits ({} < {})\n".format(len(guess), code_length))
            continue
        if (guess.isdigit() is False):
            print("Woops, your guess may only contain numbers.\n")
            continue

        if ('win' in Checker(guess, code)):
            print("You've cracked the code! it was {}, congrats!".format(code))
            exit(1)
        else:
            print("Hint: {}\n".format(Checker(guess, code)))

        print("Guesses remaining: {}".format(guesses_remaining))
        guesses_remaining -= 1

    print("You ran out of guesses, better luck next time")
