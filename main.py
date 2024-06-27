from datetime import datetime
from tkinter import Tk
from tkinter import Label
import time

window = Tk()

master.title("Digital Clock")
 
time = Label(master, font=("Helvetica", 90), bg="black", fg="white")

time.pack()

window.mainloop()
