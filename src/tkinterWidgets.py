from tkinter import *
from tkinter.font import Font
from helper import *
from datetime import datetime 
import constants
yeet = PhotoImage(file='src\images\gear.png')

button = Button(constants.root, command = lambda: collapse(button))
settings = Button(constants.root, image = yeet, text = "settings", command = settingsMenu)
mailButton = Button(constants.root, text = "Mail", command = emailMenu, width = 7)
timeLabel = Label(constants.root, text = f"{datetime.now().replace(microsecond=0)}", 
            width = 30, wraplength = 500, justify = LEFT, 
            bg = rgbToColor(constants.color), fg = rgbToColor(constants.cColor), 
            font = Font(family = "FebruaryNotes-DOwo3", size = 30, weight = "bold"))