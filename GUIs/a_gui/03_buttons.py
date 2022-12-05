from tkinter import *

# button = you click it, then it does stuff

count = 0

def click():
    global count
    count+=1
    print(count)

window = Tk()

window.geometry("420x420") #change the size of the window
window.title("buttons.py") #changing title in the window

photo = PhotoImage(file='gui\like.png')

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans",15),
                fg="black",
                bg="white",
                activeforeground="black",
                activebackground="white",
                state=ACTIVE,
                relief=RAISED, #border
                bd=10,
                padx=20,
                pady= 20,
                image=photo,
                compound='top')
button.pack()

window.mainloop()