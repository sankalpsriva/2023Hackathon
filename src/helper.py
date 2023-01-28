from tkinter import *
from datetime import datetime
from playsound import playsound
from email.message import EmailMessage
import constants, smtplib, ssl, webbrowser, json, os

mouseX, mouseY = 0, 0

def submitNotes(notes: Text):
 with open(r"data\notes.json",'r+') as file:
        file_data = json.load(file)
        file_data["Notes"].append(notes.get(1.0, "end-1c"))
        file.seek(0)
        
        print(file_data)
        json.dump(file_data, file, indent = 4)
        

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
    playsound(r"audio\buttonClick.mp3")
# settings
def settingsMenu() -> None:
    
    root = Tk()
    root.title("Settings") 
    root.geometry("400x400")
    root.config(bg = rgbToColor(constants.color))
    
    playsound(r"audio\buttonClick.mp3")
    
    root.mainloop()

# email 
def emailMenu() -> None:
    playsound(r"audio\buttonClick.mp3")
    
    root = Tk()
    root.title("Email")
    root.geometry("500x500")
    root.config(bg = rgbToColor(constants.color))
    
    subjectLabel = Label(root, text = "Subject", font = ("Times New Roman", 10), fg = rgbToColor(constants.cColor), bg = rgbToColor(constants.color))
    subjectEntry = Entry(root, width = 25)
    subjectEntry.focus_set()
    
    recipentLabel = Label(root, text = "Recipent", font = ("Times New Roman", 10), fg = rgbToColor(constants.cColor), bg = rgbToColor(constants.color))
    recipentEntry = Entry(root, width = 35)  
    
    submitButton = Button(root, text = "Submit", font = ("Times New Roman", 10), command = lambda: sendMail("Hello", recipentEntry.get()))
     
    
    subjectEntry.place(anchor = N, relx = 0.5, rely = 0.15)   
    recipentEntry.place(anchor = N, relx = 0.5, rely = 0.3) 
    
    subjectLabel.place(anchor = N, relx = 0.5, rely = 0.1)
    recipentLabel.place(anchor = N, relx = 0.5, rely = 0.25)
    
    submitButton.place(anchor = N, relx = 0.5, rely = 0.85)
    
    root.mainloop()
    
def calenderMenu() -> None:
    root = Tk()
    root.title("Calender")
    root.geometry("1000x500")
    root.config(bg = rgbToColor(constants.color))
     
    playsound(r"audio\buttonClick.mp3")

    day1 = Button(root, text = "Sunday", font = ("Times New Roman", 10),width = 17)
    day1.place(anchor = N, relx = 0.2, rely = 0.15)
    
    day2 = Button(root, text = "Monday", font = ("Times New Roman", 10), width = 17 )
    day2.place(anchor = N, relx = 0.3, rely = 0.15)
      
    day3 = Button(root, text = "Tuesday", font = ("Times New Roman", 10), width = 17)
    day3.place(anchor = N, relx = 0.4, rely = 0.15)
      
    day4 = Button(root, text = "Wednesday", font = ("Times New Roman", 10), width = 17)
    day4.place(anchor = N, relx = 0.5, rely = 0.15)
      
    day5 = Button(root, text = "Thursday", font = ("Times New Roman", 10), width = 17)
    day5.place(anchor = N, relx = 0.6, rely = 0.15)
      
    day6 = Button(root, text = "Friday", font = ("Times New Roman", 10), width = 17)
    day6.place(anchor = N, relx = 0.7, rely = 0.15)
      
    day7 = Button(root, text = "Saterday", font = ("Times New Roman", 10), width = 17)
    day7.place(anchor = N, relx = 0.8, rely = 0.15)  
    
    
    root.mainloop()
    
    
    
    
    
    
    
def sendMail(message: str, recipent: str) -> None: 
    print(f'smtp.{constants.emailEnding}')
    print(constants.file['userPassword'])
    print(f'{recipent}')
