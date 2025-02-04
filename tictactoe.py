import tkinter
import random

# functions
def changeTileLabel(row, column):
    # check if the tile is empty
    global currPlayer
    if buttons[row][column]["text"] != "":
        return

    # if not, writes the symbol of the current player
    buttons[row][column]["text"] = currPlayer
    if currPlayer == "X" :
        currPlayer = players[1]
    else :
        currPlayer = players[0]

    #the turn label changes depending on whose turn it is
    turnLabel["text"] = "it's " + currPlayer + " turn !"

# variables
players = ["X", "O"]
currPlayer = players[0]
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0] ]


# window setup
window = tkinter.Tk()
window.title("tic tac toe but it's weirder")
window.resizable(False, False)


frm = tkinter.Frame(window)
frm.grid()
tictactoe = tkinter.Frame(window)
tictactoe.grid()

# title and quit button
label = tkinter.Label(frm, text="welcome to my first game of tic tac toe !").grid(column=1, row=0)
turnLabel = tkinter.Label(frm, text="it's " + currPlayer + " turn !")
turnLabel.grid(column=1, row=21)
quitButton = tkinter.Button(tictactoe, text="Quit", command=window.destroy).grid(column=1, row=5)


# tic tac toe board
for row in range(3) :
    for column in range(3):
        buttons[row][column] = tkinter.Button(tictactoe, text="", width=10, height=4, command= lambda row=row, column=column: changeTileLabel(row,column))
        buttons[row][column].grid(column=column, row=row)



window.mainloop()