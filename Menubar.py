from tkinter import *

def OpenFile():
    print("You opened a File!")

def SaveFile():
    print("You saved a File!")

def Ddef():
    print("You executed option D!")

def Edef():
    print("You executed option E!")

def Fdef():
    print('You executed option F!')


Window = Tk()

menubar = Menu(Window)
Window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=('Arial', 10, 'bold'))
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=OpenFile)
filemenu.add_command(label='Save', command=SaveFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=quit)

editmenu = Menu(menubar, tearoff=0, font=('Arial', 10, 'bold'))
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label="D", command=Ddef)
editmenu.add_command(label="E", command=Edef)
editmenu.add_separator()
editmenu.add_command(label="F", command=Fdef)



Window.mainloop()
