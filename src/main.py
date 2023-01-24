from tkinter import *
from tkinter import font 
from helper import *
import constants, tkinterWidgets, helper

global label

constants.root.geometry(constants.screensize)
constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))
constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))


# Tkinter Widgets Placement
tkinterWidgets.layoutEdit.place(anchor= NW)
tkinterWidgets.button.place(anchor = NW, width = 10, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.95, rely = 0.01, width = 51, height = 51)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.15)
tkinterWidgets.timerButton.place(anchor = N, relx = 0.95, rely = 0.20)
tkinterWidgets.frame.place(anchor = N, relx = 0.5, rely = 0.2)
tkinterWidgets.notes.pack()

helper.make_draggable(tkinterWidgets.frame)
helper.make_draggable(tkinterWidgets.settings)

fonts = list(font.families())

# Below is stuff to find all font and find the one we love best

# def update(): 
#     label.config(font = (fonts[constants.index], 10))
#     print(f"Current Font: {fonts[constants.index]}")
#     label.after(2000, update)
#     constants.index += 1
        
# with open("fonts.txt", "a") as file:
#     [file.write(i) for i in fonts]

# root = Tk() 

# label = Label(root, text = "Hello, World")
# label.place(anchor = N, relx = 0.5, rely = 0.5)
# label.after(2000, update)

# root.mainloop()
constants.root.mainloop()   