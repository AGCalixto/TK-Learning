# To calculate the number of bits necessary to cover a number, use the following formula
# Num of Bits = log2(number) + 1

# Use the math library
import math
from tkinter import *


def bit_calculation():
    number = int(entry1.get())
    bits = math.floor(math.log2(number)) + 1
    label2['text'] = f'{str(bits)} bits'


Window = Tk()
title = (Label(Window, text='Bit Calculator'))
title.grid(row=0, column=0, columnspan=2)
label1 = (Label(Window, text='Calculate the bits of: '))
label1.grid(row=1, column=0)
entry1 = (Entry(Window))
entry1.grid(row=1, column=1)

button1 = (Button(Window, text='Calculate', command=bit_calculation))
button1.grid(row=2, column=0, columnspan=2)
label2 = (Label(Window, text=''))
label2.grid(row=3, column=0, columnspan=2)

Window.mainloop()
