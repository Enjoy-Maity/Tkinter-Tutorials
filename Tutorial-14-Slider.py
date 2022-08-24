from ssl import VerifyFlags
from tkinter import *

root=Tk()
root.title("Creating slider")
root.geometry("480x240")
vertical=Scale(root,from_=0,to=100)
vertical.pack()

horizontal=Scale(root,from_=0,to=100,orient=HORIZONTAL)     # horizontal creates the slider horizontal on the screen
horizontal.pack()

def slide():
    Label(root,text=horizontal.get()).pack()

"""
# this willmake the size of the window to change as we move the slider

def slide(var):
    Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x400")

horizontal=Scale(root,from_=0,to=100,orient=HORIZONTAL,command=slide)     # horizontal creates the slider horizontal on the screen
horizontal.pack()

# we can also make the size of the window to change according to the number we choose out of the range in the slider and then clicking on a button

def slide():
    Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x400")      # similarly we can use the vertical as well either along with horizontal or without horizontal

horizontal=Scale(root,from_=0,to=100,orient=HORIZONTAL)     # horizontal creates the slider horizontal on the screen
horizontal.pack()

Button(root,text="Click Me!",command=slide).pack()

"""

Button(root,text="Click Me!",command=slide).pack()
root.mainloop()