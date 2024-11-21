from tkinter import *
import time

Width: int = 500
Height: int = 500
xSpeed: int = 10
ySpeed: int = 5
Window = Tk()

canvas = Canvas(Window, width=Width, height=Height)
canvas.pack()

background = PhotoImage(file='pngegg.png')
bg_image = canvas.create_image(0, 0, image=background, anchor=NW)

photo = PhotoImage(file='link.png')
my_image = canvas.create_image(0, 0, image=photo, anchor=NW)

imgWidth = photo.width()
imgHeight = photo.height()

while True:
    coordinates = canvas.coords(my_image)
    if coordinates[0] >= Width-imgWidth or coordinates[0] < 0:
        xSpeed = -xSpeed
    if coordinates[1] >= Height-imgHeight or coordinates[1] < 0:
        ySpeed = -ySpeed
    canvas.move(my_image, xSpeed, ySpeed)
    Window.update()
    time.sleep(0.1)


Window.mainloop()
