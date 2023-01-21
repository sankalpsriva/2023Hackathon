from tkinter import * 
from helper import rgbToColor
from playsound import playsound 

import random, constants


root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb))     

root.mainloop()