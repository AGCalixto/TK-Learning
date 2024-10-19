# Canvas - A widget that is used to draw simple graphs or shapes within a window.

from tkinter import *

Window = Tk()

canvas = Canvas(Window, height=500, width=500)

#Pokeball
canvas.create_arc(50, 50, 200, 200, fill='red', width=10, extent=180)
canvas.create_arc(50, 50, 200, 200, fill='white', width=10, start=180, extent=180)
canvas.create_oval(100, 100, 150, 150, fill='white', width=10)

#Tri-Fuerza
canvas.create_polygon(350, 50, 250, 200, 450, 200, fill='yellow', width=5, outline='black')
canvas.create_polygon(300, 125, 400, 125, 350, 200, fill='black')

#Masterball
canvas.create_oval(25, 250, 225, 450, fill='blue', width=10)
canvas.create_arc(25, 250, 225, 450, fill='white', width=10, start=180, extent=180)
canvas.create_oval(90, 320, 160, 380, fill='white', width=10)
canvas.create_oval(100, 330, 150, 370, fill='white', width=1)
canvas.create_arc(70, 245, 225, 445, fill='purple', style=CHORD, outline='black', width=5)
canvas.create_arc(25, 245, 200, 445, fill='purple', style=CHORD, start=90, outline='black', width=5)
canvas.create_line(113, 285, 113, 305, fill='white', width=5)
canvas.create_line(142, 285, 142, 305, fill='white', width=5)
canvas.create_line(113, 285, 128, 295, fill='white', width=5)
canvas.create_line(142, 285, 128, 295, fill='white', width=5)

#Pac-Man
canvas.create_oval(250, 225, 475, 475, fill='yellow', width=10)
canvas.create_arc(250, 225, 475, 475, start=320, fill='black')
canvas.create_oval(325, 275, 345, 300, fill='red', width=10)





canvas.pack()
Window.mainloop()
