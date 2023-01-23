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


def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


frame = Frame(constants.root, bd=4, bg="grey")
frame.place(x=10, y=10)
make_draggable(frame)
make_draggable(tkinterWidgets.settings)

notes = Text(frame)
notes.pack()


constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.mainloop()   