from tkinter import *
from datetime import datetime
from playsound import playsound
from email.message import EmailMessage
import constants, smtplib, ssl

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
        
def settingsMenu():
    
    root = Tk()
    root.title("Settings") 
    root.geometry("400x400")
    root.config(bg = rgbToColor(constants.color))
    
    playsound(r"audio\buttonClick.mp3")
    
    root.mainloop()

def emailMenu():
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
    
def sendMail(message: str, recipent: str) -> None: 
    print(f'smtp.{constants.emailEnding}')
    print(constants.file['userPassword'])
    print(f'{recipent}')
#    with smtplib.SMTP_SSL(f'smtp.{constants.emailEnding}', 465, context = ssl.create_default_context()) as s:
#        s.login(constants.file['userEmail'], constants.file['userPassword'])
#        s.sendmail(constants.file['userEmail'], recipent, message)
#        print("message sent")
    
    
def labelUpdate(label: Label) -> None:
    label.config(text = f"{datetime.now().replace(microsecond=0)}")
    constants.root.after(1000, lambda: labelUpdate(label)) 


#    makes items draggable
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

def timerCommand():
    root = Tk()
    
    root.title("Timer")
    root.geometry("500x500")
    root.config(bg = rgbToColor(constants.color))

    
