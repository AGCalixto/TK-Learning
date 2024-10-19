from tkinter import *
from tkinter import ttk

Window = Tk()

notebook = ttk.Notebook(Window)
Tab1 = Frame(notebook)
Tab2 = Frame(notebook)

notebook.add(Tab1, text='Tab A')
notebook.add(Tab2, text='Tab B')
notebook.pack(expand=True, fill='both')

Label(Tab1, text='You are Welcome, This is Tab A', width=50, height=25).pack()
Label(Tab2, text='Farewell, This is Tab B', width=50, height=25).pack()

Window.mainloop()
