from distutils.cmd import Command
from tkinter import *

root=Tk()



# e=Entry(root,width=50) # width sets the width of the entry box
#e=Entry(root,width=50, fg="white",bg="green") # fg sets the text color snd bg sets the background color

e=Entry(root,width=50, fg="white",bg="green",borderwidth=4) # borderwidth sets the width of the entry 
e.insert(0,"Enter Your Name : ") # insert() gives default value inside the text box 

def click():
    hello="Hello "+e.get()
    mylabel=Label(root,text=hello)
    mylabel.pack()
mybutton=Button(root,text="Click Me!",command=click)

e.pack()
mybutton.pack()

root.mainloop()