#!/usr/bin/python3
import random
from tkinter import *


class MasterMind:
    bclick = True

    def __init__(self, master):
        self.master = master
        master.title("mastermind")
        master.geometry("350x700")
        self.cbtns = []
        self.btns = []
        self.colorn = ['red', 'blue', 'green', 'orange',
                       'black', 'white', 'purple', 'brown']
        self.colord = {'red': 0, 'blue': 1, 'green': 2, 'orange': 3,
                       'black': 4, 'white': 5, 'purple': 6, 'brown': 7}
        self.current_color = self.colorn[0]
        self.current_row = 4
        self.answer = [random.randint(0, 7) for i in range(4)]
        self.guess = [5, 5, 5, 5]

        for i in range(8):
            self.cbtns.append(Button(bg=self.colorn[i], height=1, width=1))
        for i in range(44):
            self.btns.append(Button(font=('Times 20 bold'),
                             bg='white',
                             fg='black', height=1, width=1))
        checkbtn = Button(bg='white', text="check row", height=1, width=4)
        resetbtn = Button(bg='white', text="reset Game", height=1, width=4)
        self.var = StringVar()
        labelval = Message(tk, bg='white', textvariable=self.var)
        self.var.set("time to see who's the master")
        row = 3
        column = 0
        index = 1
        # print(self.btns)
        buttons = StringVar()
        for i in self.cbtns:
            i.grid(row=1, column=column)
            i.config(command=lambda current_button=i:
                     self.recolor(current_button))
            column += 1
        column = 0
        row += 1
        checkbtn.grid(row=2, column=0, columnspan=4, sticky=W+E)
        checkbtn.config(command=lambda current_button=checkbtn:
                        self.check(current_button))
        labelval.grid(row=2, column=4, columnspan=4, rowspan=5, sticky=W+E+N+S)
        for i in self.btns:
            i.grid(row=row, column=column)
            i.config(command=lambda current_button=i: self.ttt(current_button))
            print(i, i["command"])
            column += 1
            if index % 4 == 0:
                row += 1
                column = 0
            index += 1
        resetbtn.config(command=lambda current_button=resetbtn:
                        self.reset(current_button))
        resetbtn.grid(row=row, column=0, columnspan=4, sticky=W+E)

    def reset(self, button):
        self.current_row = 4
        self.answer = [random.randint(0, 7) for i in range(4)]
        self.guess = [5, 5, 5, 5]
        for i in self.btns:
            i.config(text="", bg='white')
        self.var.set("Playing again i see")

    def ttt(self, button):
        global bclick
        global current_color
        current_color = self.current_color
        current_row = self.current_row
        # print(button)
        # print("current row is{}".format(current_row))
        info = button.grid_info()
        # print(info['row'], end="")
        # print("----------{}".format(current_row))
        if info['row'] == self.current_row:
            # print("if")
            button.config(text="X", bg=self.current_color)
            # bclick = False
            self.guess[info['column']] = self.colord[self.current_color]

    def check(self, button):
        global answer
        global guess
        place = 0
        correct = 0
        if self.current_row > 10:
            return
        print(self.guess)
        print(self.answer)
        for i in [0, 1, 2, 3]:
            if self.guess[i] == self.answer[i]:
                place += 1
                correct += 1
            elif self.guess[i] in self.answer:
                correct += 1
        print("{} correct {} in the right spot".format(correct, place))
        self.var.set("{} correct {} in the right spot".format(correct, place))
        if place == 4:
            print("Congratulations, you win")
            self.var.set("Congratulations! you win!")
            self.current_row += 20
        self.current_row += 1
        self.guess = [5, 5, 5, 5]

    def recolor(self, button):
        print(button)
        print(button["bg"])
        self.current_color = button["bg"]
        for i in self.cbtns:
            i["text"] = ""
        button["text"] = "X"
        print(self.current_color)

tk = Tk()
gui = MasterMind(tk)
tk.mainloop()
