from tkinter import *
import constants

def rgbToColor(rgb: tuple) -> str: 
    # Code from stackoverflow about changing rgb to tkinter readable color
    return "#%02x%02x%02x" % rgb 

# changes the width dependent on the clicks - Caleb's Code
def collapse(button: Button) -> None:
    if constants.collapsed:
        button.place(anchor = NW, width = 10, height = constants.heightOnClick)
        constants.collapsed = False
    else:
        button.place(anchor = NW, width = 100, height = constants.heightOnClick)
        constants.collapsed = True
        
def settingsMenu(root: Tk):
    pass
    
    

