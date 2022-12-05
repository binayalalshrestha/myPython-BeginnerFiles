from tkinter import *
from tkinter import messagebox #import messagebox library

window = Tk()

def click():

    # (1) SHOW INFO :
    # messagebox.showinfo(title='This is an info message box',message='You are a person',icon='info')


    
    # (2) SHOW WARNING :
    ''' if we add while loop, the messagebox will keep popping up-
        while(True):
            messagebox.showwarning(title='WARNING',message='You are a VIRUS!!!!')
    '''
    # messagebox.showwarning(title='WARNING',message='You have a VIRUS!!!!',icon='warning')


    # (3) SHOW ERROR :
    # messagebox.showerror(title='ERROR!',message='Something went wrong!',icon='error)


    # (4) ASK OK CANCEL :
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing?'):
    #     print('You did a thing! :) ')
    # else:
    #     print('You canceled a thing! :( ')


    # (5) ASK RETRY CANCEL :
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to retry the thing?'):
    #     print('You retried a thing! :) ')
    # else:
    #     print('You canceled a thing! :( ')


    # (6) ASK YES OR NO :
    # if messagebox.askyesno(title='ask yes or no',message='Do you like cake?'):
    #     print('I like care too :)')
    # else:
    #     print('Why do you not like cake? :(')


    # (7) ASK QUESTION :
    # answer =messagebox.askquestion(title='ask question',message='Do you like pie?')
    # if(answer == 'yes'):
    #     print('I like pie too :)')
    # else:
    #     print('Why do you not like pie? :(')


    # (8) AK YES NO CANCEL :
    # answer = messagebox.askyesnocancel(title=' Yes no cancel',message='Do you like to code?')
    # if(answer==True):
    #     print("you like to code too :) ")
    # elif(answer==False):
    #     print("Then why are you here :( ? ")
    # else:
    #     print("You have dodged the question -_- ")


button = Button(
    window,
    command=click,
    text='click me'
    )

button.pack()

window.mainloop()