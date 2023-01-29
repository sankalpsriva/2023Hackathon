from tkinter import *
from helper import *
import json, os

# JSON 
with open('data\settings.json') as file: 
    file = json.load(file)
    emailEnding = file['userEmail'][str(file['userEmail']).index("@") + 1: ]

# GUI Info
root = Tk()
screensize = "1400x700"
title = "Hackathon App"
color =  (0, 0, 0)# (random.randint(0,255), random.randint(0,255), random.randint(0,255))
cColor = (255, 0, (255 - 204))
red = (255,0,0)
black = (0,0,0)

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
calender = False

# doubles 
buttonDefaultRelx, buttonDefaultRely = 0.95, 0.01
notesWindowDefaultRelx, notesWindowDefaultRely = 0.5, 0.5

# User Desktop info
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
def desktopData():
 with open(r"data\desktop.json",'r+') as file:
        file_data = json.load(file)
        file_data["DesktopLocation"].append(desktop)
        file_data["DesktopLocation"].append(os.listdir(desktop))
        file.seek(0)
        json.dump(file_data, file, indent = 4)