from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Creating new windows")
root.iconbitmap("images/ericsson-blue-e.ico")
root.geometry("480x240")                            # gives default shape to the app window

def clicked():
    top=Toplevel()
    top.geometry("900x440")
    top.iconbitmap("images/ericsson-blue-e.ico")
    top.title("New Second Window")
    global my_img;my_img=ImageTk.PhotoImage(Image.open("images/36307.jpg"))        # made the variable lbl global so that the image is shown, only way to this right now 
    lbl=Label(top,image=my_img).pack()  
    btn=Button(top,text="Click me to exit and destroy this window",command=top.destroy)     # top.destroy() method destroys the window top and root.destroy() will do the same
    btn.pack(pady=10)

Button(root,text="Click Me!",command=clicked).pack()
root.mainloop()