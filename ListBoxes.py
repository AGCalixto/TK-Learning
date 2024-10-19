from tkinter import *

def Submit():
    selected: list = []

    for index in listbox.curselection():
        selected.insert(index, listbox.get(index))

    print(f'You ordered: ')

    for index in selected:
        print(index)

    if len(selected) == listbox.size():
        print("You selected the whole menu!")

def Add():
    listbox.insert(listbox.size(), entry.get())

def Delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

Window = Tk()

Window.title("MENU")
Window.config(bg="Lightblue")

label1 = Label(Window, text="Welcome to our Restaurant! \nPlease select what you please",
               font=("Constantia", 22, "bold"),
               bg="black",
               fg="white")
label1.pack()

listbox = Listbox(Window,
                  bg="black",
                  fg="white",
                  font=("Constantia", 18, "italic"),
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Hamburger")
listbox.insert(3, "Coffee")
listbox.insert(4, "Milk")
listbox.insert(5, "Eggs")

entry = Entry(Window, font=("Times New Roman", 12))
entry.pack()

add = Button(Window, text="Add Product", command=Add,
             font=("Times New Roman", 12))
add.pack()

delete = Button(Window, text="Delete Product", command=Delete,
                font=("Times New Roman", 12))
delete.pack()

Submit = Button(Window, text="Submit", command=Submit,
                font=("Times New Roman", 14))
Submit.pack()




Window.mainloop()