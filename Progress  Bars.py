from tkinter import *
from tkinter.ttk import *
import time


def start():
    GB = 200
    download = 0
    Internetspeed = 4
    while download < GB:
        time.sleep(0.05)
        bar['value'] += ((Internetspeed/GB)*100)
        download += Internetspeed
        progress['text'] = str(int((download/GB)*100)) + '%'
        progress2['text'] = str(download) + ('/') + str(GB) + ' GB Downloaded'
        Window.update_idletasks()

def rStart():
    bar['value'] = 0
    progress['text'] = str(0) + '%'
    progress2['text'] = '0/200 GB Downloaded'




Window = Tk()

bar = Progressbar(Window, orient=HORIZONTAL, length=300)
bar.grid(row=0, column=0, columnspan=2)
progress = Label(Window, text='0%', font=('Constantia', 14))
progress.grid(row=1, column=0, columnspan=2)
progress2 = Label(Window, text='', font=('Constantia', 14))
progress2.grid(row=2, column=0, columnspan=2)

downloadButt = Button(Window, text='Download', command=start)
downloadButt.grid(row=3, column=0)
restartButt = Button(Window, text='Restart', command=rStart)
restartButt.grid(row=3, column=1)
Window.mainloop()
