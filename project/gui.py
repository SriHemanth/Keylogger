import tkinter as tk
from tkinter import *

def pri():
    print('i am a Tesla CEO')
window = tk.Tk()
window.geometry('450x500')
bt = tk.Button(window,text="Run KeyLogger",bg="white",fg="red")
bt.grid(row=2, column=2)
window.mainloop()
