from tkinter import * 
from helper import rgbToColor
import random, constants


root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb)) 

button = Button(root)
button.place(anchor=N)


root.mainloop()