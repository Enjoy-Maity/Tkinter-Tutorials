from tkinter import *

root=Tk()
root.geometry("480x240")
root.title("Creating Checkbox")
root.iconbitmap("images/ericsson-blue-e.ico")

#var=IntVar()    # will get only 0 or 1
var=StringVar()

c=Checkbutton(root,text="Check this box. I dare you!",variable=var,onvalue="ON",offvalue="OFF")      # onvalue and the offvalue gives the value to the variable var to hold when checkbocx clicked or not 
c.deselect()        # deselect() deselects the checkbox by-default so that the checkbox is not selected and we don't have to face the None value passing glitch
c.pack()

def show():
    my_label=Label(root,text=var.get()).pack()

my_button=Button(root,text="Click me to display the checkbox selected",command=show).pack()
root.mainloop()