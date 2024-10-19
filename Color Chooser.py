from tkinter import *
from tkinter import colorchooser

def Click():
    Window.config(bg=colorchooser.askcolor()[1])

def CustomizeB():
    Label1.config(bg=colorchooser.askcolor()[1])

def CustomizeF():
    Label1.config(fg=colorchooser.askcolor()[1])

Window = Tk()
Window.geometry("200x150")
Window.title("Color Chooser")
CC = Button(Window, text="Style the background!", command=Click)
CC.pack()

Label1 = Label(Window, text="Customize Me!", font=("Arial", 18, "bold"))
Label1.pack()

LC = Button(Window, text="Style the Text's Background!", command=CustomizeB)
LC.pack()

LC2 = Button(Window, text="Style the Text's Color Font!", command=CustomizeF)
LC2.pack()
Window.mainloop()