#    with smtplib.SMTP_SSL(f'smtp.{constants.emailEnding}', 465, context = ssl.create_default_context()) as s:
#        s.login(constants.file['userEmail'], constants.file['userPassword'])
#        s.sendmail(constants.file['userEmail'], recipent, message)
#        print("message sent")

def reset(set: Button, tkFrame: Frame):
    set.place(anchor = N, relx = constants.buttonDefaultRelx, rely = constants.buttonDefaultRely)  
    tkFrame.place(anchor = N, relx = constants.notesWindowDefaultRelx, rely = constants.notesWindowDefaultRely) 
    
def labelUpdate(label: Label) -> None:
    label.config(text = f"{datetime.now().replace(microsecond=0).strftime('%d-%m-20%y - %I:%M:%S')}")
    constants.root.after(1000, lambda: labelUpdate(label)) 

def editEnable(tkFrame: Frame, tkSettings: Button, editButton: Button):
    playsound(r"audio\buttonClick.mp3")
    if not constants.editEnabled:
        editButton.config(bg = "green")
        make_draggable(tkFrame)
        make_draggable(tkSettings)      
        constants.editEnabled = True
    else:
        editButton.config(bg = "white")
        make_undragable(tkFrame)
        make_undragable(tkSettings)
        constants.editEnabled = False

def motion(event):
    mouseX, mouseY = event.x, event.y
    
#    makes items draggable
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    
def make_undragable(widget):
    widget.unbind("<Button-1>")
    widget.unbind("<B1-Motion>")
    
def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() + widget._drag_start_x + event.x
    y = widget.winfo_y() + widget._drag_start_y + event.y
    widget.place(x=x, y=y)

def timerCommand() -> None:
    root = Tk()
    
    root.title("Timer")
    root.geometry("500x500")
    root.config(bg = rgbToColor(constants.color))

    playsound(r"audio\buttonClick.mp3")
    
def openWebsite(url: str) -> None:
    webbrowser.open(url)
    
def saveNotesToTextFile():
    with open(r"data\notes.json", "r+") as jsonFile, open(r"userNotes\userNotes.txt", 'a') as txtFile:
        jsonFileReadable = json.load(jsonFile)["Notes"]
        for line in jsonFileReadable:
            txtFile.write(f"\n{line}")  
        jsonFileReadable = { 
                            "Notes" : [] 
        }
        
    with open(r'data\notes.json', 'w') as file:
        json.dump(jsonFileReadable, file)
    

def notesMenu():
    root = Tk() 
    root.title("Notes")
    root.geometry("700x700")
    root.config(bg = rgbToColor(constants.color))
    
    frame = Frame(root, bd=4, bg="grey")
    frame.place(x = 25, y = 100)
    
    notes = Text(frame)
    notes.pack()

    submitButton = Button(root, text = "Submit", width = 5, command = lambda: submitNotes(notes))
    submitButton.place(anchor = N, relx = 0.65, rely = 0.8)

    saveNotesToTextButton = Button(root, text = "Save Notes", width = 13, command = saveNotesToTextFile)
    saveNotesToTextButton.place(anchor = N, relx = 0.35, rely = 0.8)

    playsound(r"audio\buttonClick.mp3")

def dayNotes(month, day):
    root = Tk() 
    root.title("Notes")
    root.geometry("700x700")
    root.config(bg = rgbToColor(constants.color))
    
    frame = Frame(root, bd=4, bg="grey")
    frame.place(x = 25, y = 100)
    
    notes = Text(frame)
    notes.pack()
    monday = Label(root, text = month)
    monday.place(anchor = N, relx = 0.5, rely = 0.35)

    submitButton = Button(root, text = "Submit", width = 5, command = lambda: submitNotes(notes))
    submitButton.place(anchor = N, relx = 0.65, rely = 0.8)

    saveNotesToTextButton = Button(root, text = "Save Notes", width = 13, command = saveNotesToTextFile)
    saveNotesToTextButton.place(anchor = N, relx = 0.35, rely = 0.8)

    playsound(r"audio\buttonClick.mp3")
