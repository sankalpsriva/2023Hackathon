from tkinter import *
from helper import *
from datetime import datetime 
import constants

button = Button(constants.root, command = lambda: collapse(button))
settings = Button(constants.root, text = " ", command = settingsMenu)
timeLabel = Label(constants.root, text = f"{datetime.now().replace(microsecond=0)}", 
            width = 30, wraplength = 500, justify = LEFT, 
            bg = rgbToColor(constants.color), fg = rgbToColor(constants.cColor))