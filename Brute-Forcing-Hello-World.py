# How to brute force 'Hello World'
import random
import time
from tkinter import *


def Submit():
    finish = entry.get()
    start = [''] * len(finish)

    letters = ['a', 'b', 'c', 'd', 'e',
               'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y',
               'z', ' ',
               'A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O',
               'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y',
               'Z']


    current = 0
    while [start[x] for x in range(len(start))] != [finish[y] for y in range(len(finish))]:
        if start[current] != finish[current]:
            time.sleep(0.0001)
            start[current] = random.choice(letters)
            label3['text'] = start
            Window.update()
        else:
            current += 1



Window = Tk()
Window.title('Brute Forcing Words')
label = Label(Window, text='Brute Forcing Words', font=('Times New Roman', 18, 'bold'))
label.grid(row=0, column=0, columnspan=3)

label2 = Label(Window, text='Enter the Word you want to brute force', font=('Times New Roman', 16, 'italic'))
label2.grid(row=1, column=1)

entry = Entry(Window, font=('Times New Roman', 14))
entry.grid(row=2, column=1)

submit_button = Button(Window, text='Let\'s Go!', font=('Times New Roman', 14, 'bold'), command=Submit)
submit_button.grid(row=3, column=1)

label3 = Label(Window, text='', font=('Times New Roman', 15))
label3.grid(row=4, column=1)
Window.mainloop()

'''
print([start[x] for x in range(len(start))])
print([finish[y] for y in range(len(finish))])
'''
