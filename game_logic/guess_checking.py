#!/usr/bin/python3
""" All functions regarding guess/answer checking """

def Checker(input, master):
    """ Checker """
    info = ""
    cnt = 0
    for char in input:
        if char in master:
            if char == master[cnt]:
                info += "*"
            else:
                info += "#"
        else:
            info += "-"
        cnt += 1
    if info == "****":
        return "win"
    return "".join(reversed(sorted(info)))
