from tkinter import *

# from PIL import Image, ImageTk

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window forelse
window.geometry("420x420") #change the size of the window
window.title("Bnay's first GUI program") #changing title in the window

icon = PhotoImage(file='gui\logo.png')    #changing the feather picture in the GUI
window.iconphoto(True,icon)


window.config(background="black") #changing thr background colour


window.mainloop() #place window on computer screen, listen for events

