from tkinter import * 
from helper import *
from PIL import Image, ImageTk
import random, constants, numbers

settingsButton = ImageTk.PhotoImage(Image.open(r"2023Hackathon\src\images\gear.png")) 


constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.rgb))     

button = Button(constants.root, command = lambda: collapse(button))
button.place(anchor = NW, width = 10, height = constants.heightOnClick)

button = Button(constants.root , command = lambda: collapse(button))
button.place(anchor = NW, width = constants.widthOnClick, height = constants.heightOnClick)

settings = Button(constants.root , text = " ", image = settingsButton)
settings.place(anchor = NW, width = 20, height = 20)

constants.root.mainloop()