from tkinter import *
import time
from Ball import *

Height = 500
Width = 500
Window = Tk()
Window.title('Multiple Animations')
canvas = Canvas(Window, height=Height, width=Width)
canvas.pack()

Volleyball = Ball(canvas, 5, 5, 100, 5, 5, 'white')
Blackball = Ball(canvas, 5, 5, 200, 10, 20, 'black')
Redball = Ball(canvas, 5, 5, 150, 30, 15, 'red')
Tenisball = Ball(canvas, 5, 5, 50, 50, 35, 'green')

while True:
    Volleyball.move()
    Blackball.move()
    Redball.move()
    Tenisball.move()
    Window.update()
    time.sleep(0.1)


Window.mainloop()
