from tkinter import * 
from helper import *
from PIL import Image, ImageTk
import constants, tkinterWidgets, pyglet

constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))     

tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.3, rely = -0.001, width = 200, height = 200)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.05)



constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.mainloop()   