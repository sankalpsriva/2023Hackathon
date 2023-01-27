from tkinter import *
from tkinter.font import Font
from helper import *
from datetime import datetime 
import constants

# Images
gearImage = PhotoImage(file = 'images\gear.png')

button = Button(constants.root, command = lambda: collapse(button))

settings = Button(constants.root, image = gearImage, text = "settings", command = settingsMenu)

resetButton = Button(constants.root, text = "Reset", command = reset) 

mailButton = Button(constants.root, text = "Mail", command = emailMenu, width = 7)

googleButton = Button(constants.root, text = "Google", command = lambda: openWebsite("google.com")) 
canvasButton = Button(constants.root, text = "Canvas", command = lambda: openWebsite("hse.instructure.com")) 
skywardButton = Button(constants.root, text = "Skyward", command = lambda: openWebsite("https://sis.hse.k12.in.us/scripts/wsisa.dll/WService=wsEAplus/seplog01.w")) 
cleverButton = Button(constants.root, text = "Clever", command = lambda: openWebsite("clever.com")) 

timeLabel = Label(constants.root, text = f"{datetime.now().replace(microsecond=0).strftime('%d-%m-20%y - %I:%M:%S')}", 
            width = 40, wraplength = 500, justify = LEFT, 
            bg = rgbToColor(constants.color), fg = rgbToColor(constants.cColor), 
            font = Font(family = "Times New Roman", size = 30, weight = "bold"))

timerButton = Button(constants.root, text = "Start Timer", command = timerCommand) 

frame = Frame(constants.root, bd = 4, bg = "grey")

notes = Text(frame)