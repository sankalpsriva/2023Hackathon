from tkinter import *
from helper import *
import json

# JSON 
with open('data\settings.json') as file: 
    file = json.load(file)
    emailEnding = file['userEmail'][str(file['userEmail']).index("@") + 1: ]

# GUI Info
root = Tk()
screensize = "1400x700"
title = "Hackathon App"
color =  (0, 255, 204)# (random.randint(0,255), random.randint(0,255), random.randint(0,255))
cColor = (255, 0, (255 - 204))

# font 
font = file['font']
fontSize = file['fontSize']

# Integers
heightOnClick = 700
widthOnClick = 100
index = 0

# Booleans
collapsed = True
editEnabled = False
