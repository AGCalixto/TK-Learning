import random
from tkinter import *
from tkinter import messagebox


def PassCreation():
    app1: int = 0
    app2: int = 0
    app3: int = 0
    password: str = ''

    if x.get():
        letters = ['a', 'b', 'c', 'd', 'e',
                   'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F',
                   'G', 'H', 'I', 'J', 'K', 'L',
                   'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
    else:
        letters = ['a', 'b', 'c', 'd', 'e',
                   'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o',
                   'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

    a = entry1.get()
    b = entry2.get()
    c = entry3.get()

    if a == '' or b == '' or c == '':
        messagebox.showerror(title='Error', message='Please fill the blanks!')
        return

    elif a.isalpha() or b.isalpha() or c.isalpha():
        messagebox.showerror(title='Error', message='Please just use numbers!')
        return

    else:
        while app1 < int(a):
            password += random.choice(letters)
            app1 += 1

        while app2 < int(b):
            password += random.choice(nums)
            app2 += 1

        while app3 < int(c):
            password += random.choice(symbols)
            app3 += 1
    passlabel.config(text='Your New Fully Brand Password is: \n' + password)


# TK initialization and Window Creation
Window = Tk()
Window.title('Password Generator')
Window.geometry('400x350')
Window.config(bg='light grey')

# Numbers list creation
nums: list = []
for index in range(0, 10):
    nums.append(str(index))

# Symbols list creation
symbols: list = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '+']

Titlelabel = Label(Window, text='Welcome to My Password Generator!',
                   font=('Constant', 16, 'bold'), bg='light gray')
Titlelabel.pack()

rlabel = Label(Window, text='-------------------------------------------------',
               font=('Constant', 16), bg='light gray')
rlabel.pack()

# ---------------------------------------------------------------------
label1 = Label(Window, text='How Many Letters do you want to include?',
               font=('Constant', 12), bg='light gray')
label1.pack()

entry1 = Entry(Window, font=('Times New Roman', 10))
entry1.pack()

# ---------------------------------------------------------------------
label2 = Label(Window, text='How Many Numbers do you want to include?',
               font=('Constant', 12), bg='light gray')
label2.pack()

entry2 = Entry(Window, font=('Times New Roman', 10))
entry2.pack()

# ---------------------------------------------------------------------
label3 = Label(Window, text='How Many Symbols do you want to include?',
               font=('Constant', 12), bg='light gray')
label3.pack()

entry3 = Entry(Window, font=('Times New Roman', 10))
entry3.pack()

# -------------------U-S-E--U-P-P-E-R-C-A-S-E--------------------------
x = BooleanVar()
Uppers = Checkbutton(Window, text='Include uppercase letters',
                     variable=x, font=('Constant', 14), bg='light gray',
                     onvalue=True, offvalue=False)
Uppers.pack()

# ---------------------------------------------------------------------
r2label = Label(Window, text='-------------------------------------------------',
                font=('Constant', 16), bg='light gray')
r2label.pack()

# ---------------------------------------------------------------------
Submit_button = Button(Window, text='Generate password',
                       font=('Constant', 12), bg='gray',
                       activebackground='white',
                       command=PassCreation)
Submit_button.pack()

# ---------------------------------------------------------------------

passlabel = Label(Window, text='',
                  font=('Constantia', 12, 'bold'),
                  bg='light gray')

passlabel.pack()
mainloop()
