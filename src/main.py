from tkinter import *
from tkinter import font 
from helper import *
import constants, tkinterWidgets, helper

global label

constants.root.geometry(constants.screensize)

constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))
constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.bind("<Motion>", motion)


# Tkinter Widgets Placement
tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.95, rely = 0.01)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.15)
tkinterWidgets.timerButton.place(anchor = N, relx = 0.95, rely = 0.20)
tkinterWidgets.googleButton.place(anchor = N, relx = 0.95, rely = 0.3)
tkinterWidgets.canvasButton.place(anchor = N, relx = 0.95, rely = 0.35)
tkinterWidgets.skywardButton.place(anchor = N, relx = 0.95, rely = 0.4)
tkinterWidgets.cleverButton.place(anchor = N, relx = 0.95, rely = 0.45)


# Normally this code would not be here but it isn't working without it being in the same file

def editEnable(tkFrame: Frame, tkSettings: Button, editButton: Button):
    if not constants.editEnabled:
        editButton.config(bg = "green")
        make_draggable(tkFrame)
        make_draggable(tkSettings)      
        constants.editEnabled = True
    else:
        editButton.config(bg = "white")
        make_undragable(tkFrame)
        make_undragable(tkSettings)
        constants.editEnabled = False
        
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
frame.place(x = 380, y = 100)
make_draggable(frame)
make_draggable(tkinterWidgets.settings)

notes = Text(frame)
notes.pack()

layoutEdit = Button(constants.root, text = "Editor", width = 7)
layoutEdit.config(command = lambda: editEnable(tkFrame = frame, tkSettings = tkinterWidgets.settings, editButton = layoutEdit))
layoutEdit.place(anchor = N, relx = 0.02, rely = 0)


constants.root.mainloop()   