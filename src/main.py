from tkinter import *
from tkinter import font 
from helper import *
import constants, tkinterWidgets, helper

global label

constants.root.geometry(constants.screensize)

constants.root.title(constants.title)
constants.root.config(bg = rgbToColor(constants.color))
constants.root.after(1000, lambda: labelUpdate(tkinterWidgets.timeLabel))
constants.root.bind("<Motion>", motion)


# Tkinter Widgets Placement
tkinterWidgets.button.place(anchor = NW, height = constants.heightOnClick)
tkinterWidgets.settings.place(anchor = N, relx = 0.95, rely = 0.01)
tkinterWidgets.timeLabel.place(anchor = N, relx = 0.5, rely = -0.001)
tkinterWidgets.calenderButton.place(anchor = N, relx = 0.95, rely = 0.25)
tkinterWidgets.mailButton.place(anchor = N, relx = 0.95, rely = 0.15)
tkinterWidgets.timerButton.place(anchor = N, relx = 0.95, rely = 0.20)

# redirecting buttons
tkinterWidgets.googleButton.place(anchor = N, relx = 0.95, rely = 0.3)
tkinterWidgets.canvasButton.place(anchor = N, relx = 0.95, rely = 0.35)
tkinterWidgets.skywardButton.place(anchor = N, relx = 0.95, rely = 0.4)
tkinterWidgets.cleverButton.place(anchor = N, relx = 0.95, rely = 0.45)
tkinterWidgets.notesButton.place(anchor = N, relx = 0.95, rely = 0.5)
tkinterWidgets.desmosButton.place(anchor = N, relx = 0.95, rely = 0.55)
tkinterWidgets.graphingButton.place(anchor = N, relx = 0.95, rely = 0.6)


# calender 

day1 = Button(constants.root, text = "Sunday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day1.place(anchor = N, relx = 0.2, rely = 0.15)
    
day2 = Button(constants.root, text = "Monday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day2.place(anchor = N, relx = 0.3, rely = 0.15)
      
day3 = Button(constants.root, text = "Tuesday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day3.place(anchor = N, relx = 0.4, rely = 0.15)
      
day4 = Button(constants.root, text = "Wednesday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day4.place(anchor = N, relx = 0.5, rely = 0.15)
      
day5 = Button(constants.root, text = "Thursday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day5.place(anchor = N, relx = 0.6, rely = 0.15)
      
day6 = Button(constants.root, text = "Friday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day6.place(anchor = N, relx = 0.7, rely = 0.15)
      
day7 = Button(constants.root, text = "Saturday", font = ("Times New Roman", 10), width = 17, relief = SUNKEN)
day7.place(anchor = N, relx = 0.8, rely = 0.15)  

base = 0
currentMonth = datetime.now().strftime('%m')
#we are making all of the days a proof of concept becasue it would take way to long to put every single day of the month and week into a 
if currentMonth == '01':
    for e in range(1,6):
        for i in range(1,8):
            if base + i < 32:
                days = Button(constants.root, text =  base + i, font = ("Times New Roman", 10), width = 10, command = lambda: dayNotes(currentMonth, base+i))
                days.place(anchor=N, relx = 0.2+0.1*(i-1) ,rely = 0.2+0.15*(e-1))
            else:
                days = Button(constants.root, text =  " ", font = ("Times New Roman", 10), width = 10)
                days.place(anchor=N, relx = 0.2+0.1*(i-1) ,rely = 0.2+0.15*(e-1))
        base = i*e
        
if currentMonth == '02':
    for e in range(1,6):
        for i in range(1,8):
            if base + i < 28:
                days = Button(constants.root, text =  base + i, font = ("Times New Roman", 10), width = 10)
                days.place(anchor=N, relx = 0.2+0.1*(i-1) ,rely = 0.2+0.15*(e-1))
            else:
                days = Button(constants.root, text =  " ", font = ("Times New Roman", 10), width = 10)
                days.place(anchor=N, relx = 0.2+0.1*(i-1) ,rely = 0.2+0.15*(e-1))

            

# Normally this code would not be here but it isn't working without it being in the same file

def editEnable(tkSettings: Button, editButton: Button):
    if not constants.editEnabled:
        editButton.config(bg = "green")
        make_draggable(tkSettings)      
        constants.editEnabled = True
    else:
        editButton.config(bg = "white")
        make_undragable(tkSettings)
        constants.editEnabled = False
        
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y
    widget.place(x=x, y=y)


# make_draggable(frame)
make_draggable(tkinterWidgets.settings)

layoutEdit = Button(constants.root, text = "Editor", width = 7)
layoutEdit.config(command = lambda: editEnable(ztkSettings = tkinterWidgets.settings, editButton = layoutEdit))
layoutEdit.place(anchor = N, relx = 0.02, rely = 0)

saveDesktop = Button(constants.root, text = "Save Desktop", width = 10, command = lambda: constants.desktopData())
saveDesktop.place(anchor = N, relx = 0.95, rely = 0.65)

constants.root.mainloop()   