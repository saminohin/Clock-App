from tkinter import *
from time import * 


def update():
    day_string = strftime("%A")
    day_label.config(text=day_string)

    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()


date_label = Label(window, font=("Ink Free", 30), fg="#00FF00", bg="white")
date_label.pack()

day_label = Label(window, font=("Ink Free", 25), fg="#00FF00", bg="white")
day_label.pack()


time_label = Label(window, font=("Arical", 50), fg="#00FF00", bg="white")
time_label.pack()


update()
window.mainloop()