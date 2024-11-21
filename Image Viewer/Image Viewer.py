from tkinter import *
from PIL import ImageTk, Image

def PreImg(image_number):
    global preImg
    global nextImg
    global imgDisplay

    if image_number == 0:
        preImg.config(state=DISABLED)

    else:
        imgDisplay.grid_forget()
        imgDisplay = Label(image=photos[image_number-1])
        imgDisplay.grid(row=1, column=0, columnspan=3)

        nextImg = Button(Window, text='>>', command=lambda: NextImg(image_number + 1))
        nextImg.grid(row=2, column=2)
        preImg = Button(Window, text='<<', command=lambda: PreImg(image_number - 1))
        preImg.grid(row=2, column=0)


def NextImg(image_number):
    global preImg
    global nextImg
    global imgDisplay

    if image_number == 6:
        nextImg.config(state=DISABLED)

    else:
        imgDisplay.grid_forget()
        imgDisplay = Label(image=photos[image_number-1])
        imgDisplay.grid(row=1, column=0, columnspan=3)

        nextImg = Button(Window, text='>>', command=lambda: NextImg(image_number+1))
        nextImg.grid(row=2, column=2)
        preImg = Button(Window, text='<<', command=lambda: PreImg(image_number-1))
        preImg.grid(row=2, column=0)


Window = Tk()

img1 = ImageTk.PhotoImage(file='Casa1.jpg')
img2 = ImageTk.PhotoImage(file='Casa2.jpg')
img3 = ImageTk.PhotoImage(file='Paisaje1.jpg')
img4 = ImageTk.PhotoImage(file='Paisaje2.jpg')
img5 = ImageTk.PhotoImage(file='Paisaje3.jpg')

photos = [img1, img2, img3, img4, img5]

title = Label(Window, text='Your Images', font=('Constantia', 24, 'bold'))
title.grid(row=0, column=0, columnspan=3)

imgDisplay = Label(Window, image=img1)
imgDisplay.grid(row=1, column=0, columnspan=3)

preImg = Button(Window, text='<<', command=lambda: PreImg(1))
preImg.grid(row=2, column=0)
quitImg = Button(Window, text='Quit', font=('Constantia', 14, 'bold'), command=Window.destroy)
quitImg.grid(row=2, column=1)
nextImg = Button(Window, text='>>', command=lambda: NextImg(2))
nextImg.grid(row=2, column=2)


Window.mainloop()
