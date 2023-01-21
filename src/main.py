from tkinter import * 
from helper import rgbToColor

import random, constants
import numbers



hit = int(100)

def widht(): 
    global hit 
    hit = int(10) 
    button.place(anchor=NW, width=10, height=hit)
    
    
root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb)) 

button = Button(root , command = widht)
button.place(anchor=NW, width=10, height=hit)




root.mainloop()






