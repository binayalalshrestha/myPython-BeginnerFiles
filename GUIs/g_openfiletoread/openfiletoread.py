from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    file=open(filepath,'r')
    print(file.read())
    file.close()
    # filepath = filedialog.askopenfilename(initidaldir="D:\\python\\bny_py\\bny\\g_openfiletoread",
    #     title="Open file okay?",
    #     filetypes=(("text files","*.txt"),
    #     ("all files","*.*"))
    #     )
    
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open",command=openFile)
button.pack()
window.mainloop()


#07:55:30