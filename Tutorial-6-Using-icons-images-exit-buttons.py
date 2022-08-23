from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Using Icons,Images and Exit buttons")

#root.iconbitmap('c:/users/emaienj/documents/tkinter-tutorials/images/ericsson-blue-e.ico')     # iconbit uses the path or the name of the image to use it as icon
root.iconbitmap('images/ericsson-blue-e.ico')

my_img=ImageTk.PhotoImage(Image.open("images/toppng.com-ericsson-logo-ericsson-logo-transparent-1302x520.png"))     # needed to add image to the gui app
my_label=Label(root,image=my_img)
my_label.pack()

button_quit=Button(root,text="Exit",command=root.quit)      # root.quit is a method used to end the root mainloop
button_quit.pack()

root.mainloop()