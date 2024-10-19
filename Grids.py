from tkinter import *



def woutGrid():
    def dstry():
        Window.destroy()

    Window = Tk()

    WG = Label(Window, text='Without grid', font=('Constantia', 12, 'bold')).pack()
    Firstname = Label(Window, text='First Name: ').pack()
    Fname = Entry(Window).pack()
    Dstry = Button(Window, text='Return', command=dstry).pack()

    Window.mainloop()

def wGrid():
    def dstry():
        swindow.destroy()

    swindow = Tk()

    WG2 = Label(swindow, text='With grid', font=('Constantia', 12, 'bold')).grid(row=0, column=0, columnspan=2)
    Lastname = Label(swindow, text='Last Name: ').grid(row=1, column=0)
    Lname = Entry(swindow).grid(row=1, column=1)
    Dstry = Button(swindow, text='Return', command=dstry).grid(row=2, column=0, columnspan=2)

    swindow.mainloop()


MWindow = Tk()
MWindow.title('Grid Tester')
Title = Label(MWindow, text='Choose the option to see text', font=('Constantia', 16, 'bold'))
Title.grid(row=0, column=0, columnspan=2)

WithoutGrid = Button(text='Without Grid', font=('Contantia', 12), command=woutGrid)
WithoutGrid.grid(row=1, column=0)
WithGrid = Button(text='With Grid', font=('Constantia', 12), command=wGrid)
WithGrid.grid(row=1, column=1)

MWindow.mainloop()