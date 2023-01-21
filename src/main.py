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



hit = 700
wit = 100
i = 0 

#changes the width dependent on the clicks
def widht():
    
    global wit, i 
    
    if i < 1:
        wit = int(10)
        button.place(anchor=NW, width=wit, height=hit)
        i = 1
    elif i > 0:
        wit = int(100)
        button.place(anchor=NW, width=wit, height=hit)
        i = 0
    
    
    
    
root = Tk() 

root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb))     

button = Button(root , command = width)
button.place(anchor=NW, width=10, height=hit)
button = Button(root , command = widht)
button.place(anchor=NW, width=wit, height=hit)

settings = Button(root , command = widht)
settings.place(anchor=NW, width=10, height=10)




root.mainloop()