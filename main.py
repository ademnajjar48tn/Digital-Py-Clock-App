from datetime import datetime
from tkinter import Tk
from tkinter import Label
import time
import sys

window = Tk()

window.title("Digital Clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")
    time.config(text=timeVar)
    time.after(200, get_time)

time = Label(window, font=("Helvetica", 90), bg="black", fg="white")

time.pack()

get_time()

window.mainloop()
