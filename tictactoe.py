import tkinter
import random

# functions
def changeTileLabel(row, column):
    # check if the tile is empty
    global currPlayer, turns
    if buttons[row][column]["text"] != "":
        return

    # if not, writes the symbol of the current player
    buttons[row][column]["text"] = currPlayer
    if currPlayer == "X" :
        currPlayer = players[1]
        turns += 1
    else :
        currPlayer = players[0]
        turns += 1

    #the turn label changes depending on whose turn it is
    turnLabel["text"] = "it's " + currPlayer + " turn !"

    checkBoard()

def checkBoard():
    # checking horizontally
    for row in range(3):
        if (buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"]) and buttons[row][0]["text"] != "":
            turnLabel["text"] = buttons[row][0]["text"] + " won !"

    #checking vertically
    for column in range(3):
        if (buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"]) and buttons[0][column]["text"] != "":
            turnLabel["text"] = buttons[0][column]["text"] + " won !"

    #checking diagonally
    if (buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"]) and buttons[0][0]["text"] != "":
        turnLabel["text"] = buttons[0][0]["text"] + " won !"

    #checking anti diagonally
    if (buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"]) and buttons[0][2]["text"] != "":
        turnLabel["text"] = buttons[0][2]["text"] + " won !"

    #checking if there's a tie
    if turns == 9:
        turnLabel["text"] = "nobody won ... :("

    
# variables
players = ["X", "O"]
currPlayer = players[0]
turns = 0
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