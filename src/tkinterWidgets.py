from tkinter import *
from tkinter.font import Font
from helper import *
from datetime import datetime 
import constants

# Images
gearImage = PhotoImage(file = 'images\gear.png')

button = Button(constants.root, command = lambda: collapse(button))

settings = Button(constants.root, image = gearImage, text = "settings", command = settingsMenu)

mailButton = Button(constants.root, text = "Mail", command = emailMenu, width = 7)

layoutEdit = Button(constants.root, text = "Editor", command = None, width = 7)

timeLabel = Label(constants.root, text = f"{datetime.now().replace(microsecond=0).strftime('%d-%m-20%y - %I:%M:%S')}", 
            width = 40, wraplength = 500, justify = LEFT, 
            bg = rgbToColor(constants.color), fg = rgbToColor(constants.cColor), 
            font = Font(family = "Times New Roman", size = 30, weight = "bold"))

timerButton = Button(constants.root, text = "Start Timer", command = timerCommand) 

frame = Frame(constants.root, bd = 4, bg = "grey")

notes = Text(frame)