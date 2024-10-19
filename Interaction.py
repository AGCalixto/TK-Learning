from tkinter import *


def Up(event):
    x = label.winfo_x()
    y = label.winfo_y() - 5
    label.place(x=x, y=y)


def Back(event):
    x = label.winfo_x()
    y = label.winfo_y() + 5
    label.place(x=x, y=y)


def Right(event):
    x = label.winfo_x() + 5
    y = label.winfo_y()
    label.place(x=x, y=y)


def Left(event):
    x = label.winfo_x() - 5
    y = label.winfo_y()
    label.place(x=x, y=y)


Window = Tk()
Window.geometry('300x300')
label = Label(Window, bg='red', width=5, height=3)
label.place(x=0, y=0)

Window.bind("<w>", Up)
Window.bind("<a>", Left)
Window.bind("<s>", Back)
Window.bind("<d>", Right)

Window.mainloop()
