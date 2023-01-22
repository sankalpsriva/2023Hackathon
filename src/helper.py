from tkinter import *
from datetime import datetime
import constants

def rgbToColor(rgb: tuple) -> str: 
    # Code from stackoverflow about changing rgb to tkinter readable color
    return "#%02x%02x%02x" % rgb 

# changes the width dependent on the clicks - Caleb's Code
def collapse(button: Button) -> None:
    if constants.collapsed:
        button.place(anchor = N, width = 100, height = constants.heightOnClick)
        constants.collapsed = False
    else:
        button.place(anchor = N, width = 20, height = constants.heightOnClick)
        constants.collapsed = True
        
def settingsMenu():
    root = Tk()
    root.title("Settings") 
    root.geometry("400x400")
    root.config(bg = rgbToColor(constants.color))
    
    root.mainloop()
    
def labelUpdate(label: Label) -> None:
    label.config(text = f"{datetime.now().replace(microsecond=0)}")
    constants.root.after(1000, lambda: labelUpdate(label)) 
    
    
    

