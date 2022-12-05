from tkinter import *

# entry widget = textbox that accepts a single line of user input

def submit():  #this is the submit function
    username = entry.get()
    print("Hello "+username)
    # entry.config(state=DISABLED)  # This will only allow one entry, and later the entry will be disabled

def delete():  #this is the delete function
    entry.delete(0,END)

def backspace():  #this is the backspace function
    entry.delete(len(entry.get())-1,END)


window = Tk()

window.geometry("420x420") #change the size of the window
window.title("entry box with submit, delete and backspace") #changing title in the window

entry = Entry(window,
                font=("Arial",15),
                fg='green',
                bg='black',
                #show="*"#with show, whatever you type will be turned into *
                )

label = Label(window,relief=RAISED,bd=10,padx=20,pady=20)

entry.insert(0,'Delete to entry')  #This will already be typed in the entry box

entry.pack(side=LEFT)

submit_button = Button(window,text="submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="backspace",command=backspace)
backspace_button.pack(side=RIGHT)

window.config(background="black") #changing thr background colour

window.mainloop()