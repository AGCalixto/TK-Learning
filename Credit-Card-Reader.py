from tkinter import *
from tkinter import messagebox

def Reader():
    if entry1.get().isalpha():
        messagebox.showerror(title="Error",
                             message="Numbers only :(")

    else:
        x = entry1.get()
        f: int = 0
        digits = [int(x) for x in str(x)][::-1]

        for index in range(0, len(digits)):
            if index % 2 != 0:
                digits[index] *= 2
                if digits[index] > 9:
                    digits[index] -= 9
            f += digits[index]

        if f == 0:
            messagebox.showerror(title="Error",
                                 message="No number entered :(")

        elif f % 10 == 0:
            messagebox.showinfo(title="Credit Card analyzed successfully",
                                message="The Credit Card exists!")

        else:
            messagebox.showerror(title="Error in Credit Card analysis",
                                 message="The Credit Card does not exist!")

#--------------------------------------------------------
'''
Reader(5355850186163315)
Reader(4569330523507578)
Reader(4569330521793758)
'''
#--------------------------------------------------------

def Shownum():
    entry1.config(show="*") if entry1['show'] == "" else entry1.config(show="")


Window = Tk()
Window.title("Credit Card Reader")
#--------------------------------------------------------

label1 = Label(Window, text="Please write the number of your credit card",
               font=("Constantia", 20))
label1.pack()
#--------------------------------------------------------

entry1 = Entry(Window, font=("Constantia", 14), show="*")
entry1.pack()
#--------------------------------------------------------

showbutton = Button(Window, text="Show Numbers",
                    font=("Constantia", 12, "bold"),
                    command=Shownum)
showbutton.pack()
#--------------------------------------------------------

Submit = Button(Window, text="Check Number",
                font=("Constantia", 14, "bold"),
                command=Reader)
Submit.pack()
#--------------------------------------------------------

Window.mainloop()
