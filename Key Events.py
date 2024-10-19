from tkinter import *


def Enter(event):
    print('You pressed Enter!')


def Forward(event):
    print('You moved Forward!')


def Backward(event):
    print('You moved Backwards!')


def Right(event):
    print('You moved Right!')


def Left(event):
    print('You moved Left!')

def LeftClick(event):
    print('You used your Left Click!')

def MouseWheel(event):
    print('You used your Mouse Wheel!')

def RightClick(event):
    print('You used your Right Click!')


# Use '<Key>' to get any key from the user.
# Use 'event.keysym' to access the pressed key.

Window = Tk()

Window.bind("<Return>", Enter)
Window.bind("<w>", Forward)
Window.bind("<s>", Backward)
Window.bind("<a>", Left)
Window.bind("<d>", Right)

# Mouse Events
# To access the Left click of your mouse, use "<Button-1>".
# To access the Wheel of your mouse, use "<Button-2>".
# To access the Right click of your mouse, use "<Button-3>".

# Use 'event.x' and 'event.y' to get the coordinates of your clicks.

# Use "<ButtonRelease>" to perform an action when you release a button.
# Use "<Motion>" to receive constant coordinates of where the mouse is.
Window.bind("<Button-1>", LeftClick)
Window.bind("<Button-2>", MouseWheel)
Window.bind("<Button-3>", RightClick)

Window.mainloop()
