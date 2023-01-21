from tkinter import * 
from helper import rgbToColor
from PIL import Image, ImageTk

import random, constants
import numbers

global hit 

hit = 100

def collapse(): 
    hit = 10
    button.place(anchor=NW, width=10, height=hit)



hit = 700
wit = 100
i = 0 

#changes the width dependent on the clicks
def collapse():
    
    global wit, i 
    
    if i < 1:
        wit = 10
        button.place(anchor=NW, width=wit, height=hit)
        i = 1
    elif i > 0:
        wit = 100
        button.place(anchor=NW, width=wit, height=hit)
        i = 0
    
    
    
    
root = Tk() 

settingsButton = PhotoImage(file = "2023Hackathon\src\images\gear.png").subsample(1,2)


root.geometry(constants.screensize)
root.title(constants.title)
root.config(bg = rgbToColor(constants.rgb))     

button = Button(root , command = collapse)
button.place(anchor=NW, width=10, height=hit)

button = Button(root , command = collapse)
button.place(anchor=NW, width=wit, height=hit)

settings = Button(root , command = collapse)
settings.place(anchor=NW, image = settingsButton, width=10, height=10)

root.mainloop()