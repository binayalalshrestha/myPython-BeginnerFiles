# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered pizza!")
    elif(x.get()==1):
        print("You ordered hamburger!")
    elif(x.get()==2):
        print("You ordered hotdog!")
    else:
        print("Huh!?")

window = Tk()

pizzaImage = PhotoImage(file='gui\pizza.png')
hamburgerImage = PhotoImage(file='gui\hamburger.png')
hotdogImage = PhotoImage(file='gui\hotdog.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

window.title("radiobutton.py")

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
    text=food[index], #adds text to radio buttons
    variable=x, #groups radiobuttons together if they share the same variable
    value=index, #assigns each radiobutton a different value
    padx=25, #adds padding on x-axis
    font=("Impact",50),
    image=foodImages[index], #adds image to radiobutton
    compound='left', #adds image and text (left-side_)
    indicatoron=0, #elimates circle indicators
    width = 375, #sets width of radio buttons
    command=order #set command of radiobutton to function
    )

    radiobutton.pack(anchor=W)


window.config(background="black")
window.mainloop()



#07:00:45