from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def submit():
    #file = filedialog.asksaveasfile()
    filepath = filedialog.askopenfilename(title="Please choose a file",
                                          filetypes=(("Text files", "*.txt"), ("All files", "*.*"),
                                                     ('HTML Files', '*.htm')))
    file = open(filepath, "rt")
    messagebox.showinfo("Title", file.read())
    file.close()


Window = Tk()
#Window.geometry('600x200')
Submit = Button(Window, text="Submit your documents here!",
                font=("Times New Roman", 20, "bold"),
                command=submit)
Submit.pack(padx=5, pady=55)
Window.mainloop()