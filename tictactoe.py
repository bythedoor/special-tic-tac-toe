from tkinter import *
from tkinter import ttk
import random

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
tictactoe = ttk.Frame(root, padding=10)
tictactoe.grid()
ttk.Label(frm, text="welcome to my first game of tic tac toe !").grid(column=1, row=0)
ttk.Button(tictactoe, text="Quit", command=root.destroy).grid(column=1, row=5)

playerTurn = 0

# functions
def changeSquareLabel(playerTurn):
    if playerTurn == 0:
        playerTurn = 1
        return "O"
    else:
        playerTurn = 0
        return "X"

# tic tac toe interface
ttk.Button(tictactoe, command=changeSquareLabel(playerTurn)).grid(column=0, row=1)
ttk.Button(tictactoe, command=root.destroy).grid(column=1, row=1)
ttk.Button(tictactoe, command=root.destroy).grid(column=2, row=1)
ttk.Button(tictactoe, command=root.destroy).grid(column=0, row=2)
ttk.Button(tictactoe, command=root.destroy).grid(column=1, row=2)
ttk.Button(tictactoe, command=root.destroy).grid(column=2, row=2)
ttk.Button(tictactoe, command=root.destroy).grid(column=0, row=3)
ttk.Button(tictactoe, command=root.destroy).grid(column=1, row=3)
ttk.Button(tictactoe, command=root.destroy).grid(column=2, row=3)


root.mainloop()