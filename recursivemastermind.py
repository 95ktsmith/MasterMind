#!/usr/bin/python3
""" mastermind console version """
import random



def rec_mastmind(master=None, turn=0):
    """ the recursive funciton """
    if master == None:
        print("welcome to mastermind!")
        print("choosing number")
        rec_mastmind([])
        return
        master.append(random.randrange(0, 9))
        master.append(random.randrange(0, 9))
        master.append(random.randrange(0, 9))
        master.append(random.randrange(0, 9))
        print("number chosen beginning game")
        print("im testing so the master nmber is {}".format(master))
        rec_mastmind(master, 0)
    elif len(master) < 4:
        newnum = random.randrange(0, 9)
        if newnum not in master:
            master.append(newnum)
        rec_mastmind(master, 0)
    else:
        # print("please choose 4 digit number")
        n = int(input())
        guess = [int(n / 1000),
                 int(n / 100 % 10),
                 int(n / 10 % 10),
                 int(n % 10)]
        if n == 0:
            """ option to quit the game """
            return
        if n > 10000 or n < 0:
            print("number must be four digits")
            rec_mastmind([], turn)
        # print("You guessed {}".format(n))
        print("{}".format(guess), end="")
        correct = 0
        place = 0
        if int(n % 10) == master[3]:
            place += 1
            correct += 1
        elif int(n % 10) in master:
            correct += 1
        if int(n / 10 % 10) == master[2]:
            place += 1
            correct += 1
        elif int(n / 10 % 10) in master:
            correct += 1
        if int(n / 100 % 10) == master[1]:
            place += 1
            correct += 1
        elif int(n / 100 % 10) in master:
            correct += 1
        if int(n / 1000 % 10) == master[0]:
            place += 1
            correct += 1
        elif int(n / 1000 % 10) in master:
            correct += 1
        if place == 4:
            print("congratulations, you guessed right in {} guesses".format(turn))
            return
        # print("im testing so the master nmber is {}".format(master))
        print("you guessed {} correct numbers with {}\
              in the right place".format(correct, place))
        rec_mastmind(master, turn + 1)

if __name__ == "__main__":
    rec_mastmind()
