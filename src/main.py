from tkinter import * 
from helper import *
from PIL import Image, ImageTk
import constants, tkinterWidgets, pyglet

constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))


tkinterWidgets.sedit.place(anchor= NW)
tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.1, rely = -0.001, width = 51, height = 51)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.05)




constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.mainloop()   