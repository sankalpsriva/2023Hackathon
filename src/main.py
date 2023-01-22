from tkinter import * 
from helper import *
from PIL import Image, ImageTk
import random, constants, numbers, tkinterWidgets, playsound

settingsButton = ImageTk.PhotoImage(Image.open(r"2023Hackathon\src\images\gear.png")) 

constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))     

tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = NW, width = 20, height = 20)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.127, rely = -0.001)

constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.mainloop()