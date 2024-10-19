from tkinter import *


def Fun() -> None:
    if v.get() == 1:
        print("You checked!")
        Check_butt['text'] = "Done!"
        Check_butt['state'] = "disabled"
        Check_butt['bg'] = "Purple"


Window = Tk()
v = IntVar()

Check_butt = Checkbutton(Window, text="Check",
                         variable=v,
                         command=Fun,
                         font=("Times New Roman", 15),
                         bg="Black",
                         fg="Lightblue")
Check_butt.pack()

Window.mainloop()
