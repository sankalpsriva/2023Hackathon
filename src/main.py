from tkinter import * 
from helper import rgbToColor
import random

root = Tk() 

rgb = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
root.geometry("800x800")
root.title("Hackathon App")
root.config(bg = rgbToColor(rgb)) 

root.mainloop()