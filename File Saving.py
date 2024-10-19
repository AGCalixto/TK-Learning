from tkinter import *
from tkinter import filedialog

def Save():
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text File", ".txt"),
                                        ("HTML File", ".htm")
                                    ])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

Window = Tk()
save = Button(Window, text="Save File", font=("Times New Roman", 22),
              command=Save)
save.pack(side="top")

text = Text(Window, font=("Times New Roman", 18))
text.pack()
Window.mainloop()