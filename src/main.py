from tkinter import * 
from helper import *
from PIL import Image, ImageTk
import constants, tkinterWidgets, pyglet, helper


constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))


tkinterWidgets.layoutEdit.place(anchor= NW)
tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.95, rely = 0.01, width = 51, height = 51)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.15)
tkinterWidgets.timerButton.place(anchor = N, relx = 0.95, rely = 0.20)

frame = Frame(constants.root, bd=4, bg="grey")
frame.place(x=10, y=10)
helper.make_draggable(frame)
helper.make_draggable(tkinterWidgets.settings)

notes = Text(frame)
notes.pack()


constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.mainloop()   