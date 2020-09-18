#!/usr/bin/python3
""" This file contains all functions used in code generation """

from random import seed
from random import randint


def generate_code_no_dups(len=4):
    """ This generates a code NO DUPLICATES! """
    list = []

    """ were only using 8 characters """
    if (len > 8):
        print("more than 8 digits is not possible without duplicates.")
        exit(1)

    for iter in range(0, len):
        digit = randint(0, 8)
        while (digit in list):
            digit = randint(0, 8)
        list.append(digit)

    return list


def generate_code_dups(len=4):
    """ This generates code that include duplicates (Possibly) """
    list = []

    for iter in range(0, len):
        digit = randint(0, 8)
        list.append(digit)

    return list
