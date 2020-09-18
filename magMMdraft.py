#!/usr/bin/python3
import random
from tkinter import *
if 1 == 1:
    bclick = True


    tk = Tk()
    tk.title("Mastermind")
    tk.geometry("350x700")
    n = 9
    cbtns = []
    btns = []
    colorn = ['red', 'blue', 'green', 'orange',
              'black', 'white', 'purple', 'brown']
    colord = {'red': 0, 'blue': 1, 'green': 2, 'orange': 3,
              'black': 4, 'white': 5, 'purple': 6, 'brown': 7}
    current_color = colorn[0]
    current_row = 4
    answer = [random.randint(0, 7) for i in range(4)]
    print(answer)
    guess = [5, 5, 5, 5]

    def reset(button):
        global guess
        global current_row
        current_row = 4
        print(guess)
        guess = [5, 5, 5, 5]
        for i in btns:
            i.config(text="", bg='white')

    def ttt(button):
        global bclick
        global current_color
        global current_row
        print(button)
        print("current row is{}".format(current_row))
        info = button.grid_info()
        print(info['row'], end="")
        print("----------{}".format(current_row))
        if info['row'] == current_row:
            print("if")
            button.config(text="X", bg=current_color)
            bclick = False
            guess[info['column']] = colord[current_color]

    def check(button):
        global bclick
        global current_row
        global answer
        global guess
        place = 0
        correct = 0
        print(guess)
        print(answer)
        # guess = ["", "", "", ""]
        for i in btns:
            info = i.grid_info()
            # if info["row"] == current_row:
                # guess[info['colunm']] = info['bg']
        print(guess)
        for i in [0, 1, 2, 3]:
            if guess[i] == answer[i]:
                place += 1
                correct += 1
            elif guess[i] in answer:
                correct += 1
        print("{} correct {} in the right spot".format(correct, place))
        if place == 4:
            print("Congratulations, you win")
        # print(info)
        # print("implement check")
        current_row += 1
        guess = [5, 5, 5, 5]


    def recolor(button):
        global blick
        global current_color
        print(button)
        print(button["bg"])
        current_color = button["bg"]
        for i in cbtns:
            i["text"] = ""
        button["text"] = "X"
        print(current_color)

    for i in range(8):
        cbtns.append(Button(bg=colorn[i] , height=1, width=1))

    for i in range(44):
        btns.append(Button(font=('Times 20 bold'), bg='white', fg='black', height=1, width=1))

    checkbtn = Button(bg='white', text="check row", height = 1, width=4)
    resetbtn = Button(bg='white', text="reset Game", height=1, width=4)
   
    row = 3
    column = 0
    index = 1
    print(btns)
    buttons = StringVar()
    for i in cbtns:
        i.grid(row=1, column=column)
        i.config(command=lambda row=1, column=0, current_button=i: recolor(current_button))
        column += 1
    column = 0
    row += 1
    checkbtn.grid(row=2, column=0, columnspan=4)
    checkbtn.config(command=lambda row=1, column=0, current_button=checkbtn: check(current_button))
    for i in btns:

        i.grid(row=row, column=column)
        i.config(command=lambda row=row, column=column, current_button=i: ttt(current_button))
        print(i, i["command"])
        column += 1
        if index % 4 == 0:
            row += 1
            column = 0
        index += 1
    resetbtn.config(command=lambda current_button=resetbtn: reset(current_button))
    resetbtn.grid(row=row, column=0, columnspan=4)
    tk.mainloop()
