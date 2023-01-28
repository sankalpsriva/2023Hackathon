from tkinter import *
from tkinter.font import Font
from helper import *
from datetime import datetime 
import constants

# Images
gearImage = PhotoImage(file = 'images\gear.png')

# labels

# calander days

sunday = Label(constants.root, text ="Sunday")
sunday.place(anchor = N, relx = -1, rely = 0.35)

monday = Label(constants.root, text ="Monday")
monday.place(anchor = N, relx = -1, rely = 0.35)

tuesday = Label(constants.root, text ="Tuesday")
tuesday.place(anchor = N, relx = -1, rely = 0.35)

wednesday = Label(constants.root, text ="Wednesday")
wednesday.place(anchor = N, relx = -1, rely = 0.35)

thurday = Label(constants.root, text ="Thursday")
thurday.place(anchor = N, relx = -1, rely = 0.35)

friday = Label(constants.root, text ="Friday")
friday.place(anchor = N, relx = -1, rely = 0.35)

saturday = Label(constants.root, text ="Saturday")
saturday.place(anchor = N, relx = -1, rely = 0.35)


# usefull stuff needs better name
button = Button(constants.root, command = lambda: collapse(button) )

settings = Button(constants.root, image = gearImage, text = "settings", command = settingsMenu)

resetButton = Button(constants.root, text = "Reset", command = reset,) 

mailButton = Button(constants.root, text = "Mail", command = emailMenu, width = 10)

calenderButton = Button(constants.root, text = "Calender", command = calenderMenu, width = 10) 

notesButton = Button(constants.root, text = "Notes", command = notesMenu, width = 10)

# Redirecting Buttons

googleButton = Button(constants.root, text = "Google", command = lambda: openWebsite("google.com")) 
canvasButton = Button(constants.root, text = "Canvas", command = lambda: openWebsite("hse.instructure.com")) 
skywardButton = Button(constants.root, text = "Skyward", command = lambda: openWebsite("https://sis.hse.k12.in.us/scripts/wsisa.dll/WService=wsEAplus/seplog01.w")) 
cleverButton = Button(constants.root, text = "Clever", command = lambda: openWebsite("clever.com")) 
desmosButton = Button(constants.root, text = "Calculator", command = lambda: openWebsite("https://www.desmos.com/scientific")) 
graphingButton = Button(constants.root, text = "Graphing", command = lambda: openWebsite("https://www.desmos.com/calculator"))
tutoringButton = Button(constants.root, text = "Khan", command = lambda: openWebsite("https://www.khanacademy.org/"))
wordButton = Button(constants.root, text = "Word", command = lambda: openWebsite("https://www.office.com/launch/word?auth=2"))
powerPointButton = Button(constants.root, text = "Power Point", command = lambda: openWebsite("https://www.office.com/launch/powerpoint?auth=2"))
excelButton = Button(constants.root, text = "Excel", command = lambda: openWebsite("https://www.office.com/launch/excel?auth=2"))

timeLabel = Label(constants.root, text = f"{datetime.now().replace(microsecond=0).strftime('%d-%m-20%y - %I:%M:%S')}", 
            width = 40, wraplength = 500, justify = LEFT, 
            bg = rgbToColor(constants.color), fg = rgbToColor(constants.cColor), 
            font = Font(family = "Times New Roman", size = 30, weight = "bold"))

timerButton = Button(constants.root, text = "Start Timer", command = timerCommand, width = 10) 