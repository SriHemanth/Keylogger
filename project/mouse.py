from pynput.mouse import Controller
from pynput.keyboard import Controller
def mouse_control():
    mouse = Controller()
    mouse.position = (100,100)

def board_control():
    keyboard = Controller()
    keyboard.type("I am doing wonderful job")

board_control()
