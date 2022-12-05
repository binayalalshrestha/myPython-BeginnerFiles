from tkinter import *
import os
dir_path = os.path.dirname(os.path.realpath('prg.png'))

# from PIL import Image, ImageTk

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window forelse
window.geometry("420x420") #change the size of the window
window.title("labels.py") #changing title in the window

icon = PhotoImage(file='gui\logo.png')    #changing the feather picture in the GUI
window.iconphoto(True,icon)

photo = PhotoImage(file='gui/prg.png')

label = Label(window,
             text="Hello Binay", 
             font=('Arial', 40, 'bold'),
             fg='green', 
             bg='black',
             relief=RAISED, #border
             bd=10,
             padx=20,
             pady= 20,
             image= photo,
             compound='bottom')

label.pack() #this will place our label at the center

# label.place(x=0, y=0) #this allows us to place our label wherever we want, we have to give co-ordinates

window.config(background="black") #changing thr background colour


window.mainloop() #place window on computer screen, listen for events

