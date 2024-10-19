from tkinter import *

Orders: list = ["Laptops", "Mouses", "Desktops","LCD Screens"]
Window = Tk()
Window.config(bg="Black")
x = IntVar()

for index in range(len(Orders)):
    rb = Radiobutton(Window,
                     text=Orders[index], #Assigns Text
                     variable=x, #Groups buttons together if they share the same variable
                     value=index, #Assigns each radiobutton a different value
                     bg="Black",
                     fg="Red"
                     )
    rb.pack()

Window.mainloop()
