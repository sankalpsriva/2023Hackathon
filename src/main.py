from tkinter import * 
from helper import rgbToColor
from playsound import playsound 

import random, constants
import numbers

global hit 

hit = 100

def width(): 
    hit = int(10) 
    button.place(anchor=NW, width=10, height=hit)
    
    
root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb))     

button = Button(root , command = width)
button.place(anchor=NW, width=10, height=hit)




root.mainloop()