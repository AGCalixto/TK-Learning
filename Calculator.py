import math
from tkinter import *
from tkinter import messagebox

def Back():
    global Equation_text

    Equation_text = Equation_text[:len(Equation_text)-1]
    Equation_label.set(Equation_text)

def Fac(n):
    if n > 990:
        return 0
    elif n == 1:
        return 1
    else:
        n *= Fac(n - 1)
    return n


def Bpress(num):
    global Equation_text

    Equation_text = Equation_text + str(num)
    Equation_label.set(Equation_text)


def Equal():
    global Equation_text
    if Equation_text == "":
        total = ""

    elif '|' in Equation_text:
        if '.' in Equation_text:
            messagebox.showerror(title='Error', message='Can not get square root of decimals, DUMBASS!')
            total = str('')

        else:
            total = str(math.sqrt(int(Equation_text[:len(Equation_text)-1])))

    elif '/0' in Equation_text:
        messagebox.showerror(title='Error', message='Can not divide by zero, DUMBASS!')
        total = ''

    elif '!' in Equation_text:
        if '.' not in Equation_text:
            total = str(Fac(int(Equation_text[:len(Equation_text)-1])))

            if int(Equation_text[:len(Equation_text)-1]) >= 991:
                total = ''
                messagebox.showerror(title='Error',
                                     message='Can not use factorial in a number greater than 991!')

        else:
            total = ''
            messagebox.showerror(title='Error', message='Can not use factorial in decimals, DUMBASS!')

    else:
        total = str(eval(Equation_text))

    Equation_label.set(total)

    Equation_text = total


def Clear():
    global Equation_text
    global Equation_label

    Equation_text = " "
    Equation_label.set(Equation_text)


Window = Tk()
Window.title("Calculator")
Window.geometry("325x540")
Window.config(bg="#a6a4a1")

Title = Label(Window, text="Simple Calculator", font=("Times New Roman", 20, "bold"),
              bg="#a6a4a1")
Title.pack()

Equation_text = ""
Equation_label = StringVar()

Result = Label(Window, textvariable=Equation_label, font=("Arial", 20), bg="white",
               width=20, height=2)
Result.pack()

Space = Label(Window, text="-----------------------------------------", bg="#a6a4a1")
Space.pack()

BFrame = Frame(Window)
BFrame.pack()

buttons = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]

for row in range(1, 4):
    for column in range(4):
        buttons[row][column] = Button(BFrame, text="", font=("Arial", 16, "bold"), width=5, height=2,
                                      command=lambda row=row, column=column: Bpress(buttons[row][column]['text']))
        buttons[row][column].grid(row=row, column=column)

for column in range(3):
    buttons[1][column]['text'] = column + 1
for column in range(3):
    buttons[2][column]['text'] = column + 4
for column in range(3):
    buttons[3][column]['text'] = column + 7

#---------------------------Z-E-R-O-------------------------------------
button0 = Button(BFrame, text=0, font=("Arial", 16, "bold"), width=5, height=2,
                 command=lambda: Bpress(0))
button0.grid(row=4, column=1)

#--------------------------P-L-U-S--------------------------------------------

plus = Button(BFrame, text='+', font=("Arial", 16, "bold"), width=5, height=2,
              command=lambda: Bpress('+'))
plus.grid(row=0, column=3)

#--------------------------M-I-N-U-S------------------------------------------

buttons[1][3]['text'] = '-'

#--------------------M-U-L-T-I-P-L-I-C-A-T-I-O-N------------------------------

multiply = Button(BFrame, text='*', font=("Arial", 16, "bold"), width=5, height=2,
                  command=lambda: Bpress('*'))
multiply.grid(row=2, column=3)

#----------------------------D-I-V-I-S-I-O-N----------------------------------

division = Button(BFrame, text='/', font=("Arial", 16, "bold"), width=5, height=2,
                  command=lambda: Bpress('/'))
division.grid(row=3, column=3)

#--------------------------E-X-P-O-N-E-N-T-I-A-L--------------------------------

exponent = Button(BFrame, text='^', font=("Arial", 16, "bold"), width=5, height=2,
                  command=lambda: Bpress('**'))
exponent.grid(row=0, column=2)

#--------------------------F-A-C-T-O-R-I-A-L-------------------------------------

factorial = Button(BFrame, text='n!', font=("Arial", 16, "bold"), width=5, height=2,
                   command=lambda: Bpress('!'))
factorial.grid(row=0, column=1)

#------------------------------D-E-C-I-M-A-L------------------------------------

decimal = Button(BFrame, text='.', font=("Arial", 16, "bold"), width=5, height=2,
                 command=lambda: Bpress('.'))
decimal.grid(row=4, column=0)

#-------------------------S-Q-U-A-R-E--R-O-O-T----------------------------------

square = Button(BFrame, text='sqrt', font=("Arial", 16, "bold"), width=5, height=2,
                command=lambda: Bpress('|'))
square.grid(row=0, column=0)


#-------------------------------C-L-E-A-R--------------------------------------

clear = Button(BFrame, text='clear', font=("Arial", 16, "bold"), width=5, height=2,
               command=Clear)
clear.grid(row=4, column=3)

#-------------------------------B-A-C-K--------------------------------------

back = Button(BFrame, text='<-', font=("Arial", 16, "bold"), width=5, height=2,
              command=Back)
back.grid(row=4, column=2)

#-------------------------------E-Q-U-A-L-S-----------------------------------

equals = Button(BFrame, text='=', font=("Arial", 16, "bold"), width=10, height=2,
                command=Equal)
equals.grid(row=5, column=2, columnspan=2)

#---------------------------P-A-R-E-N-T-H-E-S-I-S-----------------------------------
r_parenth = Button(BFrame, text='(', font=("Arial", 16, 'bold'), width=5, height=2,
                   command=lambda: Bpress('('))
r_parenth.grid(row=5, column=0)

l_parenth = Button(BFrame, text=')', font=("Arial", 16, 'bold'), width=5, height=2,
                   command=lambda: Bpress(')'))
l_parenth.grid(row=5, column=1)


#Functions
#Advanced Functions
'''
buttons[0][0]['text'] = "n!"
buttons[0][1]['text'] = "^"
buttons[0][2]['text'] = "sqrt"


#Basic Functions
buttons[0][3]['text'] = "+"
buttons[1][3]['text'] = "-"
buttons[2][3]['text'] = "*"
buttons[3][3]['text'] = "/"
'''

Window.mainloop()
