from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "-" and Winner() is False:
        if player == Players[0]:
            buttons[row][column]['text'] = player

            if Winner() is False:
                player = Players[1]
                label.config(text=(Players[1] + " Turn!"))

            elif Winner() is True:
                label.config(text=(Players[0] + " Wins!"))

            elif Winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][column]['text'] = player
            if Winner() is False:
                player = Players[0]
                label.config(text=(Players[0] + " Turn!"))

            elif Winner() is True:
                label.config(text=(Players[1] + "Wins!"))

            elif Winner() == "Tie":
                label.config(text="Tie!")


def Winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "-":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "-":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "-":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "-":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is True:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "-":
                spaces -= 1

    if spaces == 0:
        return True
    else:
        return False

def new_game():
    global player
    player = random.choice(Players)
    label.config(text=player + " Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="-",bg="#F0F0F0")

Window = Tk()
Window.title("TicTacToe")
Players = ["X","O"]
player = random.choice(Players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + "s Turn", font=("Times New Roman", 20))
label.pack(side="top")

reset_butt = Button(text="Reset Game", command=new_game)
reset_butt.pack(side="top")

Window.config(background="White")


buttonFrame = Frame(Window)
buttonFrame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(buttonFrame, text="-", width=10, height=5,
                                      command=lambda row=row, column=column:next_turn(row, column))
        buttons[row][column].grid(row=row,column=column)

Window.mainloop()
